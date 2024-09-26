# zimbra-tools

This repository contains two files -
- The Python script ```ga.py```
- A sample CSV output file ```output_columns.csv```

## What does it do?

It fetches all the user accounts email IDs along with their user names and dumps then in a CSV file.

## Instructions

- Zimbra should be installed on the system
- Change to the zimbra user account by performing the following steps in shell
    - Enter - ```sudo su``` and enter root password to escalate the shell to root user
    - ```su - zimbra``` to change shell to zimbra user 
- Run the script by ```python3 ga.py```

## Troubleshoot

If through the zimbra user you are unable to create the CSV then create the file manually either from root or another account and use the following commands in the same directory where the script is located -
- ```touch output_columns.csv```
- ```chown zimbra output_columns.csv```