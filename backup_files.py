import os
import shutil
import time
import filecmp

# Give to user the possible SID's so user can select the correct SID.
def select_sid():
	possible_sid = []
	number = 0
	print_dir = os.listdir("/usr/sap/")

	# SID's have 3 letters and are upper case.
	for element in print_dir:
		if len(element) == 3 and element.isupper():
			possible_sid.append(element)

	# print number + possible SID
	print("Please select the correct SID of the system:")

	for element in possible_sid:
		print '(' + str(number) + ') ' + element
		number = number + 1

	# select the correct SID
	sid = int(input("SID: "))
	return possible_sid[sid]


# Copy the work directories of ASCS01 and D00
def ABAP_copy_directory(path_to_backup):

	current_date = time.strftime("%d%b%Y") # format example: 03Sep2018
	new_folder_name = path_to_backup + '_backup_' + current_date 
	tmp_new_folder_name = new_folder_name
	number = 1
	new_folder_exist = True

	# check if the provided folder exist
	if( os.path.isdir(path_to_backup) ):
#		print "[+] Path: " + path_to_backup + " does exist."
	else:
		print "[-] Error: " + path_to_backup + " doesn't exist."
		return 0

	# check if the folder to be created exist
	while new_folder_exist:
		if( os.path.isdir(new_folder_name) ):
			new_folder_name = tmp_new_folder_name
			new_folder_name = new_folder_name + '_' + str(number)
			number = number + 1
		else:
			new_folder_exist = False

	# create the backup
	try:
		shutil.copytree(path_to_backup, new_folder_name)
#		print "[+] Backup of: " + path_to_backup + " to: " + new_folder_name
		print "[+] Backup created => " + new_folder_name
	except shutil.Error as e:
		print('Directory not copied. Error: %s' % e)
	except OSError as e:
		print('Directory not copied. Error: %s' % e)

	# verify if the backup was done correctly
	if( filecmp.cmpfiles(path_to_backup, new_folder_name) ):
		print "[+] Verification: backup was done correctly."
	else:
		print "[-] Verification: failed"

# START
sid = select_sid()

# backup /usr/sap/<sid>/ASCS01/work
logs_ascs = '/usr/sap/' + sid + '/ASCS01/work'
ABAP_copy_directory(logs_ascs)

# backup /usr/sap/<sid>/D00/work
logs_d00 = '/usr/sap/' + sid + '/D00/work'
ABAP_copy_directory(logs_d00)
