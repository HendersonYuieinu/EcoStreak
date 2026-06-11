from ultralytics import YOLO
import os

def treinar_modelo():
    print("Iniciando treinamento de dentro da pasta dados_ia...")
    
    model = YOLO("yolov8n.pt") # Ele vai baixar o yolov8n.pt dentro da pasta dados_ia
    
    model.train(
        data='dados_ia/data.yaml',               # Como o yaml está na mesma pasta que este script, basta o nome direto!
        project="../resultados2_ia",     # O "../" faz o YOLO voltar uma pasta e salvar na raiz do projeto
        name="IDtrash_modelo",
        epochs=50,
        device="cpu",
        #device=0,
        batch=4,
        #batch=16,
        workers=2,
        cache=False,
        plots=True
    )

if __name__ == "__main__":
    os.environ["OMP_NUM_THREADS"] = "4"
    os.environ["MKL_NUM_THREADS"] = "4"
    treinar_modelo() 