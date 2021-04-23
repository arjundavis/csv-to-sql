# csv-to-sql
A short python script that adds csv data to an MS SQL table, prompting the user for info. 

To run this, add your csvs to the working directory and run the script. You will be prompted for the filename, please enter this with the extension ".csv"
Then enter the name of the table you wish to append to or enter a new table. 
Finally, you will be prompted for information about the server and database, for more information please see MS SQL documentation.

Pandas will then read the csv and upload it to the specificied table. 

n.b. the MS SQL database is connected to via windows authentication, hence if this is not set up this script will not work. 