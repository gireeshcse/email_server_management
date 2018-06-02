"""
Generates the copy command to copy mail folder of corresponding user
"""
import os

directory = 'home1'
users_file = directory+'.txt' # $ls /home1 > home1.txt
mail_directory = 'mail' # directory to copy which contains all the files related to the mail for corresponding user.

# destination directory This must exist before running the script
destination_directory = '/media/hdd/30012018/'

script_to_be_generated = 'generated_mail_'+directory+'.sh'
with open(users_file,'r') as users:
    with open(script_to_be_generated,'w') as generated:
        for line in users:
            # checks if user contains a file in /var/spool/mail/
            if os.path.isfile('/var/spool/mail/'+str(line).strip()):
                line = str(line).strip()
                # if directory doesnot exist creating directory
                if os.path.isdir(destination_directory +directory+"/"+line) == False:
                    command = 'mkdir '+destination_directory +directory+"/"+line
                    os.system(command)
                generated.write("cp -pvR  /"+directory+"/"+line+"/"+ mail_directory +"  "+ destination_directory+directory+"/"+line+"/")
        generated.write("\n")