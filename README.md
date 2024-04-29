# netscanner v1.0-beta
Local network scanner to detect hosts connected to our network

With netscanner we are able to scan our local network and see all hosts connected to it. netscanner is a 
Python script that uses the module **scapy** and returns IP and MAC of the connected hosts in our private network.

You will need to install Python. Then install scapy in a virtual environment using the following commands:
  - python -m venv 'name' , Creating virtual environment 'name'
  - source name/bin/activate , Activating virtual environment 'name'
  - pip install -r requirements.txt, Installing scapy module from requirements.txt file
  - deactivate , deactivate the virtual environment if we want to stop using netscanner

To run the script we just type as sudo (make sure you are in a virtual environment):
  - sudo python netscanner.py


