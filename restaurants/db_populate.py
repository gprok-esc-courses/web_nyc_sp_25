import sqlite3

db = sqlite3.connect('restaurants.db')

# Add users
db.execute("INSERT INTO users (username, password, role) VALUES ('admin', '1234', 'admin')")
db.execute("INSERT INTO users (username, password, role) VALUES ('john', '1111', 'owner')")
db.execute("INSERT INTO users (username, password, role) VALUES ('mary', '1111', 'owner')")
db.execute("INSERT INTO users (username, password, role) VALUES ('tom', '1111', 'owner')")
db.execute("INSERT INTO users (username, password, role) VALUES ('ann', '2222', 'guest')")
db.execute("INSERT INTO users (username, password, role) VALUES ('james', '2222', 'guest')")
db.execute("INSERT INTO users (username, password, role) VALUES ('jenn', '2222', 'guest')")

# Add cuisines
db.execute("INSERT INTO cuisines (name) VALUES ('Lebanese')")
db.execute("INSERT INTO cuisines (name) VALUES ('Mexican')")
db.execute("INSERT INTO cuisines (name) VALUES ('Chinese')")
db.execute("INSERT INTO cuisines (name) VALUES ('Italian')")
db.execute("INSERT INTO cuisines (name) VALUES ('Steak House')")

# Add restaurants
db.execute("""INSERT INTO restaurants (name, description, image, owner_id, cuisine_id) 
           VALUES ('Falafel', 'Orifinal middle east flavors', 'falafel.jpg', 2, 1)""")
db.execute("""INSERT INTO restaurants (name, description, image, owner_id, cuisine_id) 
           VALUES ('Texan Meat', 'Burgers etc', 'texan.jpg', 2, 5)""")
db.execute("""INSERT INTO restaurants (name, description, image, owner_id, cuisine_id) 
           VALUES ('Cantina', 'Flavors from central and south America', 'cantina.jpg', 3, 2)""")
db.execute("""INSERT INTO restaurants (name, description, image, owner_id, cuisine_id) 
           VALUES ('Chef Lee', 'Chinese and Asian recipes', 'lee.jpg', 4, 3)""")

db.commit()