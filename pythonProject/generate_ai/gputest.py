import torch

if __name__=="__main__":
    print("PyTorch 버전:", torch.__version__)
    print("CUDA 지원 버전:", torch.version.cuda)
    print("GPU 사용 가능 여부:", torch.cuda.is_available())
    if torch.cuda.is_available():
        print("GPU 이름:", torch.cuda.get_device_name(0))