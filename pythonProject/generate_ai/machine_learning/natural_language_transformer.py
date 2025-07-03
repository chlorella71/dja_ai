import torch
import pickle
import pandas as pd
import numpy as np
import evaluate
from datasets import load_dataset
from torch.ao.quantization.pt2e.representation import reference_representation_rewrite
from transformers import (
    AutoTokenizer,
    AutoModelForSequenceClassification,
    Trainer,
    TrainingArguments
)

# data = load_dataset('nsmc', trust_remote_code=True)
# with open("data/datasets.pkl", 'wb') as f:
#     pickle.dump(data, f)
# exit()

device = torch.device("cuda" if torch.cuda.is_available() else "cpu") # gpu, cpu 선택사용
print(f"현재 디바이스: {device}")

# model_name="klue/roberta-large"
# model_name="klue/roberta-base"
# model_name = "beomi/kcbert-large"
model_name = "beomi/kcbert-base" # 한국어에 특화된것
tokenizer = AutoTokenizer.from_pretrained(model_name)

def tokenizer_function(example):
    # tokenizer = AutoTokenizer.from_pretrained(model_name)
    return tokenizer(example["document"], padding="max_length", truncation=True)

def compute_metrics(eval_pred):
    accuracy_metric = evaluate.load("accuracy")
    predictions, labels = eval_pred
    predictions = np.argmax(predictions, axis=1)
    return accuracy_metric.compute(predictions=predictions, references=labels)

if __name__ == "__main__":
    # pass
    data = load_dataset('nsmc', trust_remote_code=True)
    # print(data) # 로딩이 오래 걸리면 pkl로 저장해두면 됨, data는 list나 object로 날라올 것
    # print(data["train"])
    with open("../data/datasets.pkl", 'rb') as f:
        data = pickle.load(f)
    train_data = data["train"].shuffle(seed=42).select(range(10000))
    # train_data = data["train"].shuffle(seed=42).select(range(300))
    # print(train_data)
    # df = train_data.to_pandas()
    # print(df.head())
    train_df = pd.DataFrame(train_data)
    # print(train_df.head())
    # test_data = data["test"].shuffle(seed=42).select(range(500))
    test_data = data["test"].shuffle(seed=42).select(range(100))


    tokenized_train_data = train_data.map(tokenizer_function, batched=True)
    tokenized_test_data = test_data.map(tokenizer_function, batched=True)
    tokenized_test_df = pd.DataFrame(tokenized_test_data)
    # print(tokenized_test_df)

    #사전 학습 모델 불러오기
    model = AutoModelForSequenceClassification.from_pretrained(model_name, num_labels=2)
    model.to(device) #
    # accuracy_metric = evaluate.load("accuracy")

    # 학습 설정
    n_epoch=3
    # n_epoch=1
    training_args=TrainingArguments(
        # output_dir = "./results"
        output_dir ="../results", # javascript는 .을 붙여야하지만 python은 sibling은 바로 읽을 수 있음
        num_train_epochs =n_epoch,
        per_device_train_batch_size=16,
        # per_device_train_batch_size=8,
        per_device_eval_batch_size=64,
        # per_device_eval_batch_size=16,
        warmup_steps=500,
        weight_decay=0.01,
        logging_dir="../logs",
        logging_steps=10,
        eval_strategy="epoch",
        save_strategy="epoch",
        load_best_model_at_end=True,
    )

    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=tokenized_train_data,
        eval_dataset=tokenized_test_data,
        compute_metrics=compute_metrics,
    )

    #모델 학습
    trainer.train()

    save_directory = "./save_model" #계싼식 저장하는 디렉토리, 이것만 있으면 예측을 할 수 있음(머신이 저장됨)?
    trainer.save_model(save_directory)
    tokenizer.save_pretrained(save_directory)