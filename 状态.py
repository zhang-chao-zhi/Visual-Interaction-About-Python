import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State

app = dash.Dash()

app.layout = html.Div([
    dcc.Input(id='input-1-state', type='text', value='初始值1'),
    dcc.Input(id='input-2-state', type='text', value='初始值2'),
    html.Button(id='submit-button-state', n_clicks=0, children='Submit'),
    html.Div(id='output-state')
])


@app.callback(Output('output-state', 'children'),
              [Input('submit-button-state', 'n_clicks')],
              [State('input-1-state', 'value'),
               State('input-2-state', 'value')])
def update_output(n_clicks, input1, input2):
    return '点击了 {} 次：{}, {}'.format(n_clicks, input1, input2)


if __name__ == '__main__':
    app.run_server(debug=True)
