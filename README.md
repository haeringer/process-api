# Process-API
[![Build Status](https://travis-ci.org/haeringer/process-api.svg?branch=master)](https://travis-ci.org/haeringer/process-api)

- Provides an HTTP endpoint `/processes`, listing the processes running on the host system in JSON format
- Included process information:
    - Process name
    - PID
    - PPID
    - Environment
    - Command
- The API process itself is excluded from the API output by filtering on its PGID
- Deployed as a systemd service, it is manageable via standard `systemctl` commands


### Things to consider

- In order to stay within the project boundaries, there is no user registration, database etc. involved and therefore no authentication service provided
- In production, the application should only be deployed behind a proxy (e.g. nginx) for the following reasons:
    - The API service needs to run as root in order to read the environment variables of all processes. Therefore, it should not be exposed.
    - Due to the sensitive nature of environment variables, the connection should be SSL encrypted
    - Scalability, because Gunicorn alone doesn't scale well
- Portability: The deployment is only tested on Ubuntu 18.04 with default Python 3.6
- An API prefix like /api/v1/ for extensibility has been omitted by purpose for exact requirements fulfillment


## Installation

Requirements:

- A running instance of Ubuntu Server 18.04
- A user account with sudo privileges
- If Ansible is used for the installation, an Ansible host with Ansible release >=2.8

### Deployment with Ansible

To deploy the application on a single machine, run the playbook `deployment.yml` against your target host address (don't omit the comma):

    ansible-playbook -i 10.1.2.3, \
        deployment.yml --ask-become-pass \
        -e ansible_python_interpreter=auto

### Deployment with install script

Clone the repository somewhere to your target host and run the install script from there:

    sudo bash install.sh


## Management of the Process-API service

Manually start the Process-API service:

    systemctl start process-api.service

View the status and potential exit codes in case of problems:

    systemctl status process-api.service


## Accessing the API

The HTTP server runs on port 8000.

    curl -i http://<yourhost>:8000
