#!/usr/bin/env python3


import csv

series = {
'1º Ano': '61', 
'2º Ano': '62', 
'3º Ano': '63', 
'4º Ano': '64', 
'5º Ano': '65', 
'6º Ano': '66', 
'7º Ano': '67', 
'8º Ano': '68', 
'9º Ano': '69', 
'4º Ano - NCM': '76', 
'7º Ano - NJM': '77', 
'Realfabetização 1': '81', 
'Realfabetização 2': '83', 
'Aceleração 1': '84', 
'Aceleração 2A': '87', 
'Aceleração 3': '89', 
'Total': '99', 
'Classe Especial': '0',
'Pré-Escola': '0',
'PEJA I - Bloco 1': '0',
'PEJA I - Bloco 2': '0',
'PEJA II - Bloco 1': '0', 
'PEJA II - Bloco 2': '0', 
'Creche':'0', 
'PIC': '0', 
'PROJOVEM': '0', 
'': '0'
}


# Preenchendo a Tabela Escola

escolaSerie = []
with open('ProfessoresEscola2.csv','r') as f:
	reader = csv.reader(f)
	for row in reader:
		if len(row) == 26:
			for serie in row[23].split("/"):
				b = { 'designacao': row[1], 'serie': series[serie.strip()] }
				escolaSerie.append(b)


for elem in escolaSerie:
	if elem['serie'] != '0':
		print("INSERT INTO EscolaSerie(Codigo,Designacao) VALUES ("+elem['serie']+",'"+elem['designacao']+"'); ")









