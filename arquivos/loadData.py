import MySQLdb
import csv

db = MySQLdb.connect('localhost' , 'root' , 'root')
db.select_db('TRABALHO')



bairros = []
aux = []
# open file .csv
with open('alunosPorBairro2012_.csv', 'rb') as f:
    reader = csv.reader(f)
    for row in reader:
		if len(row) == 4:
			b = {'nome': row[0], 'latitude': row[2], 'longitude': row[3]}
			bairros.append(b)
				


# prepare a cursor object using cursor() method
cursor = db.cursor()

# method for insert tuple
add_bairro = ("INSERT INTO Bairro "
              "VALUES (%(nome)s, %(latitude)s, %(longitude)s)")
			  

# execute method add_bairro
for bairro in bairros:
	try:
		# Execute the SQL command
		cursor.execute(add_bairro, bairro)
		# Commit your changes in the database
		db.commit()
	except:
		# Rollback in case there is any error
		db.rollback()

# disconnect from server
db.close()