from flask import Flask
import os

port = int(os.environ.get('PORT', 5000))
app = Flask(__name__)


@app.route("/")
def home_view():
		return "<h1>Welcome to Geeks for Geeks</h1>"

app.run(host='0.0.0.0', port=port, debug=True)
