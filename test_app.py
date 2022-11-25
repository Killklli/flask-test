from flask import Flask
from cli import main
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    time1 = datetime.now()
    main(None, None)
    time2 = datetime.now()
    return f"{time1} start, {time2} end"
