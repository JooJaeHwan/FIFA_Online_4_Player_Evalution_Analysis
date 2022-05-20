import pandas as pd

# df = pd.read_csv("Reviews.csv", index_col=0)
# # 클래스 아이디 바꿔가며 넣기
# list = ["쪽지", "판매", "팔아", "사요", "카톡", "가격", "ㅋㅋㅋㅋㅋ", "신규", "팝니", "삽니", "연락", "추천", "어때", "억", "1빠", "하한", "상한", "실력", "볼타", "재료"]
# word = '|'.join(list)
# df = df[(df["class_id"] == 101) & (df["reviews"].str.contains(word) == False) & (df["reviews"].str.contains(r'[?&]') == False)]  
   
# df.reset_index(drop=True, inplace=True)
df = pd.read_csv("ICON_Reviews.csv", index_col=0)
pd.set_option('mode.chained_assignment',  None)
for i in range(4674,len(df)):
    print(i,"번째",df.iloc[i][0],":",df.iloc[i][3])
    a = int(input("label = " ) or -1)
    df.loc[i,"label"] = a
    # 클래스 별로 나눔
    df.to_csv("ICON_Reviews.csv")