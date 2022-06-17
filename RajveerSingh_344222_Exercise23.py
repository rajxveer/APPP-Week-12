import dash
import dash_core_components as dcc
import dash_html_components as html
# import plotly.express as px
import pandas as pd

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

df = pd.read_csv("C:\\Users\\User\\Downloads\\USA_Housing.csv")

address = df['Address'].unique()
options = [{'label': a, 'value': a} for a in address]

app.layout = html.Div([
    html.H3(children='Choose or search for an address from the single-choice OR multiple-choice dropdown below'),
    html.Label('Dropdown'),
    dcc.Dropdown(
        options=options,
        value='208 Michael Ferry Apt. 674 Laurabury, NE 37010-5101'
    ),
    
    html.Br(),
    html.Label('Multi-Select Dropdown'),
    dcc.Dropdown(
        options=options,
        value=['208 Michael Ferry Apt. 674 Laurabury, NE 37010-5101', '188 Johnson Views Suite 079 Lake Kathleen, CA 48958'],
        multi=True
    ),
    ], 
    style={'columnCount': 1})

if __name__ == '__main__':
    app.run_server(debug=False)
    