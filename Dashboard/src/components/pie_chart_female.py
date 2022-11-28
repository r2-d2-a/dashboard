import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html
from dash.dependencies import Input, Output
from src.components import ids


def  render(app:Dash, data: pd.DataFrame) -> html.Div:
    @app.callback(
      Output(ids.PIE_CHART_FEMALE, "children"), 
      Input(ids.YEAR_DROPDOWN, "value"), 
      Input(ids.CAUSE_DROPDOWN, "value"),
      Input(ids.AGE_DROPDOWN, "value")
    )
    def update_pie_chart(year: int, cause:  list, age: str) -> html.Div:
        pie_data = data[(data['Year'] == year) & (data['Cause'].isin(cause)) &(data['Sex'] == 'FMLE')& (data['Age Group.2'] == age)] 
        fig = px.pie(pie_data,values = 'Death rate per 100 000 population', names='Cause')
        return html.Div(dcc.Graph(figure = fig), id = ids.PIE_CHART_FEMALE )

    return html.Div( id = ids.PIE_CHART_FEMALE )