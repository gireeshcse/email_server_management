"""
This script generates the passwd file.
This is used to change existing passwd file of new/existing server 
if user home directories are not present in default location.
"""
import csv
email_server_passwd_file = 'email_old/passwd'
file_to_be_generated = 'passwd'

users_file = 'userslist'
dirs_to_check = ['/home/','/home1/']
home_path = '/media/hdd/18042018/home/'
home1_path = '/media/hdd/18042018/home1/'
userslist = list()

# read the users adn add to userslist
with open(users_file, 'r', newline='') as userslist_file:
    for line in userslist_file:
        line = line.strip()
        userslist.append(line)
    #print(userslist)

with open(file_to_be_generated, 'w', newline='') as writefile:
    with open(email_server_passwd_file, 'r', newline='') as readfile:
        csv_reader = csv.reader(readfile,delimiter=':')
        for i,row in enumerate(csv_reader):
            for dir in dirs_to_check:
                if str(row[5]).startswith('/home/') and str(row[5]).strip()!='':
                    if row[0] in userslist:
                        row[5]= home_path + row[0]
                elif str(row[5]).startswith('/home1/') and str(row[5]).strip()!='':
                    if row[0] in userslist:
                        row[5] = home1_path + row[0]

            writefile.write(':'.join(row) + '\n')

print('done')