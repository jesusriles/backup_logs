import os
import shutil
import time

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
	for element in possible_sid:
		print '(' + str(number) + ') ' + element
		number = number + 1

	# select the correct SID
	sid = int(input("SID: "))
	return possible_sid[sid]


# Copy the work directories of ASCS01 and D00
def ABAP_copy_directory():

	sid = select_sid()
	current_date = time.strftime("%d%b%Y") # format example: 03Sep2018

	# backup /usr/sap/<sid>/ASCS01/work
	logs_ascs = '/usr/sap/' + sid + '/ASCS01/work'
	logs_ascs_backup = logs_ascs + '_backup_' + current_date

	if( os.path.isdir(logs_ascs) ):
		try:
			shutil.copytree(logs_ascs, logs_ascs_backup)
		except shutil.Error as e:
			print('Directory not copied. Error: %s' % e)
		except OSError as e:
			print('Directory not copied. Error: %s' % e)

	# backup /usr/sap/<sid>/D00/work
	logs_d00 = '/usr/sap/' + sid + '/D00/work'
	logs_d00_backup = logs_d00 + '_backup_' + current_date

	if( os.path.isdir(logs_d00) ):
		try:
			shutil.copytree(logs_d00, logs_d00_backup)
		except shutil.Error as e:
			print('Directory not copied. Error: %s' % e)
		except OSError as e:
			print('Directory not copied. Error: %s' % e)
# print supported solutions

ABAP_copy_directory()
