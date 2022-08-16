from flask import Flask, render_template, request
import requests
import pandas as pd
import pymysql

conn = pymysql.connect(
                        user    = 'FIFA',
                        passwd  = 'FIFA!',
                        host    = "3.83.154.197",
                        port    = 3306,
                        db      = 'FIFA',
                        charset = 'utf8'
        )


app = Flask(__name__)

@app.route('/')
def index():
    
    return render_template('index.html'), 200

@app.route('/player', methods=['GET',"POST"])
def user():

    text = request.form.get('text')
    res = requests.post('http://127.0.0.1:5001/result', data=text.encode('utf-8')) # 포트 포워딩 필요
    value = res.text
    value = value.split(",")
    return render_template('player.html',text=text, value=float(value[1]) * 100, idx=value[0]), 200


if __name__ == "__main__":
    app.run('0.0.0.0', port=5000, debug=True)