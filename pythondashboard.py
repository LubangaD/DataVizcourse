
import pandas as pd

# Sample dataset
df = pd.DataFrame({
    "Category": ["A", "B", "C", "D"],
    "Values": [10, 20, 30, 40]
})

import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px

# Initialize the Dash app
app = dash.Dash(__name__)

# Layout of the dashboard
app.layout = html.Div([
    html.H1("Simple Interactive Dashboard"),

    dcc.Dropdown(
        id='plot-type',
        options=[
            {'label': 'Bar Plot', 'value': 'bar'},
            {'label': 'Line Plot', 'value': 'line'},
            {'label': 'Scatter Plot', 'value': 'scatter'}
        ],
        value='bar'
    ),

    dcc.Graph(id='graph')
])

# Callback to update the graph based on the selected plot type
@app.callback(
    Output('graph', 'figure'),
    Input('plot-type', 'value')
)
def update_graph(plot_type):
    if plot_type == 'bar':
        fig = px.bar(df, x='Category', y='Values', title='Bar Plot')
    elif plot_type == 'line':
        fig = px.line(df, x='Category', y='Values', title='Line Plot')
    elif plot_type == 'scatter':
        fig = px.scatter(df, x='Category', y='Values', title='Scatter Plot')
    return fig

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
