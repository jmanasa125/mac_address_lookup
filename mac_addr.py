import pprint
import requests
import re
import argparse

#URL for th api_key
api_url = "https://api.macaddress.io/v1?apiKey=at_9GCvOaHGn1f7CGwBE7w3C6YZ9vafi"

# Setup commandline parser
parser = argparse.ArgumentParser(description="Query macaddress.io and fetch the vendor information associated with the mac address")

parser.add_argument("macaddr", type=str, help="MAC Address of the device")

parser.add_argument("-o", "--output",
		     help="output format control, accepted values are json, csv, minimal",
        	     dest="output",
                     default="minimal",)
parser.add_argument("-q", "--query",
	             help="query fields, one or multiple comma seperated eg. name,transmission,valid,blockfound",
                     dest="query",
                     default="name",)
parser.add_argument("-r", "--rawjson",
                    help="return raw json from the server that can be piped to jq for other fields",
                    action="store_true",)
parser.add_argument( "-v", "--verbose",
        help="make output more verbose sets to DEBUG",
        action="store_true", )

args = parser.parse_args()
mac_address = args.macaddr

#Checking if the provided mac is valid or not
result = False
if not re.match("^([0-9A-Fa-f]{2}[ :.-]?){6}$" , mac_address.strip()):
    print("Given mac address is not valid!!")
else:
    result = True

#Passing the given mac to URL and get the company name
output = {}
if result:
    parameters = {'output' : 'json', 'search' : mac_address}
    get_req = requests.get(url = api_url, params = parameters)
    output = get_req.json()
    if not 'vendorDetails' in output.keys() or not 'companyName' in output['vendorDetails'].keys():
        print("Vendor Details not found for given mac " + mac_address)
    else:
        print("Company Name for mac " +mac_address+" is " +output['vendorDetails']['companyName'])



