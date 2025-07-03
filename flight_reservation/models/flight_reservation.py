# from models.payment import Payment

# Task 7: Create Reservation Class
import os
import sys
from mysql.connector.errors import IntegrityError
from datetime import date
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import mysql.connector
class FlightReservation:
    def __init__(self):
        pass

    def reserveFlight(self, username):  # <-- Add 'self' here
        connection = mysql.connector.connect(
            host="localhost",
            user="educative",
            password="secret",
            database="flight"
        )

        if connection.is_connected():
            mycursor = connection.cursor()

            departure = input("Select departure airport (Use 3 letter abbreviation): ")
            arrival = input("Select destination nairport (Use 3 letter abbreviation): ")
            

            query = """
                SELECT flight_no FROM flight
                WHERE arri_port = %s AND dep_port = %s
                LIMIT 1
            """

            mycursor.execute(query, (arrival, departure))
            myresult = mycursor.fetchone()

            if myresult:
                print("Flight number:", myresult[0])
                flightNum = myresult[0]
                    
                while True:
                    bookFlight = input("Would you like to book this flight? (Yes/No): ").strip().lower()
                    if bookFlight in ['yes', 'y']:
                        print("Booking confirmed. Proceeding with reservation...")
                        mycursor = connection.cursor()    
                        insert_query  = """INSERT INTO flightreservation (user_id, flight_no, seats, creation_date, payment_amount)
                                            VALUES (%s, %s, %s, %s, %s)"""
                        
                        mycursor.execute("SELECT account_id FROM account WHERE username = %s", (username,))
                        accID = mycursor.fetchone()
                        today = date.today()
                        data = (accID[0], flightNum, 2, today, 420.00)
                        mycursor.execute(insert_query, data)
                        mycursor.execute("""UPDATE flight SET booked_seats = booked_seats + 1 WHERE flight_no = %s""", (flightNum,))
                        connection.commit()
                        print("Flight number:", myresult[0], " booked, have a safe flight!")
                        return
                    elif bookFlight in ['no', 'n']:
                        print("Understood, Returning to Menu.")
                        return
                    else:
                        print("Please enter 'yes' (y) or 'no' (n) only.")   
            else:
                print("Sorry, we do not have an available flight for this location. Returning to Menu.")
                return
            
    def flightSearch(self, username):
        connection = mysql.connector.connect(
            host="localhost",
            user="educative",
            password="secret",
            database="flight")

        mycursor = connection.cursor()
        mycursor.execute("SELECT account_id FROM account WHERE username = %s", (username,))
        accID = mycursor.fetchone()

        user_id = accID[0]
        searchChoice =  input("Enter 1 to display all flights, enter 2 to search for a flight: ").strip()
        if searchChoice == '1':
            query = "SELECT * FROM flightreservation WHERE user_id = %s"
            mycursor.execute(query, (user_id,))
            user_flights = mycursor.fetchall()

            if not user_flights:
                print(f"No flight reservations found for user: {username}")
            else:
                print(f"{'Reservation':<15}{'User ID':<10}{'Flight No':<10}{'Seats':<6}{'Date':<20}{'Amount':<10}")
                print("-" * 70)
                for flight in user_flights:
                    reservation_number, user_id, flight_no, seats, creation_date, payment_amount = flight
                    print(f"{reservation_number:<15}{user_id:<10}{flight_no:<10}{seats:<6}{creation_date:<20}{payment_amount:<10}")
        elif searchChoice == '2':
                searchFlight = input("Enter the flight number to view: ").strip()
                query = "SELECT reservation_number, user_id, flight_no, seats, creation_date, payment_amount FROM flightreservation WHERE flight_no = %s AND user_id = %s"
                mycursor.execute(query, (searchFlight, user_id))
                flight = mycursor.fetchone()

                if flight is None:
                    print(f"No reservation found for flight {searchFlight}.")
                    return

                reservation_number, user_id_fetched, flight_no, seats, creation_date, payment_amount = flight

                header = f"{'Reservation':<15}{'User ID':<10}{'Flight No':<10}{'Seats':<6}{'Date':<20}{'Amount':<10}"
                print(header)
                print("-" * len(header))
                print(f"{reservation_number:<15}{user_id:<10}{flight_no:<10}{seats:<6}{creation_date:<20}{payment_amount:<10}")
        else: 
            print(searchChoice, "is not an option, please retry with a valid choice.")
            return
        
    def flightRemove(self, username):
        connection = mysql.connector.connect(
            host="localhost",
            user="educative",
            password="secret",
            database="flight")

        mycursor = connection.cursor()
        mycursor.execute("SELECT account_id FROM account WHERE username = %s", (username,))
        accID = mycursor.fetchone()
        user_id = accID[0]
        remFlight = input("Enter the flight number of the reservation you wish to cancel: ")
        
        query = "SELECT 1 FROM flightreservation WHERE flight_no = %s AND user_id = %s"
        mycursor.execute(query, (remFlight, user_id))
        result = mycursor.fetchone()

        if result is None:
            print("User has not booked flight number ", remFlight, " please retry with a valid flight.")
            return

        choice = input("Do you want to cancel this flight?: ").strip().lower()
        if choice in ['no', 'n']:
            print("Understood, returning to main menu")
            return
        elif choice in ['yes', 'y']:
            query = "DELETE FROM flightreservation WHERE flight_no = %s AND user_id = %s"
            mycursor.execute(query, (remFlight, user_id))
            mycursor.execute("""UPDATE flight SET booked_seats = booked_seats - 1 WHERE flight_no = %s""", (remFlight,))
            connection.commit()

            print("Reservation for flight ", remFlight, " has been cancelled.")
        else:
            print("Input error, please try again")
               
    def adminflightadd(self):
        connection = mysql.connector.connect(
            host="localhost",
            user="educative",
            password="secret",
            database="flight")

        mycursor = connection.cursor()
        #mycursor.execute("SELECT account_id FROM account WHERE username = %s", (username,))
        getArri = input("Enter the Destination of the flight (3 initials only): ").strip()
        getDep = input("Enter the location of the flight's departure (3 initials only): ").strip()
        getCode = input("Enter the airline code: ").strip()
        getDist = ("Enter the flight's distance in km: ").strip()
        


    def adminRemove(self):
        connection = mysql.connector.connect(
            host="localhost",
            user="educative",
            password="secret",
            database="flight")

        mycursor = connection.cursor(dictionary=True)
        remFlight = input("Enter the flight number of the reservation you wish to cancel: ")
        
        mycursor.execute("""SELECT airline_code, dep_time, arri_time, dep_port, arri_port, arri_time FROM flight WHERE flight_no = %s""", (remFlight,))
        row = mycursor.fetchone()
        if row is None:
            print("There is no flight with the number  ", remFlight, " please retry with a valid flight.")
            mycursor.close()
            connection.close()
            return

        print(f"\nFound flight {remFlight}:")
        print(f"  Airline Code:    {row['airline_code']}")
        print(f"  Departure Time:    {row['dep_time']}")
        print(f"  Arrival Time:      {row['arri_time']}")
        print(f"  Departure: {row['dep_port']}")
        print(f"  Arrival:   {row['arri_port']}\n")


        choice = input("Do you want to cancel this flight?: ").strip().lower()
        if choice in ['no', 'n']:
            print("Understood, returning to main menu")
            return
        elif choice in ['yes', 'y']:
            query = "DELETE FROM flight WHERE flight_no = %s"
            mycursor.execute(query, (remFlight,))
            connection.commit()

            print("Flight number ", remFlight, " has been cancelled.")
        else:
            print("Input error, please try again")
           