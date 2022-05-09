from multiprocessing import shared_memory
import pandas as pd
from flask import Flask, render_template, request, send_file
from visualization import Graphs

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():
    graphs = Graphs()
    fig1 = graphs.fig1()
    fig2 = graphs.fig2()
    fig3 = graphs.fig3()
    fig4 = graphs.fig4()
    fig5 = graphs.fig5()
    fig6 = graphs.fig6()
    fig7 = graphs.fig7()
    fig8 = graphs.fig8()
    fig9 = graphs.fig9()

    return render_template(
        "index.html",
        plot1=fig1,
        plot2=fig2,
        plot3=fig3,
        plot4=fig4,
        plot5=fig5,
        plot6=fig6,
        plot7=fig7,
        plot8=fig8,
        plot9=fig9,
    )


@app.route("/contactus", methods=["GET"])
def Contact():
    return render_template("contactus.html")


@app.route("/team", methods=["GET"])
def team():
    return render_template("team.html")


@app.route("/data", methods=["GET", "POST"])
def data():
    df = pd.read_csv("Shark Tank Data.csv")
    df1 = df[
        [
            "brand_name",
            "idea",
            "sector",
            "pitcher_ask_amount",
            "ask_equity",
            "ask_valuation",
            "deal_amount",
            "deal_equity",
            "deal_valuation",
        ]
    ]
    headings = df1.columns
    data = []
    for i in range(len(df1)):
        data.append(list(df1.iloc[i].values))
    return render_template("results.html", headings=headings, data=data)


if __name__ == "__main__":
    app.run(debug=True)
