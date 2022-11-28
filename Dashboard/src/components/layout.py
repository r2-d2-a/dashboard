import pandas as pd
from dash import Dash, html
from src.components import year_dropdown
from src.components import gender_dropdown
from src.components import cause_dropdown
from src.components import bar_chart

def create_layout(app: Dash, data: pd.DataFrame) ->html.Div:
    return html.Div(className = "app-div", 
                    children = [html.H1(app.title),
                                html.Div(className = "dropdown",
                                        children = [year_dropdown.render(app,data), 
                                                    gender_dropdown.render(app,data), 
                                                    cause_dropdown.render(app,data)],
                                        style = {'display': 'flex', 'flex-direction': 'row'}
                                ),
                                bar_chart.render(app,data),],)