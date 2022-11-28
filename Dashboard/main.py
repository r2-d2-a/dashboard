import pandas as pd
from dash import Dash, html
from dash_bootstrap_components.themes import BOOTSTRAP
from src.components.layout import create_layout
from src.components.data.loader import loadData

PATH = "./data/data.csv"
def main() -> None:
    data = loadData(PATH)
    app = Dash(external_stylesheets = [BOOTSTRAP])
    app.title = "Dashboard"
    app.layout = create_layout(app,data)
    app.run()

if __name__ == "__main__":
    main()