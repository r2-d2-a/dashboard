import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html, dash_table
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
from . import ids



def  render(app:Dash, data: pd.DataFrame) -> html.Div:
    @app.callback(
      Output(ids.DATA_TABLE, "children"), 
      Input(ids.YEAR_DROPDOWN, "value"), 
      Input(ids.CAUSE_DROPDOWN, "value"),
      Input(ids.GENDER_DROPDOWN, "value"),
      Input(ids.AGE_DROPDOWN, "value")
    )
    def update_data_table(year: int, cause: list, gender: list, age: str) -> html.Div:
        table_data = data[(data['Year'] == year) & (data['Cause'].isin(list(cause))) & (data['Sex'].isin(gender)) & (data['Age Group.2'] == age)]
        table_data = table_data.drop(columns= ['Code', 'ISO3'])
        table_data = table_data.rename(columns = {'Death rate per 100 000 population':'Death rate', 'DALY rate per 100 000 population':'DALY rate'})
        table = dash_table.DataTable(table_data.to_dict('records'))
        return html.Div(table, id = ids.DATA_TABLE)

    return html.Div(id = ids.DATA_TABLE)