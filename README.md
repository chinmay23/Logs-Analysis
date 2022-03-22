# Logs-Analysis
It is an internal reporting tool that will use information from the database to discover what kind of articles the site's readers like.
Analysis of logs is done to answer the following three questions:

1 : What are the most popular three articles of all time?

2 : Who are the most popular article authors of all time?

3 : On which days did more than 1% of requests lead to errors?

The database contains newspaper articles, authors of articles as well as the web server log for the site.

We have three tables : articles, authors and log.

The articles table has the list of articles

The authors table has names of authors who have published articles

The log table has list of request sent to the server


We have to first install Virtual Machine and Vagrant on the device.

VirtualBox is the software that actually runs the virtual machine.

Vagrant is the software that configures the VM and lets you share files between your host computer and the VM's filesystem.

Download the VirtualBox from the link below :

https://www.virtualbox.org/wiki/Download_Old_Builds_5_1

Download Vagrant from the link below:

https://www.vagrantup.com/downloads.html

Steps to log in into the VM from command line:

1 : Go to the folder where the Vagrant file is stored 

2 : vagrant up -> vagrant ssh

Now you are logged in to the VM

We need to have the newsdata.sql file from the Udacity downloads section. 

Download the file from the link below:

https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip

Unzip the folder containing file using : unzip newsdata.zip 

The file needs to be in the same folder in which the vagrant file is present

Enter into the vagrant directory : cd /vagrant

By 'ls' you will see the files present in the directory

The vagrant file and newsdata.sql file must be present in this file

To load the data , enter the command: psql -d news -f newsdata.sql

To run the python code it is necessary to have the psycopg2 module

Install it using: pip install psycopg2

Run the python code using: python news.py

The output is displayed on the terminal.
