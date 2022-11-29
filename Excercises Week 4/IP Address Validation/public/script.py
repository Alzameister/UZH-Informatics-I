#!/usr/bin/env python3

# These are examples for valid and invalid inputs to your validation function


from multiprocessing.sharedctypes import Value


IPv4_STRING = "127.0.0.1"
IPv4_INVALID_STRING = "300.0.0.1"
IPv6_STRING = "2001:0db8:85a3:0000:0000:8a2e:0FFF:7334"
IPv6_INVALID_STRING = "0:0:0:0:0:0:0:GFFF"
INVALID_IP_STRING = "Some arbitrary string"


def is_valid_IPv4_octet(octet: str):
    #"""Returns True if octet represents a valid IPv4 octet, False otherwise"""
    try:
        if 0 <= int(octet) <= 255:
            return True
    except ValueError:
        return False
    return False

def is_valid_IPv4(ip: str):
    #Returns True if ip represents a valid IPv4 address, False otherwise
    octets = ip.split(".")

    if len(octets) <= 4:
        if all(is_valid_IPv4_octet(octet) for octet in octets):
                return True
    return False

def is_valid_IPv6_hextet(hextet: str):
    #"""Returns True if hextet represents a valid IPv6 hextet, False otherwise"""
    try:
        if 0 <= int(hextet, 16) <= 65535:
            return True
    except ValueError:
        return False
    return False

def is_valid_IPv6(ip: str):
    #"""Returns True if ip represents a valid IPv6 address, False otherwise"""
    hextets = ip.split(":")
    
    if len(hextets) <= 8:
        if all(is_valid_IPv6_hextet(hextet) for hextet in hextets):
            return True
    return False

def is_valid_IP(ip: str):
    #"""Returns True if ip represents a valid IPv4 or IPv6 address False otherwise"""
    if all([character.isdigit() or character == "." for character in ip]):   #Checks all characters in ip for numbers and "." --> IPV4 Address
        if is_valid_IPv4(ip):
            return True
    elif all([character.isalnum() or character == ":" for character in ip]):
        if is_valid_IPv6(ip):
            return True
    return False


# The following lines call is_valid_IP and print the result.
# This way you can check what it does.
# However, we encourage you to write tests, because then you
# can easily test many different values on every "Test & Run"!
print(
    f"{IPv4_STRING} is a valid IP Address:",
    is_valid_IP(IPv4_STRING))
print(
    f"{IPv4_INVALID_STRING} is a valid IP Address:",
    is_valid_IP(IPv4_INVALID_STRING),
)
print(
    f"{IPv6_STRING} is a valid IP Address:",
    is_valid_IP(IPv6_STRING))
print(
    f"{IPv6_INVALID_STRING} is a valid IP Address:",
    is_valid_IP(IPv6_INVALID_STRING),
)
print(
    f"{INVALID_IP_STRING} is a valid IP Address:",
    is_valid_IP(INVALID_IP_STRING),
)
