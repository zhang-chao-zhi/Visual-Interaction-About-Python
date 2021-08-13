import dash
import pandas as pd
import plotly.express as px
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash()

df = pd.read_csv('GDP和人均寿命.csv')

fig = px.scatter(df, x='gdp per capita', y='life expectancy',
                 size='population', color='continent', hover_name='country',
                 log_x=True, size_max=60)

app.layout = html.Div([
    dcc.Graph(
        id='life-exp-vs-gdp',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
