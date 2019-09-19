# Process-API

#### API for retrieving host system information via HTTP

Based on the Flask Python framework and Gunicorn Python WSGI HTTP Server.

### What it does

- Provides an HTTP endpoint `/processes` with a JSON output listing the processes running on the host system
- Included process information: Process name, PID, PPID, environment and command
- The API process itself is excluded from the API output
- Deployed as a systemd service, it is manageable via standard `systemctl` commands

### What it does NOT

- Authentication: In order to stay within the project boundaries, there is no user registration, database etc. involved and therefore no authentication possible
- Scale: In order to keep the dependencies low, the application is deployed without a proxy. Gunicorn is probably fine for an internal API, but would need e.g. nginx as a proxy for scalability
- Portability: The deployment is only tested on Ubuntu 18.04
- An API prefix like /api/v1/ for extensibility has been omitted by purpose for exact requirements fulfillment


## Requirements

Ubuntu 18.04 default image

## Deployment with Ansible

Deployment host Ansible version >=2.8

Run the playbook `deployment.yml`, providing your target host address (don't omit the comma):

    ansible-playbook -i 192.168.56.101, \
        deployment.yml \
        --ask-become-pass \
        -e ansible_python_interpreter=auto


## Manual Deployment

    sudo apt-get update && sudo apt-get install python3-pip python3-venv
    sudo adduser process-api
    cd /opt
    sudo git clone https://github.com/haeringer/process-api.git
    sudo cp process-api/configs/process-api.service /etc/systemd/system/
    sudo systemctl daemon-reload
    sudo chown -R process-api:process-api process-api
    sudo su process-api
    printf "\nexport FLASK_APP=main.py\nexport FLASK_ENV=development\n" >> ~/.bashrc
    cd /opt/process-api
    python3 -m venv venv
    . venv/bin/activate
    pip3 install -r app/requirements.txt

dev server:

    python3 main.py

gunicorn test:

    gunicorn main:app -b 0.0.0.0:5000

prod server:

    systemctl start process-api.service


## Management of the Process-API Gunicorn service

    systemctl start/status/stop/restart process-api.service


## Access the API

    curl -i http://<host>:8000
