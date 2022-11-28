import pandas as pd
from dash import Dash, html, dcc
from src.components import ids
from .data import loader
def render(app: Dash, data: pd.DataFrame) -> html.Div:
    all_years = sorted(list(set(data['Year'].tolist())))

    return html.Div(
        children = [
            html.H6("Years"),
            dcc.Dropdown(
                id = ids.YEAR_DROPDOWN,
                options = [{"label":year, "value": year} for year in all_years],
                multi = False,
                style = {'width': '150px'}
            )
        ]
    )
