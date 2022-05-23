import pandas as pd

df = pd.read_csv("Reviews2.csv", index_col=0)
# 쓸모없는 단어들 제외 시키기
list = ["쪽지", "판매", "팔아", "사요", "카톡", "가격", "ㅋㅋㅋㅋㅋ", "신규", "팝니", "삽니", "연락", "추천", "어때", "억", "1빠", "하한", "상한", "실력", "볼타", "재료", "VS", "vs", "비교", "실분", "ㅇㅈ", "https", "넥필", "넥스트", "떡상", "전재산" ,"영끌", "매물", "임대", "보유", "일베", "잼민", "초딩", "성격", "듣보잡", "사주", "영상", "장사", "구매", "인벤", "둘다"]
word = '|'.join(list)
df = df[(df["reviews"].str.contains(word) == False) & (df["reviews"].str.contains(r'[?&]') == False) & (df["reviews"].str.contains(r'[▇&]')==False)]  
# rate는 쓸모없는 지표라고 생각하고 지우기
df = df.drop(["rate"],axis =1)
df.reset_index(drop=True, inplace=True)
df.to_csv("Reviews2.csv")

# df = pd.read_csv("ICON_Reviews.csv", index_col=0)
# pd.set_option('mode.chained_assignment',  None)
# for i in range(len(df)):
#     print(i,"번째",df.iloc[i][0],":",df.iloc[i][3])
#     a = int(input("label = " ) or -1)
#     df.loc[i,"label"] = a
#     # 클래스 별로 나눔
#     df.to_csv("ICON_Reviews.csv")