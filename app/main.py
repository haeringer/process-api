import utils

from flask import Flask, jsonify, url_for
app = Flask(__name__)


@app.route('/')
def api_root():
    """Show available endpoints."""

    processes_url = url_for('processes', _external=True)
    return {
        'processes_url': processes_url,
    }


@app.route('/processes')
def processes():
    """List host processes in JSON."""

    processes = utils.get_processes()
    return jsonify(processes)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
