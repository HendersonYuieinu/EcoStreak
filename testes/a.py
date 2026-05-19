import torch

print(torch.__version__)
print("gpu configurada: ", torch.cuda.is_available())
print("total de gpus: ", torch.cuda.device_count())

if torch.cuda.is_available():
    print("gpu atual: ", torch.cuda.current_device())
    print("device: ", torch.cuda.device(0))
    print("device name ", torch.cuda.get_device_name(0))
    
else:
    print("nenhuma gpu configurada.")