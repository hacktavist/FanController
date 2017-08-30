import sys
import os
from rflib import *

from sys import version_info





d = RfCat();
d.setFreq(433927500)
d.setMdmModulation(MOD_ASK_OOK)
d.setMdmDRate(int(1.0/0.000395833))

response = 9999
while response != 0:
        os.system("clear")
	if response == 1:
	  d.RFxmit("\xb6\xdb\x64\xb2\x48\x00\x00\x00" * 3)
	if response == 2:
	  d.RFxmit("\xb6\xdb\x65\x92\x48\x00\x00\x00" * 3)
	if response == 3:
	  d.RFxmit("\xb6\xdb\x6c\x92\x48\x00\x00\x00" * 3)
	if response == 4:
	  d.RFxmit("\xb6\xdb\x64\x96\x48\x00\x00\x00" * 3)
	if response == 5:
	  d.RFxmit("\xb6\xdb\x64\x92\xc8\x00\x00\x00" * 3)
	if response == 0:
  	  sys.exit()
	print("Fan Controller v1.0.1")
	print("[1]Fan Speed Low")
	print("[2]Fan Speed Medium")
	print("[3]Fan Speed High")
	print("[4]Reverse Spin Direction")
	print("[5]Off")
        print("[0]Exit")


        response = raw_input("Please Enter a Fan Control Option: ")
        response = int(response)
