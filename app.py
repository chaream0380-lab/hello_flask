import os
import random
from flask import Flask, request, render_template_string

app = Flask(__name__)

# HTMLテンプレート
html = """
<!doctype html>
<title>Hello App</title>
<h1>名前を入力してください</h1>
<form method="POST">
  <input type="text" name="username">
  <input type="submit" value="送信">
</form>
{% if name %}
  <h2>Hello, {{ name }}!</h2>
  <p>{{ message }}</p>
{% endif %}
"""

# メッセージ候補
messages = [
    "Nice to meet you!",
    "Have a great day!",
    "Welcome back!",
    "How's it going?",
    "Good luck today!"
]

@app.route('/', methods=['GET', 'POST'])
def hello():
    name = None
    message = None
    if request.method == 'POST':
        name = request.form.get('username')
        if name:  # 名前が入力されていたら
            message = random.choice(messages)  # ランダムで1つ選ぶ
    return render_template_string(html, name=name, message=message)

if __name__ == '__main__':
    # Render用：環境変数PORTを参照
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

