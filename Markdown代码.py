import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash()

markdown_text = '''
# 你的Markdown代码
## 欢迎你的到来
## 制作自己的markdown
```python
import dash
import dash_core_components as dcc
import dash_html_components as html
```
'''

app.layout = html.Div([
    dcc.Markdown(children=markdown_text)
])

if __name__ == '__main__':
    app.run_server(debug=True)
