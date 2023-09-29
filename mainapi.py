from flask import Flask, render_template

app=Flask("__name__")


@app.route('/')
def home():
    return render_template("myapi.html")
@app.route("/api/v1/<station>/<date>/")

def hi(station, date):
    id="TG_STAID"
    filepath= "dataset/"+id+ str(station).zfill(6) + ".txt"
    import pandas as pd
    import numpy as np

    df= pd.read_csv(filepath, skiprows=20, parse_dates=['    DATE'])
    df['TG'] = df['   TG'].mask(df['   TG'] == -9999, np.nan)
    temperature = df.loc[df['    DATE']== date]['TG'].squeeze()/10

    apidata = {"station": station, "date": date, "temperature": temperature}

    return apidata

if __name__ == "__main__":
    app.run(debug=True)