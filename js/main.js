document.getElementById("cadastroForm").addEventListener("submit", function(e) {
    e.preventDefault(); // Evita envio real do formulário
    document.getElementById("mensagem-sucesso").style.display = "block";
  });
  