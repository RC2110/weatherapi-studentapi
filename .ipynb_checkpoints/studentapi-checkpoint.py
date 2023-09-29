from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("task.html")

@app.route('/api/hb1/<checkword>/')
def capital(checkword):
    return {'word': checkword,
            'nword':checkword.upper()
            }

if __name__ == "__main__":
    app.run(debug=True, port= 5001)

