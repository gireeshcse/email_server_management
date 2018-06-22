The /etc/passwd is a text file that contains one separate line entry, delimited by a colon (:), 
for each user account configured in the system
Example:

    ram     :  x  :  500  :  500  :  Shri Ram Chandra  :  /home/ram     :  /bin/bash
    |---1---|--2--|---3---|---4---|---------5----------|-------6--------|-----7----|

* **Username** field: This field denotes the User (or User Account) Name.
 According to the man page of useradd command, "Usernames may only be up to 32 characters long". 
 This username must be used at the time of logging in to the system.
* **Password** field: Second field is the Password field, not denoting the actual password though. 
A 'x' in this field denotes the password is encrypted and saved in the /etc/shadow file.
* **UID** field: Whenever a new user account is created, 
it is assigned with a user id or UID (UID for the user 'ram' is 500, in this case) and this field specifies the same.
* **GID** field: Similar to the UID field, this field specifies which group the user belongs to, 
the group details being present in /etc/group file.
* **Comment/Description/User Info** field: This field is the short comment/description/information 
of the user account (For this example, user account 'ram' belongs to the user Shri Ram Chandra, hence this comment).
* **User Home Directory**: Whenever a user logs in to the system, he is taken to his Home directory, 
where all his personal files reside. This field provides the absolute path to the user's home directory (/home/ram in this case).
* **Shell**: This field denotes, the user has access to the shell mentioned in this field
 (user 'ram' has been given access to /bin/bash or simply bash shell).





 ##### Credits

 About etc/passwd file[http://www.yourownlinux.com/2015/07/etc-passwd-file-format-in-linux-explained.html]