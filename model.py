from konlpy.tag import Okt
import nltk
import numpy as np
import pandas as pd
import json
import pickle
import numpy as np
import keras

def tokenize(doc):
    # norm은 정규화, stem은 근어로 표시하기를 나타냄
    return ['/'.join(t) for t in okt.pos(doc, norm=True, stem=True)]

def predict_pos_neg(df, review):
    token = tokenize(review)
    tf = term_frequency(token)
    data = np.expand_dims(np.asarray(tf).astype('float32'), axis=0)
    score = model.predict(data)
    index = np.argmax(score, axis=1)[0]

def term_frequency(doc):
    return [doc.count(word) for word in selected_words]

def predict_pos_neg(df,i, review):
    token = tokenize(review)
    tf = term_frequency(token)
    data = np.expand_dims(np.asarray(tf).astype('float32'), axis=0)
    score = model.predict(data)
    index = np.argmax(score, axis=1)[0]

    if index == 0:
        df.iloc[:, 3][i] = 0
    elif index == 1:
        df.iloc[:, 3][i] = 1
    else:
        df.iloc[:, 3][i] = 2

with open('train_docs.json') as f:
    train_docs = json.load(f)
with open('test_docs.json') as f:
    test_docs = json.load(f)
model = keras.models.load_model('suggestion_model.h5')

okt = Okt()
tokens = [t for d in train_docs for t in d[0]]
text = nltk.Text(tokens, name='NMSC')
selected_words = [f[0] for f in text.vocab().most_common(10000)]

df = pd.read_csv("Reviews.csv", index_col=0)
pd.set_option('mode.chained_assignment',  None)

for i in range(115472, 128630):
    predict_pos_neg(df, i , df.iloc[:,2][i])
    print(i,"번째 완료")
    df.to_csv("Modeling_Reviews.csv")
print("최종 완료")

# df = pd.read_csv("Modeling_Reviews.csv")
# df = df.loc[df["label"] != 2]
# df.reset_index(drop=True, inplace=True)
# season =  pd.read_csv("Season.csv", index_col=0)
# suggestion = df.groupby(["name","class_id"], as_index=False)["label"].mean().round(2)
# suggestion["evalution"] = 0
# suggestion = suggestion.fillna(-1)
# pd.set_option('mode.chained_assignment',  None) # 오류 제거
# for i in range(len(season)):
#     suggestion.loc[suggestion["class_id"] == season.iloc[:,0][i], "class_name"] = season.iloc[:,1][i]

# for i in range(len(suggestion)):
#     if suggestion.iloc[:,2][i] == -1:
#         suggestion.iloc[:,3][i] = 4
#     elif suggestion.iloc[:,2][i] >= 0.9:
#         suggestion.iloc[:,3][i] = 3     # 강력추천
#     elif suggestion.iloc[:,2][i] >= 0.7:
#         suggestion.iloc[:,3][i] = 2     # 추천
#     elif suggestion.iloc[:,2][i] >= 0.5:
#         suggestion.iloc[:,3][i] = 1     # 그럭저럭
#     else:    
#         suggestion.iloc[:,3][i] = 0     # 추천하지 않음
# suggestion.to_csv("Suggestion.csv")