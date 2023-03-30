Auto Device Reset

Auto Device Reset is a Python program that automates the process of resetting a network device when it stops responding to pings. The program uses the ping command to continuously ping the device until it responds, and then uses SSH to log into the device and execute the set-default command to reset it.
Requirements

    Python 3.x
    Paramiko (can be installed via pip install paramiko)

Usage

    Clone this repository to your local machine.
    Open auto_device_reset.py in a text editor and modify the device_ip, ssh_username, and ssh_password variables to match your network device's IP address and login credentials.
    Run the program by typing python auto_device_reset.py in the terminal.
    The program will continuously ping the device until it responds, and then reset the device using SSH. It will continue this loop until the program is interrupted (e.g. by pressing Ctrl + C).

Contributing

If you'd like to contribute to this project, feel free to submit a pull request or open an issue.
License

This project is licensed under the MIT License - see the LICENSE file for details.
