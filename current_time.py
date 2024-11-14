from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def current_time():
    now = datetime.now()
    formatted_time = now.strftime('%Y-%m-%d %H:%M:%S')
    return f"""
    <html>
        <head>
            <style>
                body {{
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    height: 100vh;
                    margin: 0;
                    font-family: Arial, sans-serif;
                    font-size: 24px;
                }}
            </style>
        </head>
        <body>
            Сейчас ровно: {formatted_time}
        </body>
    </html>
    """

if __name__ == "__main__":
    app.run()