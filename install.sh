#!/bin/bash

appdir="/opt/process-api"
venv="$appdir/.venv"
scriptsrc="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"


printf "Updating repository cache & installing packages ...\n"
apt-get -q update && apt-get -qqy install python3-pip python3-venv

printf "Creating application directory in /opt/ ...\n"
mkdir $appdir && cp -r $scriptsrc/. $appdir

printf "Creating Python virtual environment ...\n"
python3 -m venv $venv

printf "Activating Python virtual environment ...\n"
source $venv/bin/activate

printf "Installing Python dependencies ...\n"
export PIPENV_VENV_IN_PROJECT
pip3 install -r $appdir/requirements.txt

printf "Copying systemd service file ...\n"
cp $appdir/configs/process-api.service /etc/systemd/system/

printf "Reloading systemd manager configuration ...\n"
systemctl daemon-reload

printf "Enabling process-api gunicorn service unit ...\n"
systemctl enable process-api

printf "Starting process-api gunicorn service ...\n"
systemctl start process-api
