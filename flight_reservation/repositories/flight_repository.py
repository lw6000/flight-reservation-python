# To handle operations related to the Flight database
import mysql.connector
from datetime import datetime, timedelta
from collections import deque
from config.database_config import get_db_connection


class FlightRepository:
    def __init__(self):
        self.connection = get_db_connection()
        self.cursor = self.connection.cursor()

    # Task 4: Define the function to add flight

    # Task 4: Define the function to delete flight

    # Task 4, 11: Find a direct flight

    # Task 4, 12: Find the itineraries

    # Task 4, 13: Define the function to find flights
