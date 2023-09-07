from flask import Flask, render_template_string

app = Flask(__name__)

@app.route("/")
def index():
    # 定义HTML模板
    template = """
    <!DOCTYPE html>
    <html>
    <head>
    <title>欢迎词示例</title>
    </head>
    <body>
    <h1>{{ welcome_message }}</h1>
    </body>
    </html>
    """

    # 渲染模板并返回响应
    return render_template_string(template, welcome_message="欢迎来到我的网站！")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
