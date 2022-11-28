import pandas as pd
import matplotlib.pyplot as pp
import plotly.express as px
from dash import Dash, dcc, html
from dash.dependencies import Input, Output
from . import ids


def  render(app:Dash, data: pd.DataFrame) -> html.Div:
    @app.callback(
      Output(ids.BAR_CHART, "children"), 
      Input(ids.YEAR_DROPDOWN, "value"), 
      Input(ids.CAUSE_DROPDOWN, "value"),
      Input(ids.GENDER_DROPDOWN, "value")
    )
    def update_bar_chart(year: int, cause: list, gender: list) -> html.Div:
        bar_data = data[(data['Year'] == year) & (data['Cause'].isin(cause)) & (data['Sex'].isin(gender))]
        fig = px.bar(bar_data, x = "Cause", y = "Death rate per 100 000 population", color = "Sex", barmode = "group" )
        return html.Div(dcc.Graph(figure = fig), id = ids.BAR_CHART)

    return html.Div(id = ids.BAR_CHART)

