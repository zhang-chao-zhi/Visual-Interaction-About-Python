import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash()

app.layout = html.Div([
    html.Label('Dropdown 单选下拉框'),
    dcc.Dropdown(
        options=[
            {'label': '北京', 'value': 'BJ'},
            {'label': '上海', 'value': 'SH'},
            {'label': '广州', 'value': 'GZ'}
        ],
        value='GZ'  # 默认值
    ),
    html.Br(),  # 换行

    html.Label('Dropdown 多选下拉框'),
    dcc.Dropdown(
        options=[
            {'label': '北京', 'value': 'BJ'},
            {'label': '上海', 'value': 'SH'},
            {'label': '广州', 'value': 'GZ'}
        ],
        value=['BJ', 'GZ'],
        multi=True  # 多选
    ),
    html.Br(),

    html.Label('RadioItems 单选按钮'),
    dcc.RadioItems(
        options=[
            {'label': '北京', 'value': 'BJ'},
            {'label': '上海', 'value': 'SH'},
            {'label': '广州', 'value': 'GZ'}
        ],
        value='GZ'
    ),
    html.Br(),

    html.Label('Checklist 复选按钮'),
    dcc.Checklist(
        options=[
            {'label': '北京', 'value': 'BJ'},
            {'label': '上海', 'value': 'SH'},
            {'label': '广州', 'value': 'GZ'}
        ],
        value=['BJ', 'GZ']
    ),
    html.Br(),

    html.Label('Input 输入框'),
    html.Br(),
    dcc.Input(value='广州', type='text'),
    html.Br(),
    html.Br(),

    html.Label('Slider 滑动条'),
    dcc.Slider(
        min=0,
        max=9,
        marks={i: str(i) for i in range(10)},  # 传入字典作为标记显示
        value=3,
    ),
    html.Br(),
])

if __name__ == '__main__':
    app.run_server(debug=True)
