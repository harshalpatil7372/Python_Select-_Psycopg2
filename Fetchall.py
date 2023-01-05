import psycopg2


#forming the connection

conn = psycopg2.connect(
	database="postgres",#enter your database name
	user='postgres',#enter your postgres username
	password='123456789',#enter your password
	host='localhost',#enter your host name
	port='5432'#port number
)


# Creating a cursor object with cursor() method

cursor = conn.cursor()


cursor.execute("CREATE DATABASE database_name")
conn.commit()



#table creation  using sql command

sql = '''CREATE TABLE articals(
				publisher_id SERIAL PRIMARY KEY,
				publisher_name VARCHAR(255) NOT NULL,
				publisher_estd INT,
				publsiher_location VARCHAR(255),
				publsiher_type VARCHAR(255)
)'''
cursor.execute(sql)
print("Table created successfully")
conn.commit()



#Inserting the data into articals table 

postgres_insert_query = """ INSERT INTO articals(publisher_id,
publisher_name, publisher_estd, publsiher_location, publsiher_type)
VALUES (%s,%s,%s,%s,%s)"""
record_to_insert = [(1, 'Packt', 1950,
						'chennai', 'books'),
						(22, 'Springer', 1950,
						'chennai', 'books'),
						(23, 'Springer', 1950,
						'chennai', 'articles'),
						(54, 'Oxford', 1950,
						'chennai', 'all'),
						(52, 'MIT', 1950,
						'chennai', 'books'),
						(10, 'RCT', 1992,
						'Mumbai', 'all'),
						(6, 'ICT', 1995,
						'Delhi', 'article'),
						(7, 'PICT', 1955,
						'Pune', 'article')
						]
for i in record_to_insert:
		cursor.execute(postgres_insert_query, i)
		conn.commit()
		count = cursor.rowcount
print(count, "Record inserted successfully \
	into publisher table")

# Fetching Data From articals Table

postgreSQL_select_Query = "select * from articals"
cursor.execute(postgreSQL_select_Query)
print("Selecting rows from publisher table using cursor.fetchall")
publisher_records = cursor.fetchall()
print(publisher_records)


postgreSQL_select_Query = "select * from articals where publisher_name LIKE 'S%'"
cursor.execute(postgreSQL_select_Query)
publisher_records = cursor.fetchall()
print(publisher_records)


postgreSQL_select_Query = "select distinct publisher_name from articals"
cursor.execute(postgreSQL_select_Query)
publisher_records = cursor.fetchall()
print(publisher_records)


postgreSQL_select_Query = "select publisher_ID, publisher_name from articals where publisher_locations='Pune'"
cursor.execute(postgreSQL_select_Query)
publisher_records = cursor.fetchall()
print(publisher_records)




# Creating list of fetched records

list_1 = []
for i in publisher_records:
	i = list(i)
	list_1.append(i)
print(list_1)

# check type of list 

print(type(list_1))
conn.close()
