import datetime
import fileinput
import sys

# set variables for today's date and yesterday's date in yyyy-mm-dd format
today = str(datetime.date.today())
yesterday = str(datetime.date.today() + datetime.timedelta(days=-1))

# go through todo.txt and replace all instances of yesterday's date with today's date
for line in fileinput.FileInput("/Users/alanj/Dropbox/todo/todo.txt",inplace=1):
   line = line.replace(yesterday,today)
   sys.stdout.write(line)

# to do: add another element to my todo.txt file to record number of days something is overdue, 
# increment that value by 1 each time the replacement above happens.

