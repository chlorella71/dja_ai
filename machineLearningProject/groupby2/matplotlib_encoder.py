import matplotlib.pyplot as plt

def hangul_encoding():
    try:
        plt.rc('font', family='Malgun Gothic') # Windows 기본 폰트
        print("Malgun Gothic 폰트 설정 완료.")
    except:
        try:
            plt.rc('font', family='NanumGothic') # 나눔고딕 (설치 필요)
            print("NanumGothic 폰트 설정 완료.")
        except:
            print("경고: Malgun Gothic 또는 NanumGothic 폰트를 찾을 수 없습니다. 다른 한글 폰트를 시도하거나 설치해주세요.")