# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import numpy as np

raw_data = pd.read_csv('../data/actual-data.csv')
plottable_data = {}
plot_months = ['Jan', 'Feb', 'Mar']

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

def get_plottable_data():
    for kiddo in np.unique(raw_data.Name):
        # TODO processing here for spending column
        # TODO processing here for future month predictions, out 6 months
        print('Not really processing data yet for ' + kiddo )

    return plottable_data

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(children=[
    html.H1(children='Financial Graphs For Year 2019'),

    html.Hr(),

    dcc.Dropdown(
        options=[
            {'label': 'Adam', 'value': 'Adam'},
            {'label': 'Daniel', 'value': 'Daniel'},
            {'label': 'Anna', 'value': 'Anna'},
            {'label': 'Peter', 'value': 'Peter'}
        ],
        value=['Adam'],
        id='name-selector',
        multi=False
    ),

    html.Div([
        dcc.Graph(id='bargraph')
    ])
])


@app.callback(
    dash.dependencies.Output(component_id='bargraph', component_property='figure'),
    [dash.dependencies.Input(component_id='name-selector', component_property='value')]
)
def update_output_div(selected_name):
    print('Received name: ' + str(selected_name))
    named_data = raw_data[raw_data.Name==selected_name]
    return {
            'data': [
                {'x': named_data.Month, 'y': named_data.Balance, 'type': 'bar', 'name': 'Adam'}
            ],
            'layout': {
                'title': ''
            }
        }


if __name__ == '__main__':
    data = get_plottable_data()
    app.run_server(debug=True)  # find it on http://127.0.0.1:8050/