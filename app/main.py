import os
import psutil

from flask import Flask

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
    """List all processes running on the host system."""

    processes = {}
    pgid_current = os.getpgid(0)

    for proc in psutil.process_iter():
        try:
            pinfo = proc.as_dict(attrs=[
                'name', 'pid', 'ppid', 'environ', 'cmdline',
            ])
        except psutil.NoSuchProcess:
            pass
        else:
            pgid = os.getpgid(pinfo['pid'])
            if not pgid == pgid_current:
                processes[pinfo['name']] = pinfo

    return processes


if __name__ == '__main__':
    app.run(host='0.0.0.0')
