import pandas as pd
from dash import Dash, html, dcc
from src.components import ids
from .data import loader

def render(app: Dash, data: pd.DataFrame) -> html.Div:
    all_cause = sorted(list(set(data['Cause'].tolist())))

    return html.Div(
        children = [
            html.H6("Cause"),
            dcc.Dropdown(
                id = ids.CAUSE_DROPDOWN,
                options = [{"label":cause, "value": cause } for cause in all_cause],
                multi = True,
                searchable = True,
                style = {'width': '1000px'} 
            )
        ]
    )