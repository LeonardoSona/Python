from database import Database
from user import User

Database.initialise(database="DBNAME", user="DBUSER", password="DBPASSWORD", host="localhost")

user = User('email@gmail.com', 'Leo', 'Sona', None)

user.save_to_db()

user_from_db = User.load_from_db_by_email('email@gmail.com')

print(user_from_db)