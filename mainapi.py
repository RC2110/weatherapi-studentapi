from flask import Flask

app=Flask("myapi")

@app.route("http://127.0.0.1:5000/api/v1/<station>/<date>/")

def hi(station, date):
    data= pd.read_csv()
    temperature= data.station(data)

    return {"station":station,
            "date":date,
            "temperature":temperature}