from flask import Flask
from flask import jsonify
from flask import render_template
from flask import request
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/api', methods=['POST'])
def api():
    return jsonify(request.get_json())

if __name__ == '__main__':
    app.run(debug=True)
