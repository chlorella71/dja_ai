import pandas as pd

if __name__=="__main__":
    #csv파일 읽기, sep=''는 구분자, csv파일은 ';', '\t' 형식으로 보통 나뉘어 있음
    marketing_campaign_df =pd.read_csv('data/marketing_campaign.csv', sep='\t')
    print(marketing_campaign_df.head())
