td=$(date '+%F')
/Users/alanj/Downloads/todo.txt_cli-2.7/todo.sh add "(A) Review RT queue *$td"
/Users/alanj/Downloads/todo.txt_cli-2.7/todo.sh add "(A) Review Jira queue *$td"
/Users/alanj/Downloads/todo.txt_cli-2.7/todo.sh archive
cp /Users/alanj/Dropbox/todo/todo.txt /Users/alanj/Dropbox/todo/todo.txt.archive
python "/Users/alanj/Documents/Python experiments/todoUpdate/todoUpdate.py"
