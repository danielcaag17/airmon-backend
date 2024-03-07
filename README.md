This is the backend repository for the project Airmon of the subject PES QP23-24.

# Installation
This installation is thought on ubuntu 22.04.

· Python:
First of all you should have installed python. Check that by executing in the terminal:
python --version
This should show you the python version. Use Python 3.11.5:
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt update
sudo apt install python3.11
sudo apt install python3.11-venv

· Environment:
To create an environment for the project use:
python3.11 -m venv env
This will create the environment but you may need to activate it using:
source env/bin/activate
We also recommend you to have a shortcut to open the directory and activate the environment so that you never forget.
You can do that, for example, by adding this alias to your profile shell file (.bashrc, .zshrc, etc):
alias airmon-back="cd /path/to/airmon/airmon-backend && source env/bin/activate"

· Pip:
Install on the env pip and then execute:
pip install -r requirements.txt

