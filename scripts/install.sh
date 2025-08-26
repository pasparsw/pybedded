# prerequisite: arduino-cli lib install Servo
arduino-cli lib install LiquidCrystal
arduino-cli lib install SD
arduino-cli lib install Stepper
arduino-cli lib install Ethernet
arduino-cli lib install Keyboard
"""
        # IMPORTANT: need to install arduino-cli first with sudo snap install arduino-cli
        # and install all the necessary platforms (example: arduino-cli core install arduino:avr)
        And this is a good content for bug of the week:
        sudo snap connect arduino-cli:raw-usb
        sudo snap set system experimental.hotplug=true
        sudo systemctl restart snapd
        sudo snap connect arduino-cli:serial-port
        """