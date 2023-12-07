import os

os.system("airmon-ng start wlan0")
os.system("airodump-ng wlan0mon")

BSSID = input("Enter the BSSID of the network to be sniffed: ")
channel = input("Enter the channel this network is working on: ")
packageName = input("Name of directory to save the package: ")

os.system("mkdir DataGenerated/" + packageName)

print("airodump-ng -d " + BSSID + " -c" + channel + " -w DataGenerated/"+packageName+ "/"
          + packageName + " wlan0mon")

os.system("airodump-ng -d " + BSSID + " -c" + channel + " -w DataGenerated/"+packageName+ "/"
          + packageName + " wlan0mon")
