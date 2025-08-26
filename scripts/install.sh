#!/bin/bash

set -e

SCRIPTS_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )
REPO_DIR="$SCRIPTS_DIR/.."
VENV_DIR="$REPO_DIR/venv"
INTERPRETER_PATH="$REPO_DIR/venv/bin/python3"

python3 -m venv $VENV_DIR
$INTERPRETER_PATH -m pip install -r $REPO_DIR/requirements.txt

#sudo snap install arduino-cli
#sudo snap connect arduino-cli:raw-usb
#sudo snap set system experimental.hotplug=true
#sudo systemctl restart snapd
#sudo snap connect arduino-cli:serial-port
#
#arduino-cli core install arduino:avr

arduino-cli lib install Servo
arduino-cli lib install LiquidCrystal
arduino-cli lib install SD
arduino-cli lib install Stepper
arduino-cli lib install Ethernet
arduino-cli lib install Keyboard
