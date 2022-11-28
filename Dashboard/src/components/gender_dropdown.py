import pandas as pd
from dash import Dash, html, dcc
from src.components import ids
from .data import loader

def render(app: Dash, data: pd.DataFrame) -> html.Div:
    all_gender = sorted(list(set(data['Sex'].tolist())))

    return html.Div(
        children = [
            html.H6("Gender"),
            dcc.Dropdown(
                id = ids.GENDER_DROPDOWN,
                options = [{"label":gender, "value": gender } for gender in all_gender],
                multi = True,
                style = {'width': '200px'}
            )
        ]
    )