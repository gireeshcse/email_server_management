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
