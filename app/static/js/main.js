
  document.addEventListener('DOMContentLoaded', () => {
    const tipoLinks = document.querySelectorAll('.tipo-busca');
    const input = document.getElementById('input-busca');
    const tipoInputHidden = document.getElementById('tipo-escolhido');
    const btnTipoBusca = document.getElementById('btn-tipo-busca');

    let tipoAtual = 'cpf';
 
    const mascaras = {
      cpf: (v) => {
        return v
          .replace(/\D/g, '')
          .slice(0, 11)
          .replace(/(\d{3})(\d)/, '$1.$2')
          .replace(/(\d{3})(\d)/, '$1.$2')
          .replace(/(\d{3})(\d{1,2})$/, '$1-$2');
      },
      telefone: (v) => {
        return v
          .replace(/\D/g, '')
          .slice(0, 11)
          .replace(/(\d{2})(\d)/, '($1) $2')
          .replace(/(\d{5})(\d)/, '$1-$2')
          .replace(/(-\d{4})\d+?$/, '$1');
      }
    };

    // Aplica a máscara enquanto digita
    input.addEventListener('input', () => {
      input.value = mascaras[tipoAtual](input.value);
    });

    // Configurações iniciais para CPF (caso padrão)
    tipoInputHidden.value = tipoAtual;
    input.placeholder = 'Digite o CPF';
    input.pattern = '\\d{3}\\.\\d{3}\\.\\d{3}-\\d{2}|\\d{11}';
    input.title = 'Digite um CPF válido (ex: 123.456.789-00)';
    btnTipoBusca.textContent = 'CPF';

    // Altera tipo ao clicar no dropdown
    tipoLinks.forEach(link => {
      link.addEventListener('click', (e) => {
        e.preventDefault();
        const tipo = e.target.getAttribute('data-tipo');
        tipoAtual = tipo;

        tipoInputHidden.value = tipo;
        btnTipoBusca.textContent = tipo === 'cpf' ? 'CPF' : 'Telefone';

        if (tipo === 'cpf') {
          input.placeholder = 'Digite o CPF';
          input.pattern = '\\d{3}\\.\\d{3}\\.\\d{3}-\\d{2}|\\d{11}';
          input.title = 'Digite um CPF válido (ex: 123.456.789-00 ou 12345678900)';
        } else {
          input.placeholder = 'Digite o telefone';
          input.pattern = '\\(?\\d{2}\\)?\\s?\\d{4,5}-?\\d{4}|\\d{10,11}';
          input.title = 'Digite um telefone válido (ex: (11) 91234-5678)';
        }

        input.value = ''; // limpa o campo ao trocar tipo
      });
    });

  




  });

  document.addEventListener('DOMContentLoaded', () => {

    const cpfElement = document.getElementById("cpfText");
    const alertCpf = document.getElementById("alertCpf");
  
    if (cpfElement && alertCpf) {
      cpfElement.addEventListener("click", function (event) {
        event.preventDefault(); 
  
        const textToCopy = cpfElement.textContent.trim();
  
        navigator.clipboard.writeText(textToCopy).then(() => {
          // Mostra o alerta Bootstrap
          alertCpf.classList.remove('d-none');
          alertCpf.classList.add('show');
  
          // Oculta após 2 segundos
          setTimeout(() => {
            alertCpf.classList.remove('show');
            alertCpf.classList.add('d-none');
          }, 2000);
        }).catch(err => {
          console.error("Erro ao copiar: ", err);
        });
      });
    }
  });
  