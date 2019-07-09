#!/usr/bin/env python3

import sys
import requests
import re

def check_mac(mac):
    """use this function to check if a string supplied is a mac address"""
    return re.match('[0-9a-f]{2}([-:.]?)[0-9a-f]{2}(\\1[0-9a-f]{2}){4}$', mac.lower())

def getCompany():
    """use this function to query the macaddress.io API with the api key and mac address"""
    try:
        API_AUTH_KEY=sys.argv[1]
        MAC=sys.argv[2]
    except IndexError:
        sys.exit("error: please the following format 'mac_address.py <api key> <mac address>'")
    url='https://api.macaddress.io/v1?apiKey='+API_AUTH_KEY+'&output=vendor&search='+MAC.lower()
    if not check_mac(MAC):
        sys.exit("please enter a valid mac address")
    try:
        resp = requests.get(url)
    except Exception:
        sys.exit("error: Issue with api request. Please check parameters.")
    else:
        print(resp.text)

if __name__ == "__main__":
    getCompany()

