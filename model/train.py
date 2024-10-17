# train.py

from model.gera_model import GeraModel, train_model
from model.data_loader import load_data, preprocess_data

def main():
    data = load_data()
    processed_data = preprocess_data(data)
    model = GeraModel()
    trained_model = train_model(model, processed_data)
    print("模型训练完成。")

if __name__ == "__main__":
    main()
