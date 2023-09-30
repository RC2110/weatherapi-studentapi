from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("task.html")

@app.route('/api/hb1/<checkword>/')
def meaning(checkword):
    import pandas as pd
    df = pd.read_csv("dataset/dictionary.csv")

    if df.loc[df['word'] == checkword].empty:
        checkword = checkword.title()
        if df.loc[df['word'] == checkword].empty:
            checkword = checkword.lower()

    mean1 = df.loc[df['word'] == checkword]['definition'].squeeze()

    return {'word': checkword,
            'nword':mean1
            }

if __name__ == "__main__":
    app.run(debug=True, port= 5001)

