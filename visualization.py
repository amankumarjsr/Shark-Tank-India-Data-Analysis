import pandas as pd
import numpy as np
from plotly import graph_objs as go
import json
import plotly
import plotly.express as px
from data_collecter import data_func

df = pd.read_csv("Shark Tank Data.csv")
data_list = [
    df["ashneer_deal"],
    df["anupam_deal"],
    df["aman_deal"],
    df["namita_deal"],
    df["vineeta_deal"],
    df["peyush_deal"],
    df["ghazal_deal"],
]


class Graphs:
    def fig1(self):
        func = data_func()
        output = func.each_episode_deal(df["episode_number"], df["deal_amount"])
        episode_list = []
        i = 1
        for item in range(35):
            episode_list.append("episode " + str(i))
            i += 1
        fig = px.bar(y=output, x=episode_list, color=output)
        graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
        return graphJSON

    def fig2(self):
        func = data_func()
        output = func.total_investment(data_list, df["amount_per_shark"])
        labels = ["Ashneer", "Anupam", "Aman", "Namita", "Vineeta", "Peyush", "Ghazal"]
        # Use `hole` to create a donut-like pie chart
        fig = px.pie(df, values=output, names=labels, hole=0.3)
        graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
        return graphJSON

    def fig3(self):
        sectors = list(df.sector.unique())
        df[df["sector"] == sectors[1]]
        fig = px.histogram(
            df,
            y="deal_amount",
            x="sector",
            color="sector",
        )
        graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
        return graphJSON

    def fig4(self):
        fig = px.bar(
            df[df["deal"] == 1], x="brand_name", y="ask_equity", color="deal_equity"
        )
        graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
        return graphJSON

    def fig5(self):
        fig = px.bar(
            df[df["deal"] == 1],
            x="brand_name",
            y="ask_valuation",
            color="deal_valuation",
        )
        graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
        return graphJSON

    def fig6(self):
        data_list = [
            df["ashneer_deal"],
            df["anupam_deal"],
            df["aman_deal"],
            df["namita_deal"],
            df["vineeta_deal"],
            df["peyush_deal"],
            df["ghazal_deal"],
        ]
        output = []
        labels = ["Ashneer", "Anupam", "Aman", "Namita", "Vineeta", "Peyush", "Ghazal"]

        for item in data_list:
            temp = []
            for data in df["equity_per_shark"][item == 1]:
                temp.append(data)
            output.append(round(sum(temp), 2))

        fig = px.pie(values=output, names=labels)
        graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
        return graphJSON

    def fig7(self):
        labels = [
            "ashneer_deal",
            "anupam_deal",
            "aman_deal",
            "namita_deal",
            "vineeta_deal",
            "peyush_deal",
            "ghazal_deal",
        ]
        fig = px.bar(df[df["deal"] == 1], x="brand_name", y=labels)
        graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
        return graphJSON

    def fig8(self):
        output1 = len(df["deal"][df["deal"] == 1])
        output0 = len(df["deal"][df["deal"] == 0])
        labels = ["Got Deal", "Not Got Deal"]
        values = [output1, output0]
        fig = px.pie(values=values, names=labels)
        graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
        return graphJSON

    def fig9(self):
        output = []
        data_list = [
            df["ashneer_deal"],
            df["anupam_deal"],
            df["aman_deal"],
            df["namita_deal"],
            df["vineeta_deal"],
            df["peyush_deal"],
            df["ghazal_deal"],
        ]
        for item in data_list:
            output.append(len(df[item == 1]))
        labels = ["Ashneer", "Anupam", "Aman", "Namita", "Vineeta", "Peyush", "Ghazal"]
        fig = px.bar(x=labels, y=output, color=output)
        graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
        return graphJSON


# df = pd.read_csv("Shark Tank India Dataset.csv")

# y = [494.33, 533.83, 887.49, 648.33, 328.33, 719.66, 130.0]
# x = ["ashneer", "anupam", "aman", "namita", "vineeta", "peyush", "ghazal"]
