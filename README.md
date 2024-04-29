# netscanner v1.0
Local network scanner to detect hosts connected to our network

With netscanner we are able to scan our local network and see all hosts connected to it. netscanner is a 
Python script that uses the module scapy and returns IP and MAC of the connected hosts in our private network.

You will need to install Python. Then install scapy in a virtual environment using the following commands:
  -- python -m venv 'name' , Creating virtual environment 'name'
  -- source name/bin/activate , Activating virtual environment 'name'
  -- pip install scapy , Installing scapy module with pip
  -- deactivate , deactivate the virtual environment if we want

To run the script we just type as sudo:
  -- sudo python netscanner.py


