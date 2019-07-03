# ip-validator

A simple script written in Python with Flask to provide details of a given IP address.

Including:
* Validity of the address
* Whether the addresss is a known Tor exit node
* Approxmiate location of the address if known

## Download

To get the script, either download the .zip or:
```
git clone https://github.com/arunbarnard/ip-validator
```
## Run

Navigate to the download location, and run with:
```
python validator.py
```
## Modification

You are able to modify the Python or HTML code by modifying the following files:

* validator.py - Main Python script
* templates
  * main.html - Default HTML page
  * valid.html - Shown when address is valid
  * invalid.html - Shown when address is invalid
* static
  * css
    * main.css - CSS for all HTML files
