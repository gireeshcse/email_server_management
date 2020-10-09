 The /etc/shadow file stores actual password in encrypted format (more like the hash of the password) for user’s account with additional properties related to user password. Basically, it stores secure user account information. All fields are separated by a colon (:) symbol. It contains one entry per line for each user listed in /etc/passwd file. 

 Example:


    ram     :  $6$i8KPmhNu.. :  17703  :  0  :  99999  :  7  :   :   :
    |---1---|--2-------------|---3-----|-4---|----5----|-6---| 8 | 9 |


1 - Username
2 - Encrypted Password
3 - Last password change (lastchanged) : Days since Jan 1, 1970 that password was last changed
4 - Minimum : The minimum number of days required between password changes i.e. the number of days left before the user is allowed to change his/her password
5 - Maximum : The maximum number of days the password is valid (after that user is forced to change his/her password)
6 - Warn : The number of days before password is to expire that user is warned that his/her password must be changed
7 - Inactive : The number of days after password expires that account is disabled
8 - Expire : days since Jan 1, 1970 that account is disabled i.e. an absolute date specifying when the login may no longer be used.

To change password aging the command used is **chage**

### Checking integrity of the /etc/passwd and /etc/shadow

Use the **pwck** command verifies the integrity of the users and authentication information. It checks that all entries in /etc/passwd and /etc/shadow have the proper format and contain valid data. The user is prompted to delete entries that are improperly formatted or which have other uncorrectable errors. The syntax is:

```
pwck -r /etc/passwd
pwck -r /etc/shadow
```

The above commands displays the warning and errors.