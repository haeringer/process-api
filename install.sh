#!/bin/bash

appdir="/opt/process-api"
venv="$appdir/venv"


printf "Updating repository cache & installing packages ...\n"
apt-get -q update && apt-get -qqy install python3-pip python3-venv

printf "Creating application directory in /opt/ ...\n"
mkdir $appdir && cp -r ./ $appdir

printf "Creating Python virtual environment ...\n"
python3 -m venv $venv

printf "Activating Python virtual environment ...\n"
source $venv/bin/activate

printf "Installing Python dependencies ...\n"
pip3 install -r $appdir/requirements.txt --install-option="--install-scripts=$venv/bin"

printf "Copying systemd service file ...\n"
cp configs/process-api.service /etc/systemd/system/

printf "Reloading systemd manager configuration ...\n"
systemctl daemon-reload

printf "Starting process-api gunicorn service ...\n"
systemctl start process-api
