# from models.payment import Payment

# Task 7: Create Reservation Class
import os
import sys
from mysql.connector.errors import IntegrityError
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import mysql.connector
class FlightReservation:
    def __init__(self):
        pass

    def reserveFlight(self):  # <-- Add 'self' here
        connection = mysql.connector.connect(
            host="localhost",
            user="educative",
            password="secret",
            database="flight"
        )

        if connection.is_connected():
            mycursor = connection.cursor()

            print("LOGIN")
            arrival = input("Select airport (Use 3 letter abbreviation): ")
            departure = input("Select destination (Use 3 letter abbreviation): ")

            query = """
                SELECT flight_no FROM flight
                WHERE arri_port = %s AND dep_port = %s
                LIMIT 1
            """

            mycursor.execute(query, (arrival, departure))
            myresult = mycursor.fetchone()

            if myresult:
                print("This flight is available. Flight number:", myresult[0])
            else:
                print("Sorry, we do not have an available flight for this location.")