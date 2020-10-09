'''
Updates only encrypted passwords to the main server to backup server
'''
import sys
import csv

if len(sys.argv) != 4:
    print("Invalid Arguments \npython3 shadow_generator.py main_server_shadow backup_server_shadow new_shadow")
    exit(0)
print("Old Shadow file : "+sys.argv[1]+
"\nBackup Server Shadow: "+sys.argv[2]+"\nNew file to be generated: "+ sys.argv[3])
old_shadow_dict = dict()
new_shadow_dict = dict() # intially backup server shadow is loaded later its is updated

# list the account which you wanted to skip change of the password
account_to_skip = ['root','emailadmin']

try:
    with open(sys.argv[1], 'r', newline='') as old_shadow_file:
        csv_reader = csv.reader(old_shadow_file,delimiter=':')
        for row in csv_reader:
            old_shadow_dict[row[0]] = row[1]

    with open(sys.argv[2], 'r', newline='') as backup_shadow_file:
        csv_reader = csv.reader(backup_shadow_file,delimiter=':')
        for row in csv_reader:
            if row[0] in account_to_skip:
                print("<Password change skipped:"+row[0])
                continue
            if row[0] in old_shadow_dict.keys():
                if old_shadow_dict[row[0]] != row[1]:
                    row[1] = old_shadow_dict[row[0]]
                    print(">>Password changed:"+row[0])
                else:
                    print(">>>Same as old password:"+row[0])
            else:
                print(">>>>User account not present in main server:"+row[0])

            new_shadow_dict[row[0]] = row

    # check any accounts not present in backup server
    for username in old_shadow_dict.keys():
        if username not in new_shadow_dict.keys():
            print("<<User account not present in backup server:"+username)

    with open(sys.argv[3], 'w') as write_file:
        for username in new_shadow_dict.keys():
            write_file.write(':'.join(new_shadow_dict[username]) + '\n')

    print("\nGenerated")
except:
    print("\n------Error-----\n")
    print(sys.exc_info())