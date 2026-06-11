const SERVER_URL = "http://localhost:8000/predict";

let usandoCameraTraseira = true;
let facingmode = "environment"; 

const video = document.getElementById('webcam');
const canvas = document.getElementById('canvas');
const textoStatus = document.getElementById('status');
const textoDica = document.getElementById('dica');
const btnCapturar = document.getElementById('btn-capturar');
let processando = false;

// Configuração ideal para evitar distorção no mobile
const constraintsYOLO = {
    width: { ideal: 640 },
    height: { ideal: 480 }
};

function gerenciarEspelhamentoUI() {
    if (facingmode === "user") {
        video.style.transform = "scaleX(-1)";
    } else {
        video.style.transform = "scaleX(1)";
    }
}

const alternarcamera = () => {
    if (video.srcObject) {
        video.srcObject.getTracks().forEach(track => track.stop());
    }
    usandoCameraTraseira = !usandoCameraTraseira;
    facingmode = usandoCameraTraseira ? "environment" : "user";
    
    gerenciarEspelhamentoUI();
    iniciarCamera();
}

function iniciarCamera() {
    navigator.mediaDevices.getUserMedia({ 
        video: { facingMode: facingmode, ...constraintsYOLO }, 
        audio: false 
    })
    .then(stream => {
        video.srcObject = stream;
        video.play();
    })
    .catch(err => {
        console.error(err);
        textoStatus.innerText = "Erro na Câmera";
    });
}

// Inicializa
gerenciarEspelhamentoUI();
iniciarCamera();

btnCapturar.addEventListener('click', () => {
    if (processando) return; 

    processando = true;
    textoStatus.innerText = "Analisando...";
    textoDica.innerText = "Aguarde a IA identificar o objeto...";

    canvas.width = video.videoWidth;
    canvas.height = video.videoHeight;
    const ctx = canvas.getContext('2d');

    ctx.save();
    if (facingmode === "user") {
        ctx.translate(canvas.width, 0); 
        ctx.scale(-1, 1);
    }
    ctx.drawImage(video, 0, 0, canvas.width, canvas.height);
    ctx.restore(); 
    
    canvas.toBlob((blob) => {
        const formData = new FormData();
        formData.append('file', blob, 'imagem.jpg');

        fetch(SERVER_URL, {
            method: 'POST',
            body: formData
        })
        .then(response => {
            if (!response.ok) throw new Error("Erro no servidor");
            return response.json();
        })
        .then(data => {
            // Salva a resposta da IA temporariamente e envia para a página separada
            localStorage.setItem("resultadoIA", JSON.stringify(data));
            window.location.href = "resultado.html";
        })
        .catch(err => {
            textoStatus.innerText = "Erro!";
            textoDica.innerText = "Não foi possível conectar ao servidor.";
            processando = false;
        });

    }, 'image/jpeg', 0.9);
});

// Captura o input de arquivo
const fileInput = document.getElementById('file-input');

fileInput.addEventListener('change', (event) => {
    const file = event.target.files[0];
    if (!file) return;

    processando = true;
    textoStatus.innerText = "Enviando arquivo...";
    textoDica.innerText = "Aguarde a análise da IA...";

    const formData = new FormData();
    formData.append('file', file);

    fetch(SERVER_URL, {
        method: 'POST',
        body: formData
    })
    .then(response => {
        if (!response.ok) throw new Error("Erro no servidor");
        return response.json();
    })
    .then(data => {
        localStorage.setItem("resultadoIA", JSON.stringify(data));
        window.location.href = "resultado.html";
    })
    .catch(err => {
        console.error(err);
        textoStatus.innerText = "Erro no upload";
        textoDica.innerText = "Tente novamente.";
        processando = false;
    });
});