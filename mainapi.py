from flask import Flask, render_template

app=Flask("__name__")


@app.route('/')
def home():
    return render_template("myapi.html")
@app.route("/api/v1/<station>/<date>/")

def hi(station, date):
#   data= pd.read_csv()
#   temperature= data.station(data)
    tempertature = 23
    return {"station":station,
            "date":date,
            "temperature":tempertature}

if __name__ == "__main__":
    app.run(debug=True)