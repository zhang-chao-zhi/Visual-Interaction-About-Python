import dash
import pandas as pd
import plotly.express as px
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash()

colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}

df = pd.DataFrame({'x': [1, 2, 3], 'SF': [4, 1, 2], 'Montreal': [2, 4, 5]})

fig = px.bar(df, x='x', y=['SF', 'Montreal'], barmode='group')

fig.update_layout(plot_bgcolor=colors['background'], paper_bgcolor=colors['background'], font_color=colors['text'])

app.layout = html.Div(
    style={'backgroundColor': colors['background']},
    children=[
        html.H1(
            children='Hello Dash',
            style={
                'textAlign': 'center',
                'color': colors['text']
            }
        ),

        html.Div(
            children='Dash: 一款Python web应用框架',
            style={
                'textAlign': 'center',
                'color': colors['text']
            }
        ),

        dcc.Graph(
            id='example-graph-2',
            figure=fig
        )
    ])

if __name__ == '__main__':
    app.run_server(debug=True)
