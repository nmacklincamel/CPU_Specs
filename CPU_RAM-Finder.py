# Problem: I want to easily find the RAM that I can buy that corresponds with specific Intel CPUs. (i.e. i7 4790k)
#          --OR-- to find *all* AMD/Intel CPUs that take either ddr2, ddr3, or ddr4

# Gathered Information from amd.com && ark.intel.com

# Installed imports
from bs4 import BeautifulSoup
# Ordinary imports
import requests
import string
import re

def main():

    options = input("Enter 1 if you want to search for RAM that takes a specific CPU\n --OR--\nEnter 2 if you want to search for all AMD/Intel CPUs that take a specific RAM\n")
    if options == "1":
        RAM()
    elif options == "2":
        ALL_CPUs()
    else:
        print("Sorry, that was *NOT* 1 or 2. Please try again.")
        main()

# METHOD: RAM()
# Search for the input using browser search and return the ddr_type
#   (ddr2,ddr3,ddr4) and then return the newegg link when you search
#   that type of ram using price_low to price_high
def RAM():
    while True:
        amd_vs_intel = input("Enter 1 if the CPU you want to search for is Intel or enter 2 if its AMD:\n")
        if amd_vs_intel == "2":
            cpu_name = input("Enter the name of your CPU (i.e. i7-4790K or FX 8350):\n")
            request_get = requests.get(,headers={'', 'User-Agent': 'Mozilla/5.0'})

            # request_get = requests.get(''.join(['https://www.amd.com/en/products/cpu/amd-', cpu_name.replace(" ","-")]), headers={'User-Agent': 'Mozilla/5.0'}) # using https for the time being
            # amd_soup = BeautifulSoup(request_get.content, "html5lib")
            print("Nicely printed amd stuff\n")
            break
        elif amd_vs_intel == "1":
            cpu_name = input("Enter the name of your CPU (i.e. i7-4790K or FX 8350):\n")

            # do the same for amd but use an intel link
            print("Nicely printed intel stuff\n")
            break
        else:
            print("Sorry, that was *NOT* 1 or 2. Please try again.")

def ALL_CPUs():
    while True:
        ddr_type = input("Enter 2 if you want to search for DDR2 RAM, 3 for DDR3 RAM, or 4 for DDR4 RAM : ")
        if ddr_type == "2":
            # do some action
            break
        elif ddr_type == "3":
            # do some action
            break
        elif ddr_type == "4":
            # do some action
            break
        else:
            print("Sorry, that was *NOT* 2, 3 or 4. Please try again.")

# init the program
main()
