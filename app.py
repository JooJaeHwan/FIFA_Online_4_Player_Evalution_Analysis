from flask import Flask, request
from konlpy.tag import Kkma, Okt
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
import keras
import re
import numpy as np

app1 = Flask(__name__)

@app1.route('/') # 테스트용
def index() :
    return '모델 서버 입니다. 여기로 직접 접근하면 안됩니다.'

@app1.route('/result', methods=['POST','GET']) # http://아이피:포트/api
def api() :
    data = request.get_data()
    value = str(data, 'utf-8')
    value = clean_text(value)
    return sentiment_predict(value)


def clean_text(d):
  pattern = r'[^가-힣a-zA-Z\s]'
  text = re.sub(pattern, '', d)
  text = re.sub("\n", ' ', text)
  text = re.sub("  +", " ", text)
  return text

def sentiment_predict(new_sentence):
    tokenizer = Tokenizer(6631, oov_token='OOV')
    stopword = ['의', '가', '이', '은', '들', '는', '좀', '잘', '걍', '과', '도', '를', '으로', '자', '에', '와', '한', '하다', '에', '은', '는', '하', '새끼', '병신', '좆', '에서']
    new_token = [word for word in Okt().morphs(new_sentence) if word not in stopword]
    tokenizer.fit_on_texts(new_token)
    new_sequences = tokenizer.texts_to_sequences([new_token])
    new_pad = pad_sequences(new_sequences, maxlen=25)
    loaded_model = keras.models.load_model("./BILSTM_best_model.h5")
    answer = loaded_model.predict(new_pad)
    return ",".join([str(answer.argmax()), str(f'{np.max(answer):.4f}')])

if __name__ == '__main__' :
    app1.run('0.0.0.0', port=5001, debug=False) # 포트 포워딩 필요