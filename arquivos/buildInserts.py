#!/usr/bin/env python3


import csv


# Preenchendo a Tabela Bairro
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

print("\n\n\n")


# Preenchendo a Tabela Escola

professoresEscola = []
with open('ProfessoresEscola.csv','r') as f:
	reader = csv.reader(f)
	for row in reader:
		if len(row) == 26:
			b = { 'nome': row[0], 'bairro': row[2], 'designacao': row[1], 'latitude': row[24], 'longitude': row[25],

				}
			professoresEscola.append(b)


for profEsc in professoresEscola:
	print("INSERT INTO Escola(Designacao,Nome,Latitude,Longitude,NomeBairro) VALUES (" + 
		"'" + profEsc['designacao'] + "','"
		+ profEsc['nome']+"',"
		+ profEsc['latitude']+","
		+ profEsc['longitude']+",'"
		+ profEsc['bairro']+"');")

print("\n\n\n")

# Preenchendo a Tabela de EscolaDisciplina

disciplina = {
	'Artes Cênicas'      :"AC"     ,
	'Artes Industriais'  :"AI"     ,
	'Artes Plasticas'    :"AP"     ,
	'Ciências'           :"C"      ,
	'Educação Física'    :"EF"     ,
	'Educação Musical'   :"EM"     ,
	'Educação Para O Lar':"EPOL"   ,
	'Espanhol'           :"ES"     ,
	'Francês'            :"FR"     ,
	'Geografia'          :"GEO"    ,
	'História'           :"HIS"    ,
	'Inglês'             :"ING"    ,
	'Língua Portuguesa'  :"LP"     ,
	'Matemática'         :"MAT"    ,
	'Técnicas Agrícolas' :"TECAGRI",
	'Técnicas Comerciais':"TECINF" ,
	'Educação Infantil'  :"EDUINF" ,
	'Ensino Fundamental' :"ENSFUND",
	'Ensino Religioso'   :"ENSREL" ,
	'Professor II'       :"PROF2"  
}

data = []
with open('ProfessoresEscola.csv','r') as f:
	reader = csv.reader(f)
	for row in reader:
		if len(row) == 26:
			data.append(row)

cabe = data[0]
del data[0]

disciplinaEscola = []
for row in data:
	for i in range(3,23):
		if row[i] != '0':
			b = { 'sigla': disciplina[cabe[i]], 'designacao': row[1], 'numeroProfessores': row[i] }
			disciplinaEscola.append(b)

for discEsc in disciplinaEscola:
	print("INSERT INTO EscolaDisciplina(NumProfessores,Sigla,Designacao) VALUES (" +
		discEsc['numeroProfessores'] + ",'" + discEsc['sigla'] + "','" + discEsc['designacao'] + "');")



