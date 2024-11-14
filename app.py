from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)


@app.route("/")
def current_time():
    now = datetime.now()
    formatted_time = now.strftime('%Y-%m-%d %H:%M:%S')
    return render_template('index.html', time=formatted_time)


if __name__ == "__main__":
    app.run()