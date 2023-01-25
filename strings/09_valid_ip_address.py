# Valid IP Address

"""
You're given a string of length 12 or smaller, containing only digits. Write a function that returns all the possible IP addresses that can be created by inserting three s in the string.

An IP address is a sequence of four positive integers that are separated by • s, where each individual integer is within the range 0 - 255, inclusive.

An IP address isn't valid if any of the individual integers contains leading © s. For example, "192.168.0.1" is a valid IP address, but "192.168.00.1" and "192.168.0.01" aren't, because they contain "00" and 01 respectively. Another example of a valid IP address is "99.1.1.10"; conversely, "991.1.1.0" isn't valid, because "991" is greater than 255.

Your function should return the IP addresses in string format and in no particular order. If no valid IP addresses can be created from the string, your function should return an empty list.

Note: check out our Systems Design Fundamentals on SystemsExpert to learn more about IP addresses!

# Sample Input
string = "1921680"

# Sample Output

[
    "1.9.216.80",
    "1.92.16.80",
    "1.92.168.0",
    "19.2.16.80",
    "19.2.168.0",
    "19.21.6.80",
    "19.21.68.0",
    "19.216.8.0",
    "192.1.6.80",
    "192.1.68.0",
    "192.16.8.0",

]


"""

import math


def isValidIP(ip_address):
    parts = ip_address.split(".")
    if len(parts) != 4:
        return False
    for part in parts:
        if len(part) > 3:
            return False
        if part == "":
            return False
        if part.startswith("0") and len(part) > 1:
            return False
        if int(part) < 0 or int(part) > 255:
            return False
    return True

# Time: O(1) | Space: O(1)
def validIPAddresses(string):
    length = len(string)
    part_length = 3
    valid_ip_addresses = []
    for i in range(0, part_length + 1):
        for j in range(i + 1, i + part_length + 1):
            for k in range(j + 1, j + part_length + 1):
                ip_address = (
                    string[:i]
                    + "."
                    + string[i:j]
                    + "."
                    + string[j:k]
                    + "."
                    + string[k:]
                )
                if isValidIP(ip_address):
                    valid_ip_addresses.append(ip_address)
    return valid_ip_addresses


if __name__ == "__main__":
    string = "1921680"
    expected_output = sorted(
        [
            "1.9.216.80",
            "1.92.16.80",
            "1.92.168.0",
            "19.2.16.80",
            "19.2.168.0",
            "19.21.6.80",
            "19.21.68.0",
            "19.216.8.0",
            "192.1.6.80",
            "192.1.68.0",
            "192.16.8.0",
        ]
    )
    output = sorted(validIPAddresses(string))
    output_set = set(output)
    expected_output_set = set(expected_output)
    print(output_set.difference(expected_output_set))
    print(expected_output_set.difference(output_set))
    assert sorted(expected_output) == output
