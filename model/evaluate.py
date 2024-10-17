# evaluate.py

from model.gera_model import GeraModel, predict
from model.data_loader import load_data, preprocess_data

def main():
    data = load_data()
    processed_data = preprocess_data(data)
    model = GeraModel()  # 假设这是训练过的模型
    predictions = predict(model, processed_data)
    print("模型评估完成，预测结果：", predictions)

if __name__ == "__main__":
    main()
