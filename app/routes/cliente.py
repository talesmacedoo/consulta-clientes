from flask import Blueprint, render_template, redirect, url_for, request
from database.models.cliente import Cliente

cliente_route = Blueprint('cliente', __name__)

@cliente_route.route('/')
def lista_cliente():
    """ listar os clientes """
    clientes = Cliente.select()
    return render_template('lista_cliente.html', clientes=clientes)
    
@cliente_route.route('/adicionar-cliente')
def adicionar_cliente():
    """ listar os clientes """
    return render_template('adicionar_cliente.html')
    

@cliente_route.route('/', methods=['POST'])
def inserir_cliente():
    """ Inserir os dados do cliente via formulário HTML """

    novo_usuario = Cliente.create(
        nome=request.form.get('nome'),
        cpf=request.form.get('cpf'),
        celular1=request.form.get('celular1'),
        celular2=request.form.get('celular2'),
        data_de_nascimento=request.form.get('data_de_nascimento'),
        data_atualizacao=request.form.get('data_atualizacao'),
    )

    return redirect(url_for('cliente.lista_cliente'))

@cliente_route.route('/new')
def form_cliente():
    """ formulario para cadastrar um cliente """
    return render_template('form_cliente.html')
    

@cliente_route.route('/<int:cliente_id>')
def detalhe_cliente(cliente_id):
    """ exibir detalhes do cliente """
    
    cliente = Cliente.get_by_id(cliente_id)
    return render_template('detalhe_cliente.html', cliente=cliente)
    
@cliente_route.route('/buscar')
def buscar_cliente():
    """ Buscar cliente por CPF ou telefone """
    valor = request.args.get('valor')
    tipo = request.args.get('tipo')

    if not valor or not tipo:
        return "Parâmetros 'valor' e 'tipo' são obrigatórios", 400


    # Decide qual campo consultar
    if tipo == 'cpf':
        cliente = Cliente.get_or_none(Cliente.cpf == valor)
    elif tipo == 'telefone':
        valor = valor.replace("(","")
        valor = valor.replace(")","")
        valor = valor.replace("-","")
        valor = valor.replace(" ","")
        cliente = Cliente.get_or_none(Cliente.celular1 == valor)
    else:
        return "Tipo inválido. Use 'cpf' ou 'telefone'", 400

    if not cliente:
        return "Cliente não encontrado", 404

    return render_template('detalhe_cliente.html', cliente=cliente)

@cliente_route.route('/<int:cliente_id>/edit')
def form_edit_cliente(cliente_id):
    """ formulario para editar um cliente """
    cliente = Cliente.get_by_id(cliente_id)
    return render_template('form_cliente.html', cliente=cliente)

@cliente_route.route('/<int:cliente_id>/update', methods=['PUT'])
def atualizar_cliente(cliente_id):
    """ atualizar informacoes do cliente """
    # obter dados do formulario de edicao
    data = request.json
    
    cliente_editado = Cliente.get_by_id(cliente_id)
    cliente_editado.nome = data['nome']
    cliente_editado.email = data['email']
    cliente_editado.save()
            
    # editar usuario
    return render_template('item_cliente.html', cliente=cliente_editado)
    

@cliente_route.route('/<int:cliente_id>/delete', methods=['DELETE'])
def deletar_cliente(cliente_id):   
    cliente = Cliente.get_by_id(cliente_id)
    cliente.delete_instance()
    return {'deleted': 'ok'}