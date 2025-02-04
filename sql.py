from datetime import datetime
from kafka import KafkaConsumer
import mysql.connector
from mysql.connector import Error

TOPIC = 'toll'
DATABASE = 'tolldata'
USERNAME = 'chinmayi'
PASSWORD = 'chinmayi'

print("Connecting to the database")

connection = None
cursor = None

try:
    connection = mysql.connector.connect(host='localhost',database='tolldata',user='chinmayi',password='chinmayi')
    
    if connection.is_connected():
        print("Connected to database")
        cursor = connection.cursor()
    else:
        print("Failed to connect to the database.")
except Error as e:
    print(f"Error connecting to database: {e}")
    exit(1)  # Exit if unable to connect to the database


