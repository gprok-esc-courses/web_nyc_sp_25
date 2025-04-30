import sqlite3 

db = sqlite3.connect('restaurants.db')

db.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL UNIQUE,
                password TEXT,
                role TEXT
            )
           """)

db.execute("""
            CREATE TABLE IF NOT EXISTS owner_requests (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                uners_id INTEGER
            )
           """)

db.execute("""
            CREATE TABLE IF NOT EXISTS cuisines (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT
            )
           """)

db.execute("""
            CREATE TABLE IF NOT EXISTS restaurants (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                description TEXT,
                image TEXT, 
                owner_id INTEGER,
                cuisine_id INTEGER
            )
           """)


db.execute("""
            CREATE TABLE IF NOT EXISTS reviews (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                rate INTEGER,
                comment TEXT,
                user_id INTEGER,
                restaurant_id INTEGER
            )
           """)