# -- Web-Based IP Address Validator --
# By Arun Barnard on 01/07/19

# Import libraries and modules
from flask import Flask, render_template, request
import pandas as pd
from geoip import geolite2


app = Flask(__name__)

# Default
@app.route('/')
def home():
    # Return the default HTML site when the website loads.
    return render_template('main.html')


@app.route('/', methods=['POST'])
def my_form_post():

    # Read known exit nodes CSV file
    nodes = pd.read_csv("torExitNodes.csv")
    # nodes = nodes['Addresses']
    # Fetch ip from the form
    ip = request.form['number']

    # Put IP through various validation tests
    if validate1(ip):
        if validate2(ip):
            # status = isTorExit(ip, nodes)
            if isTor(ip, nodes):
                # Return valid HTMl site, letting the user know it is a known Tor exit node.
                return render_template('valid.html', value=str(ip), torStatus="This is a known Tor exit node.", location=ipLocation(ip))
            else:
                # Return invalid HTML site, letting the user know it is not a known Tor exit node.
                return render_template('valid.html', value=str(ip), torStatus="This is not a known Tor exit node.", location=ipLocation(ip))
        else:
            # Return invalid HTML page
            return render_template('invalid.html', value=str(ip))
    else:
        # Return invalid HTML page
        return render_template('invalid.html', value=str(ip))


def isTor(ip, nodes):
    if ip in str(nodes['addresses']):
        return True
    else:
        return False


def ipLocation(ip):
    match = geolite2.lookup(ip)
    if match is not None:
        output = match.country
        return output
    else:
        return "Unknown"


def validate1(ip):

    # Establish a count
    count = 0
    try:
        ip = ip.replace(".", "")
    except:
        print("")

    # Check input IP is numerical
    if ip.isdigit():
        count = count + 1

    # If the address is between 5 and 12 characters
    if 4 <= len(ip) < 13:
        count = count + 1

    # If the count is 2, then valid
    if count == 2:
        return True
    else:
        return False


def validate2(ip):

    # Establish a count
    count = 0

    # Put IP address into an array of 4 parts where it is split into four parts at every decimal point.
    splitIp = ip.split(".")

    # Check each block is valid for an IPv4 address (a value between 0 and 255)
    # Try to float each section of the ip address...
    # ...so that the program doesn't crash if the section contains anything that isn't numerical
    try:
        if 0 <= float(splitIp[0]) <= 255:
            count = count + 1

        if 0 <= float(splitIp[1]) <= 255:
            count = count + 1

        if 0 <= float(splitIp[2]) <= 255:
            count = count + 1

        if 0 <= float(splitIp[3]) <= 255:
            count = count + 1
    except:
        print("")

    # If all 4 blocks are valid, then valid
    if count == 4:
        return True
    else:
        return False


if __name__ == "__main__":
    # Setup data
    app.run(debug=True, port=8080)