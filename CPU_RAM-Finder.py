# Problem:
#   I want to easily find the RAM that I can buy that corresponds with specific Intel CPUs. (i.e. i7 4790k)
#          --OR--
#   to find *all* AMD/Intel CPUs that take either ddr2, ddr3, or ddr4
#
# Gathered Information from amd.com && ark.intel.com
#
# DISCLAIMER: Sooo, I reached a point where I was being recognized as a bot for
#   you know... web scraping... So, instead... I found the data on the above websites
#   and saved them as a CSV. As this will not be a permanent fix with new hardware
#   coming out all the time, I will figure out a way to become an unrecognizable bot
#   and make this program more adaptable. --- That IS why I am using a CSV.
# ------------------------------------------------------------------------------
# Installed imports
from bs4 import BeautifulSoup
# Ordinary imports
import requests
import string
import re
# Reading stored data
import csv
import sys

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
        amd_vs_intel = input("Enter 1 if the CPU you want to search for is AMD or enter 2 if its Intel:\n") # decide which file to use -- can be omitted a search delim is added
        if amd_vs_intel == "1": # AMD
            cpu_name = input("Enter the name of your CPU (i.e. fx-6300 or FX 8350):\n")

            with open('AMD_processors_list_2012-2020.csv',"r") as file:
                csv_read = csv.reader(file)
                for line in csv_read:
                    for item in line:
                        if cpu_name == item:
                            temp_line = line # use this for more complex parts of the tool
                            print("\nHere are some specs found about the searched CPU:")
                            print("Processor:             {0}".format(line[2]))
                            cleprint("Release year:          {0}".format(line[8]))
                            print("Cores/Threads:         {0} cores/{1} threads".format(line[10],line[11]))
                            print("Base/Max frequency:    {0}/{1} ".format(line[14],line[15]))
                            print("Supported RAM type(s): {0}".format(line[30]))
# TODO: Must create a way to display the data in 'line' that equals the cpu_name in a format that looks good and omits the uneccessary items
    # Name of processor -if any more- i7-4790k ---> Intel Core i7-4790K Devil's Canyon Quad-Core 4.0GHz
    # ddr_type : ***
    # 2-5 links to pages where you can view the corresponding RAM
        # Possibly with ratings of which RAM is the best to worst
        # links should have Rated(best-worst), pricing, name, site name, and link
                    # end of item for
                # end of line for
            # request_get = requests.get(''.join(['https://www.amd.com/en/products/cpu/amd-', cpu_name.replace(" ","-")]), headers={'User-Agent': 'Mozilla/5.0'}) # using https for the time being
            # amd_soup = BeautifulSoup(request_get.content, "html5lib")
            break # terminates program
        elif amd_vs_intel == "2": # Intel
            cpu_name = input("Enter the name of your CPU (i.e. i7-4790K or i7 4790k):\n")
            with open('Intel_processors_list_2006-2019.csv',"r") as file:
                csv_read = csv.reader(file)
                for line in csv_read:
                    for item in line:
                        if cpu_name == item:
                            temp_line = line # use this for more complex parts of the tool
# TODO: Must create a way to display the data in 'line' that equals the cpu_name in a format that looks good and omits the uneccessary items
    # Name of processor -if any more- i7-4790k ---> Intel Core i7-4790K Devil's Canyon Quad-Core 4.0GHz
    # ddr_type : ***
    # 2-5 links to pages where you can view the corresponding RAM
        # Possibly with ratings of which RAM is the best to worst
        # links should have Rated(best-worst), pricing, name, site name, and link
                            print("\nHere are some specs found about the searched CPU:")
                            print("Processor:             {0}{1}".format(line[1],line[2]))
                            print("Release year:          {0}".format(line[4]))
                            print("Cores/Threads:         {0} cores/{1} threads".format(line[6],line[7]))
                            print("Base/Max frequency:    {0} GHz/{1} GHz".format(line[8],line[11]))
                            print("Supported RAM type(s): {0}".format(line[13]))
                    # end of item for
                # end of line for
            break # terminates program
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
