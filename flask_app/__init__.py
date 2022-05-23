
import os
from flask import Flask, render_template, request
import pickle
import requests
import pandas as pd




app = Flask(__name__)

@app.route('/')
def index():
    
    return render_template('index.html'), 200

@app.route('/player', methods=["POST"])
def user():


    value = request.form["player"]
    player = "%s"%value
    suggestion = pd.read_csv("/Users/jjwani/workspace/codestates/FIFA_Online_4_Player_Evalution_Analysis/Suggestion.csv", index_col=0)
    suggestion = suggestion.loc[suggestion["name"].str.contains(player)]
    name = suggestion.iloc[:,4]
    name = list(name)
    evalution = suggestion.iloc[:,3]
    evalution = list(evalution)
    return render_template('player.html', suggestion=len(suggestion)-1, name=name, player=player, evalution=evalution), 200


if __name__ == "__main__":
    app.run(debug=True)