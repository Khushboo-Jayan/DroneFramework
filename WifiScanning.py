import os
from mac_vendor_lookup import MacLookup

os.system("airmon-ng start wlan0")
os.system("airodump-ng --band abg wlan0mon")

BSSID = input("Enter the BSSID of any network to be sniffed: ")
channel = input("Enter the channel this network is working on: ")
packageName = input("Name of directory to save the package: ")

os.system("mkdir DataGenerated/" + packageName)

os.system("sudo airodump-ng wlan0mon -c " + channel + " --bssid " + BSSID)

# "98:AF:65:B9:F3:E3" is intel
macAddr = input("Enter the mac address for the vendor lookup: ")
try:
  print("\nMacAddress: " + macAddr + "\nVendor: " + MacLookup().lookup(macAddr))
except:
  print("Mac vendor not registered")


