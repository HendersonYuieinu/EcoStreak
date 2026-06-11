const texto = document.getElementById("texto");
const dots = document.querySelectorAll(".dot");
const btnProx = document.getElementById("btn-prox");

let cont = 0;

// Textos com pequenos ajustes de pontuação
const texts_intro = [
    "Olá! Seja bem-vindo ao EcoStreak.",
    "O sistema é simples: você aponta a câmera para um lixo e eu te digo como descartar!",
    "Cada tipo de resíduo tem um destino certo: plástico, metal, papel, orgânico ou vidro.",
    "Ao descartar nos nossos centros de coleta, você ganha créditos!",
    "Vamos começar a salvar o planeta?"
];

// Inicia com o primeiro texto
texto.textContent = texts_intro[0];

const button_prox = () => {
    if (cont < texts_intro.length - 1) {
        cont++;
        texto.textContent = texts_intro[cont];
        
        // Atualiza a barra de progresso (bolinhas)
        dots.forEach((dot, index) => {
            if (index === cont) {
                dot.classList.add('active');
            } else {
                dot.classList.remove('active');
            }
        });

        // Muda o estilo do botão na última etapa
        if (cont === texts_intro.length - 1) {
            btnProx.textContent = "Começar Agora!";
            btnProx.style.backgroundColor = "#16a34a"; // Verde mais escuro de confirmação
            btnProx.style.transform = "scale(1.05)";
            setTimeout(() => btnProx.style.transform = "scale(1)", 200);
        }
    } else {
        // Agora redireciona para o Menu Principal (Início)
        passar_paraindex();
    }
};

const passar_paraindex = () => {
    window.location.href = 'index.html';
};