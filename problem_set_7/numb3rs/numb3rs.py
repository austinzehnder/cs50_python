import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    if re.match(r"[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}", ip, re.IGNORECASE):
        return len(ip.split('.')) == 4 and all(0<= int(octet) <= 255 for octet in ip.split('.'))
    return False

if __name__ == "__main__":
    main()
