document.addEventListener("DOMContentLoaded", () => {
    const dadosSalvos = localStorage.getItem("resultadoIA");
    
    if (!dadosSalvos) {
        window.location.href = "index.html"; // Redireciona se não houver dados
        return;
    }

    const data = JSON.parse(dadosSalvos);

    document.getElementById("objeto-nome").innerText = data.objeto || "Desconhecido";
    document.getElementById("dica-texto").innerText = data.dica || "Descarte conscientemente.";
    
    if (data.imagem_base64) {
        document.getElementById("img-resultado").src = `data:image/jpeg;base64,${data.imagem_base64}`;
    }

    // Configura a cor da tag da lixeira
    const tagLixeira = document.getElementById("lixeira-tag");
    const lixeira = data.lixeira || "Nenhuma";
    tagLixeira.innerText = `Lixeira ${lixeira}`;

    if (lixeira.includes("Vermelha")) tagLixeira.style.backgroundColor = "#d32f2f";
    else if (lixeira.includes("Verde")) tagLixeira.style.backgroundColor = "#388e3c";
    else if (lixeira.includes("Azul")) tagLixeira.style.backgroundColor = "#1976d2";
    else if (lixeira.includes("Marrom")) tagLixeira.style.backgroundColor = "#5d4037";
    else if (lixeira.includes("Amarela")) tagLixeira.style.backgroundColor = "#fbc02d";
    else tagLixeira.style.backgroundColor = "#757575";

    // Limpa o localStorage para a próxima foto
    localStorage.removeItem("resultadoIA");
});