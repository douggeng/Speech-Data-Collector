import mysql.connector
from datetime import date
import string

from password import passwrd


db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd=passwrd,
    database="userdata"
    )
cursor = db.cursor()

tdate = date.today()
ipad = "ipad"
iphone = "iphone"



with open('transcript.txt', 'r') as f:
    for line in f:
        words = line.split()
        table = str.maketrans("", "", string.punctuation)
        stripped = [w.translate(table) for w in words]
        assembled = " ".join(stripped)
        
        if 'ipad' in assembled:
            cursor.execute("INSERT INTO apple (product, date) VALUES (%s, %s)", (ipad, tdate))
            db.commit()
            
        if 'iphone' in assembled:
            cursor.execute("INSERT INTO apple (product, date) VALUES (%s, %s)", (iphone, tdate))
            db.commit()
