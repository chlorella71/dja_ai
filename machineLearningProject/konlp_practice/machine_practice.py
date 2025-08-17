# /data/Student_performance_data.csv에서
# GradeClass를 label(정답값)으로 한 machine 만들어보기
import pandas as pd
import os
import numpy as np
import matplotlib.pyplot as plt
import joblib
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix, f1_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.impute import SimpleImputer

DATA_PATH = 'data/Student_performance_data.csv'
OUT_DIR = 'data'

def load_data(path):
    df = pd.read_csv(path)
    # target/불필요 컬럼 정의
    target = 'GradeClass'
    drop_cols = [c for c in ['StudentID'] if c in df.columns]
    X = df.drop(columns=[target] + drop_cols)
    y = df[target].astype(int)
    return X, y, df

def build_pipeline(X):
    # 숫자/문자 컬럼 자동 분리
    num_cols = X.select_dtypes(include=[np.number]).columns.tolist()
    cat_cols = [c for c in X.columns if c not in num_cols]

    num_pipe = Pipeline(steps=[
        ('imputer', SimpleImputer(strategy='median')),
        # 트리에 스케일은 필수 아님이지만, 다른 모델로 교체 시 대비
        ('scaler', StandardScaler(with_mean=False))
    ])

    cat_pipe = Pipeline(steps=[
        ('imputer', SimpleImputer(strategy='most_frequent')),
        ('onehot', OneHotEncoder(handle_unknown='ignore'))
    ])

    preproc = ColumnTransformer(
        transformers=[
            ('num', num_pipe, num_cols),
            ('cat', cat_pipe, cat_cols)
        ],
        remainder='drop'
    )

    clf = RandomForestClassifier(
        n_estimators=400,
        random_state=42,
        n_jobs=-1,
        class_weight='balanced', # 불균형 대응
        min_samples_leaf=2
    )

    pipe = Pipeline(steps=[('prep', preproc), ('clf', clf)])
    return pipe

def plot_confusion_matrix(cm, classes, out_path):
    import itertools
    fig, ax = plt.subplots(figsize=(6,5))
    im = ax.imshow(cm, interpolation='nearest')
    ax.set_title("Confusion Matrix (GradeClass)")
    plt.colorbar(im, ax=ax)
    tick_marks = np.arange(len(classes))
    ax.set_xticks(tick_marks)
    ax.set_yticks(tick_marks)
    ax.set_xticklabels(classes)
    ax.set_yticklabels(classes)
    ax.set_xlabel('Predicted')
    ax.set_ylabel('True')
    thresh = cm.max() / 2.0
    for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
        ax.text(j, i, format(cm[i, j], 'd'),
                ha='center',
                color='white' if cm[i, j] > thresh else 'black')
    plt.tight_layout()
    plt.savefig(out_path, dpi=150)
    plt.close()

def export_feature_importances(pipe, out_csv):
    # 전처리 후 피처 이름 얻기 (sklearn >= 1.0)
    try:
        feat_names = pipe.named_steps['prep'].get_feature_names_out()
    except Exception:
        feat_names = [f'feat_{i}' for i in range(len(pipe.named_steps['clf'].feature_importances_))]
    imps = pipe.named_steps['clf'].feature_importances_
    fi = (pd.DataFrame({'feature': feat_names, 'importance': imps})
          .sort_values('importance', ascending=False))
    fi.to_csv(out_csv, index=False)
    return fi

if __name__ == "__main__":
    os.makedirs(OUT_DIR, exist_ok=True)

    # 1) 데이터 로드
    X, y, df_all = load_data(DATA_PATH)
    print("Shape:", df_all.shape)
    print("GradeClass 분포:\n", y.value_counts(normalize=True).sort_index())

    # 2) 파이프라인 구성
    pipe = build_pipeline(X)

    # 3) 학습/검증 분리(층화)
    X_tr, X_te, y_tr, y_te = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    # 4) 학습
    pipe.fit(X_tr, y_tr)

    # 5) 평가
    y_pred = pipe.predict(X_te)
    acc = accuracy_score(y_te, y_pred)
    macro_f1 = f1_score(y_te, y_pred, average='macro')
    print(f'\nAccuracy: {acc:.4f} | Macro-F1: {macro_f1:.4f}')
    print('\nClassification report:\n', classification_report(y_te, y_pred))

    # 6) 혼동행렬 저장
    cm = confusion_matrix(y_te, y_pred, labels=np.sort(y.unique()))
    cm_path = os.path.join(OUT_DIR, 'confusion_matrix_gradeclass.png')
    plot_confusion_matrix(cm, classes=np.sort(y.unique()), out_path=cm_path)
    print("Saved:", cm_path)

    # 7) 피처 중요도 저장
    fi_csv = os.path.join(OUT_DIR, 'feature_importances_gradeclass.csv')
    fi_top = export_feature_importances(pipe, fi_csv)
    print('Saved:', fi_csv)
    print('\nTop 10 중요 피처:\n', fi_top.head(10))

    # 8) 모델 저장
    model_path = os.path.join(OUT_DIR, 'student_grade_model.joblib')
    joblib.dump(pipe, model_path)
    print("Saved model:", model_path)

    # 9) 예측 예시
    X_new = pd.DataFrame([{
        "Age":17, "Gender":1, "Ethnicity":2, "ParentalEducation":3,
        "StudyTimeWeekly":8.0, "Absences":2, "Tutoring":1, "ParentalSupport":4,
        "Extracurricular":1, "Sports":0, "Music":1, "Volunteering":0, "GPA":3.6
    }])
    print("Pred:", int(pipe.predict(X_new)[0]))