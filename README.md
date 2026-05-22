Siga os passos abaixo para configurar o ambiente e iniciar o treinamento do modelo.

## 1. Instalando as Dependências
Antes de qualquer coisa, você precisa instalar a biblioteca base para a Inteligência Artificial funcionar. Abra o seu terminal e execute o comando:

```bash
pip install ultralytics
```
Dica para usar a placa de vídeo (RTX 3050): Para o treinamento ser mais rápido e usar a GPU, instale também o PyTorch com suporte a CUDA:

```Bash
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
```

### 2. Preparando o Banco de Imagens
Você vai receber um arquivo .zip contendo as fotos que a IA vai usar para estudar.

Extraia o arquivo .zip.

Pegue as pastas train, valid e test.

Mova essas três pastas para dentro da pasta dados_ia do nosso projeto.

A estrutura deve ficar assim:

```Plaintext
dados_ia/
 ├── train/
 ├── valid/
 ├── test/
 ├── data.yaml
 └── TrainYOLO.py
```
### 3. Iniciando o Treinamento
Com a biblioteca instalada e as pastas no lugar certo, basta rodar o script principal.

Abra o terminal na pasta onde está o arquivo e execute:

```Bash
python TrainYOLO.py
```
Pronto! Agora é só esperar o treinamento terminar. A IA fará o resto do trabalho.

⚠️ Nota (Se o treino travar no 0%):
Se o processo congelar na hora de começar, abra o código TrainYOLO.py e adicione workers=0 dentro da função model.train(). Isso resolve o problema
