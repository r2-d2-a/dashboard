from dash import Dash, html, dcc
import pandas as pd
from . import pie_chart_male
from . import pie_chart_female

def render(app: Dash, data: pd.DataFrame) -> html.Div:
    return html.Div([dcc.Tabs
                        (
                         style = {'width': '450px'},    
                         children = [
                            dcc.Tab(label = 'Male', children = [pie_chart_male.render(app, data)]),
                            dcc.Tab(label = 'Famale', children = [pie_chart_female.render(app, data)])
                            ]
                       
                        )
                        ]
                   )
