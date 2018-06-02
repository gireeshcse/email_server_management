"""
This is used to copy .mailboxlist which is used by the squirrelmail for each user
which contains the folders created by each user.
"""
import os

# source directory
directory = 'home'

# destination directory This must exist before running the script
destination_directory = '/media/hdd/30012018/'

users_file = directory+'.txt' # $ls /home > home.txt

script_to_be_generated = 'generated_mail_'+directory+'.sh'

with open(users_file,'r') as users:
    with open(script_to_be_generated,'w') as generated:
        for line in users:
            if os.path.isfile('/var/spool/mail/'+str(line).strip()):
                line = str(line).strip()
                # if directory doesnot exist creating directory
                if os.path.isdir(destination_directory +directory+"/"+line) == False:
                    command = 'mkdir '+destination_directory +directory+"/"+line
                    os.system(command)

                generated.write("cp -pv  /"+directory+"/"+line+"/.mailboxlist "+ destination_directory +directory+"/"+line+"/")
        generated.write("\n")