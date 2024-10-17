# main.py

from train import main as train_main
from evaluate import main as evaluate_main

def main():
    print("开始训练模型...")
    train_main()
    print("开始评估模型...")
    evaluate_main()

if __name__ == "__main__":
    main()
