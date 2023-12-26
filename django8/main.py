from MySQLdb import _mysql
host = "localhost"
user = "root"
password = "root"
database = "django.db.backends.mysql"

try:
    # Connect to the MySQL database

    connection = MySQLdb.connect(host='localhost', user='root', passwd='root', db='django.db.backends.mysql')

    # If the connection was successful, print a message
    print("Connected to the MySQL database successfully.")
    connection.close()
except Exception as e:

    print("Error:", e)
