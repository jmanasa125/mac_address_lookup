# mac_address_lookup

For a given MAC address retrieve company name.

- Program accepts a command line parameter of a MAC address
- Which outputs the Company Name associated with that MAC address 

Install required packages

Step 1. python setup.py install

Execute the script with MAC address as an argument

Step 2. python mac_addr.py 44:38:39:ff:ef:57

# Pre-requisite
Assume python2 is installed in your system

python - version - 2.7

# Sample snippet
python macc_addr.py 44:38:39:ff:ef:57 

Company Name for mac 44:38:39:ff:ef:57 is Cumulus Networks, Inc

# Using Docker
You can use the Dockerfile to get an image

Once you have the image, we can get output with below command in linux

sudo docker run image_id 44:38:39:ff:ef:57

