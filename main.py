from flask import Flask
from flask import request
app = Flask(__name__)


@app.route('/')
def index():


@app.route('/recommendation', methods=['POST'])
def get_recommendation():


if __name__ == '__main__':
    app.run(debug=True)