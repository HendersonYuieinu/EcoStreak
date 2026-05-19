from ultralytics import YOLO

def treinar_modelo():
    print("Iniciando treinamento de dentro da pasta dados_ia...")
    
    model = YOLO("yolov8n.pt") # Ele vai baixar o yolov8n.pt dentro da pasta dados_ia
    
    model.train(
        data='dados_ia/data.yaml',               # Como o yaml está na mesma pasta que este script, basta o nome direto!
        project="../resultados_ia",     # O "../" faz o YOLO voltar uma pasta e salvar na raiz do projeto
        name="IDtrash_modelo",
        epochs=30,
        device="cpu",
        batch=8
    )

if __name__ == "__main__":
    treinar_modelo() 