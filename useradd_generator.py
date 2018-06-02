"""
This script generates the useradd.sh from /etc/passwd file of the old server.

This is used to generate the user accounts in new server according based on the /etc/passwd file.For more info regarding the file
see important_info file

"""
import csv

# file which is used to create user accounts

email_server_passwd_file = '/etc/passwd'
# passwd may contain some system related account which may be present in the server you may migrate so to avoid those 
# accounts we will aslo check whether corresponding home directories exits are not.Here we are using list 
# because some user accounts may present in some other directory
dirs_to_check = ['/home','/home1']

# user group name create this group in other/migrating server before running the script generated
group_name = 'users'

# we are generating shell script to create accounts.
file_to_be_generated = 'useradd.sh'


with open(file_to_be_generated, 'w', newline='') as writefile:
    with open(email_server_passwd_file, 'r', newline='') as readfile:
        csv_reader = csv.reader(readfile,delimiter=':')
        for i,row in enumerate(csv_reader):
            flag_include = False
            for dir in dirs_to_check:
                # row[5] contains home directory of the user
                if str(row[5]).startswith(dir) and str(row[5]).strip()!='':
                    flag_include = True
                    break

            if flag_include:
                user_info = row[4]
                username = row[0]
                writefile.write('useradd -c "'+user_info+'" -m -G '+ group_name +' '+username+'\n')