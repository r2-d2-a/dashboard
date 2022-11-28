import pandas as pd
from dash import Dash, html, dcc
from src.components import ids
from .data import loader
def render(app: Dash, data: pd.DataFrame) -> html.Div:
    all_age = sorted(list(set(data['Age Group.2'].tolist())))

    return html.Div(
        children = [
            html.H6("Age"),
            dcc.Dropdown(
                id = ids.AGE_DROPDOWN,
                options = [{"label":age, "value": age} for age in all_age],
                multi = False,
                style = {'width': '150px'}
                
            )
        ]
    )