from flask import abort
from flask import Flask
from flask import jsonify
from flask import render_template
from flask import request
from subprocess import Popen

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/api', methods=['POST'])
def api():
    req = request.get_json()
    branch = req.get('branch', 'red')
    repo = req.get('repo', 'colored_pages')
    subdomain = req.get('subdomain')
    if subdomain is None:
        abort(403)

    cmd = 'docker kill {}'.format(subdomain) 
    Popen(cmd.strip().split())
    cmd = 'docker rm {}'.format(subdomain)
    Popen(cmd.strip().split())
    cmd = 'docker run -d -P --name {} -e BRANCH={} -e VIRTUAL_HOST={}.chaxster.com {}'.format(subdomain, branch, subdomain, repo)
    Popen(cmd.strip().split())
    return jsonify(request.get_json())

@app.route('/api/delete', methods=['POST'])
def api_delete():
    req = request.get_json()
    subdomain = req.get('subdomain')
    if subdomain is None:
        abort(403)

    cmd = 'docker kill {}'.format(subdomain)
    Popen(cmd.strip().split())
    cmd = 'docker rm {}'.format(subdomain)
    Popen(cmd.strip().split())
    return jsonify(request.get_json())

if __name__ == '__main__':
    app.run(debug=True)
