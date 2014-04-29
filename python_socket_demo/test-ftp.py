"""
it works.
had to reset the buffer position to the beginning of the StringIO file.
csv_file.seek(0) before calling ftp.storbinary did the trick
so csv_file.read() starts at the beginning of the file.

ok i tried and it seems to create the file on the ftp server.
my task is to create a csv file and store it on an ftp server.
the problem im encountering is that the file of the ftp ends up empty.
here is what i tried:
"""

import csv
import StringIO

from ftplib import FTP

csv_file = StringIO.StringIO()
writer = csv.writer(csv_file, lineterminator='\n')
writer.writerow(["FOO", "BAR", "BAZ"])

csv_file.seek(0) 
#so csv_file.read() starts at the beginning of the file.

ftp = FTP('ftp.example.com', 'username', 'password')
ftp.storbinary('STOR test.csv', csv_file)



