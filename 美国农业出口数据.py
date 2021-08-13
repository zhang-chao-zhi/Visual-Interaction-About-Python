import dash
import pandas as pd
import dash_html_components as html

df = pd.read_csv('美国农业出口数据.csv')


def generate_table(dataframe, max_rows=10):
    '''生成表格'''
    return html.Table([
        html.Thead(
            html.Tr([html.Th(col) for col in dataframe.columns])
        ),
        html.Tbody([
            html.Tr([
                html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
            ]) for i in range(min(len(dataframe), max_rows))
        ])
    ])


app = dash.Dash()

app.layout = html.Div(
    children=[
        html.H4(
            children='US Agriculture Exports (2011)'
        ),
        generate_table(df)
    ])

if __name__ == '__main__':
    app.run_server(debug=True)
