#!/usr/bin/python
import os
import sys


# run as root user
if not os.geteuid() == 0:
    sys.exit("\nRun as ROOT user\n")

print "\n************ NODE AUTOMATION TOOL ************"
print "\nThis tool will be used in automating the configuration and provision of Dell SuperMicro nodes"

# check for network connectivity


question = str(input("\nMake a selection from the menu.\nType a number: \n'[ 1 ]' RHEV BIOS Config\n'[ 2 ]' SecOnion BIOS Config\n'[ 3 ]' Install ISO on Nodes\n'[ quit ]' to EXIT\nSelection: "))



if "1" in question:
 	cmd = "ansible-playbook automate_bios_RHV.yml"
	print "Running playbook for RHV Node BIOS Configuration"
	os.system(cmd)
elif "2" in question:
	cmd2 = "ansible-playbook automate_bios_BAREMETAL.yml"
        print "Running playbook for SecOnion BIOS Configuration"
	os.system(cmd2)
elif "3" in question:
	# which iso do you want to install
	list_iso_dir = os.listdir("/opt/images/iso/")
	print "\nI see the following ISOs on your Master Laptop:\n"
	print "############ BEGIN ##############\n"
	# for every image in the output
	# add sequence of numbers
	num = 0
	# prep a dictionary for numbers and isos
	num_iso_dict = dict()
	for x in list_iso_dir:
		# if it ends in *.iso
		if x.endswith(".iso"):
			num += 1
			# numbers = key isos = value
			# strip out the whitespace
			iso = x.split()[0].strip()
			# print out the iso
			print num,"--> " + iso
			# creates the dictionary
			num_iso_dict[num] = iso
		
	print "\n############ END ##############"
	iso_question = int(input("\nWhich ISO do you want to baremetal install?\nSelection (select a number): "))
	# print what number and image you selected
	print "DICTIONARY: ", num_iso_dict
	selection = num_iso_dict[iso_question]
	print "Selected: " + selection



	print "Mounting " + "[ " + selection + " ]" + " ISO on Nodes"
        cmd3 = "ansible-playbook baremetal_iso_install.yml"
	cmd3b = ' -e "iso_image='+selection+'"'
	plays = cmd3+cmd3b
        os.system(plays)

elif "q" or "quit" in question:
	print "\nQuitting now"
	sys.exit(1)       
else:
	print "\nScript Canceled"
        sys.exit()





