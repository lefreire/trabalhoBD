#!/usr/bin/env python3


import csv

bairros = []
aux = []

with open('alunosPorBairro2012_.csv', 'r') as f:
	reader = csv.reader(f)
	for row in reader:
		if len(row) == 4:
			b = {'nome': row[0], 'latitude': row[2], 'longitude': row[3]}
			bairros.append(b)
				
for bairro in bairros:
	print("INSERT INTO Bairro VALUES ('" + bairro['nome'] + "',"+ bairro['latitude']+","+bairro['longitude']+");")

