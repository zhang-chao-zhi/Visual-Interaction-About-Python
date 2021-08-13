# python可视化交互库——dash
## 简介：
`Dash`是一款web应用的python框架，建立在 Plotly.js, React 和 Flask 之上，将现代UI元素(如下拉框、滑块和图形)直接与Python代码绑定。
`dash_core_components`模块的`Graph`使用开源JavaScript库 plotly.js，支持超过35种图表类型，并以矢量SVG和高性能WebGL呈现。
```python
import dash
import pandas as pd
import plotly.express as px
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash()

df = pd.read_csv('GDP与人均寿命.csv')

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
```

