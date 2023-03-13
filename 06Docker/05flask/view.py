from flask import Flask, render_template
from dotenv import load_dotenv
import os

load_dotenv()
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)