import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

app = dash.Dash()

app.layout = html.Div([
    html.H1('智能聊天机器人'),
    dcc.Input(id='my-id', value='在吗？', type='text'),
    html.Div(id='my-div')
])


@app.callback(
    Output(component_id='my-div', component_property='children'),  # 输出给id为my-div的children
    [Input(component_id='my-id', component_property='value')]  # 输入来自id为my-id的value
)
def update_output_div(input_value):
    '''AI核心代码，估值1个亿'''
    return input_value.replace('吗', '').replace('?', '!').replace('？', '！')


if __name__ == '__main__':
    app.run_server(debug=True)
