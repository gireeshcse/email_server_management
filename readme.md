# Email Server Management

This project includes the scripts for maintaining the linux email server.

### Migrating accounts from one server to another

use **useradd_generator.py**

This script generates the useradd.sh from /etc/passwd file of the old server.

This is used to generate the user accounts in new server according based on the /etc/passwd file

Use **passwd_generator.py**

This script generates the passwd file.(changes home directories only)
This is used to change existing passwd file of new/existing server 
if user home directories are not present in default location.

Use **shadow_generator.py**

Updates only encrypted passwords to the main server to backup server
Also prints passwords changed and accounts not present in both backup server and main server

```
python3 shadow_generator.py main_server_shadow backup_server_shadow new_shadow

```

use **automate_mail_folder.py**

To only copy the mail folder of each user present in the system 

use **automate_mailboxlist.py**

To copy .mailboxlist which is used by the squirrelmail for each user
which contains the folders created by each user.