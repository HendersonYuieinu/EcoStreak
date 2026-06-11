from fastapi import FastAPI, UploadFile, File
from ultralytics import YOLO
import cv2
import numpy as np
import base64
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # Permite que qualquer dispositivo (inclusive seu celular) acesse a API
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

model = YOLO(r"runs\resultados5_ia\IDtrash_modelo-2\weights\best.pt")
#model = YOLO("resultados_ia/weights/best.pt")

@app.post("/predict")
async def predict_trash(file: UploadFile = File(...)):
    contents = await file.read()
    nparr = np.frombuffer(contents, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    
    results = model(img)
    
    label_ingles = "none"
    lixeira = "Nenhuma"
    dica = "Tente tirar a foto de mais perto."
    cor_bgr = (255, 255, 255)
    
    for r in results:
        for box in r.boxes:
            # if float(box.conf[0]) > 0.5:
                x1, y1, x2, y2 = map(int, box.xyxy[0])
                class_id = int(box.cls[0])
                label_ingles = model.names[class_id]
                
                if label_ingles == "plastic":
                    texto_imagem, cor_bgr = "Plastico", (0, 0, 255)
                    lixeira, dica = "Lixeira Vermelha (Plastico)", "Plásticos demoram até 4000 anos para se decompor! Descarte em lixeiras vermelhas. Lave as embalagens antes. Evite plásticos de uso único. Reciclar plástico economiza até 80% da energia necessária para produzi-lo do zero!"
                
                elif label_ingles == "glass":
                    texto_imagem, cor_bgr = "Vidro", (0, 255, 0)
                    lixeira, dica = "Lixeira Verde (Vidro)", "O vidro é 100% reciclável e pode ser reaproveitado infinitamente sem perder a qualidade! Descarte em lixeiras verdes. Lave as embalagens antes de descartar. Se houver vidro quebrado, embrulhe em jornal para proteger os coletores. Reciclar vidro economiza até 30% da energia necessária para fazer um novo!"
                
                elif label_ingles in ["paper"]:
                    texto_imagem, cor_bgr = "Papel", (255, 0, 0)
                    lixeira, dica = "Lixeira Azul (Papel)", "Cada tonelada de papel reciclado salva 17 árvores! Descarte em lixeiras azuis. Não misture papel molhado ou engordurado. Papéis com grampos podem ser reciclados normalmente."
                
                elif label_ingles == "cardboard":
                    texto_imagem, cor_bgr = "Papelão", (255, 0, 0)
                    lixeira, dica = "Lixeira Azul (Papel)", "Papelão é um dos materiais mais reciclados do mundo! Descarte em lixeiras azuis. Desmonte as caixas para economizar espaço. Evite papelão molhado. Uma caixa reciclada pode virar nova caixa em 2 semanas!"
                
                elif label_ingles == "organic":
                    texto_imagem, cor_bgr = "Organico", (42, 42, 165)
                    lixeira, dica = "Lixeira Marrom (Orgânico)", "Restos de comida viram adubo atravás da compostagem! descarte em lixeiras marrons, Cascas, restos de frutas e vegetais são perfeitos. O composto enriuece o solo em produtos químicos."
                
                elif label_ingles == "metal":
                    texto_imagem, cor_bgr = "Metal", (0, 255, 255)
                    lixeira, dica = "Lixeira Amarela (Metal)", "Metais como alumínio e aço são 100% recicláveis infinitamente! Descarte em lixeiras amarelas. Uma lata reciclada volta às prateleiras em 60% dias. Reciclar alumínio gasta 95% menos energia!"
                else:
                    texto_imagem = "Desconhecido."
                
                cv2.rectangle(img, (x1, y1), (x2, y2), cor_bgr, 3)
                cv2.putText(img, texto_imagem, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, cor_bgr, 2)
    _, buffer = cv2.imencode(".jpg", img)
    img_base64 = base64.b64encode(buffer).decode("utf-8")
    
    return {
        "objeto" : label_ingles,
        "lixeira": lixeira,
        "dica": dica,
        "imagem_base64": img_base64
    }                    
                                         
    
