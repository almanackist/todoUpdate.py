import datetime
import fileinput
import sys

today = str(datetime.date.today())
yesterday = str(datetime.date.today() + datetime.timedelta(days=-1))

for line in fileinput.FileInput("/Users/alanj/Dropbox/todo/todo.txt",inplace=1):
   line = line.replace(yesterday,today)
   sys.stdout.write(line)


