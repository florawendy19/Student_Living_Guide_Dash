import pandas as pd
import plotly.express as px
import dash
from dash import dcc
from dash import html
from dash import dash_table
# Load data into a Pandas DataFrame
df = pd.read_csv("../data/processed_data.csv")

fig = px.scatter(df, x="Cost of Living Index", y="Local Purchasing Power Index",
                 size="Groceries Index", color="Continent", hover_name="Country",
                 log_x=True, size_max=60)
# Create the app

app = dash.Dash(__name__)
server = app.server

# Define the bar plot layout
bar_layout = html.Div(children=[
    html.H2(children='Cost of Living by Country'),
    dcc.Graph(id='bar-graph')
])

# Define the map layout
map_layout = html.Div(children=[
    html.H2(children='Cost of Living'),
    dcc.Graph(id='map-graph', style={'height': '100vh'})
])

# Define the scatter layout
scatter_layout = html.Div(children=[
    html.H2(children='Cost of living Index versus Local Purchasing Power Index'),
    dcc.Graph(id='scatter-graph', figure=fig)
])




# Define the tabs
app.layout = html.Div([
    html.H1(children='Student Living Guide'),

    html.Div(children=[
        html.Label('Select Continent of Interest',style={'font-weight': 'bold',"margin-right": "10px"}),
        dcc.Dropdown(
            id="continent-dropdown",
            options=[{'label': i, 'value': i} for i in df['Continent'].unique()],
            value="Africa",
            style={"width": "150px","fontsize":"1px"}
        )
    ], style={'display': 'flex', 'align-items': 'center', 'margin-top': '10px', 'margin-bottom': '10px'}),
    dcc.Tabs(id="tabs", value='tab-1', children=[
        dcc.Tab(label='Map', value='tab-1', children=[map_layout]),
        dcc.Tab(label='Bar Chart', value='tab-2', children=[bar_layout]),
        dcc.Tab(label='Scatter Chart', value='tab-3', children=[scatter_layout])
        
    ])

    
    
])

# Define the callbacks for the stacked bar plot
@app.callback(
    dash.dependencies.Output('bar-graph', 'figure'),
    [dash.dependencies.Input('continent-dropdown', 'value')]
)
def update_bar_plot(continent):
    filtered_df = df[df['Continent'] == continent]
    fig = px.bar(
        filtered_df,
        x='Country',
        y=['Cost of Living Index', 'Rent Index','Groceries Index','Restaurant Price Index'],
        barmode='stack',
        title=f"Cost of Living by Country in {continent}"
    )
    return fig
# Define the callbacks for the Continent map
@app.callback(
    dash.dependencies.Output('map-graph', 'figure'),
    [dash.dependencies.Input('continent-dropdown', 'value')]
)
def update_map(continent):
    filtered_df = df[df['Continent'] == continent]
    fig = px.scatter_mapbox(
        filtered_df,
        lat='latitude',
        lon='longitude',
        hover_name='Cost of Living Index',
        size='Rent Index',
        color='Continent',
        zoom=2,
        title=f"Cost of Living in {continent}"
    )
    fig.update_layout(mapbox_style="open-street-map")
    return fig




# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)