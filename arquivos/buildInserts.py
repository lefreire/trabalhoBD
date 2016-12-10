#!/usr/bin/env python3


import csv

# Preenchendo a Tabela Bairro
bairros = []
aux = []

with open('bairros_.csv', 'r') as f:
	reader = csv.reader(f)
	for row in reader:
		b = {'nome': row[0], 'latitude': row[1], 'longitude': row[2]}
		bairros.append(b)
i = 0;

print("INSERT INTO Bairro (NomeBairro,Latitude,Longitude) VALUES ", end="")				
for bairro in bairros:
	print(" ('" + bairro['nome'] + "',"+ bairro['latitude']+","+bairro['longitude']+")",end="")
	if i != len(bairros) - 1:
		print(",", end="")
	else:
		print(";")
	i = i + 1

print("")

print("""INSERT INTO Bairro (NomeBairro,Latitude,Longitude) VALUES  ('Vila Kosmos',-22.8537025,-43.3111508);
INSERT INTO Bairro (NomeBairro,Latitude,Longitude) VALUES  ('Vila Kennedy',-22.8603639,-43.4901816);
INSERT INTO Bairro (NomeBairro,Latitude,Longitude) VALUES  ('Usina',-22.9429299,-43.2541778);
INSERT INTO Bairro (NomeBairro,Latitude,Longitude) VALUES  ('Tubiancaga',-22.7848207,-43.2268643);
INSERT INTO Bairro (NomeBairro,Latitude,Longitude) VALUES  ('Triagem',-22.7848207,-43.2268643);
INSERT INTO Bairro (NomeBairro,Latitude,Longitude) VALUES  ('Tijuca - Andaraí',-22.9290073,-43.2639233);
INSERT INTO Bairro (NomeBairro,Latitude,Longitude) VALUES  ('Tijuca - Comunidade Chacrinha',-22.9290073,-43.2639233);
INSERT INTO Bairro (NomeBairro,Latitude,Longitude) VALUES  ('São Cristovão - Tuiuti',-22.8974819,-43.2334411);
INSERT INTO Bairro (NomeBairro,Latitude,Longitude) VALUES  ('Sulacap',-22.8824732,-43.4121144);
INSERT INTO Bairro (NomeBairro,Latitude,Longitude) VALUES  ('Santa Tereza',-22.9318655,-43.215731);
INSERT INTO Bairro (NomeBairro,Latitude,Longitude) VALUES  ('Santa Teresa - Morro dos Prazeres',-22.9347172,-43.2069109);
INSERT INTO Bairro (NomeBairro,Latitude,Longitude) VALUES  ('S. FERNANDO    SANTA CRUZ',-22.8784771,-43.705992);
INSERT INTO Bairro (NomeBairro,Latitude,Longitude) VALUES  ('RIO DAS PEDRAS - JACAREPAGUÁ',-22.9733701,-43.3319959);""") 


print("\n\n\n")


# Preenchendo a Tabela Escola

professoresEscola = []
with open('ProfessoresEscola2.csv','r') as f:
	reader = csv.reader(f)
	for row in reader:
		if len(row) == 26:
			if row[24] !=  '' and row[25] != '':
				b = { 'nome': row[0], 'bairro': row[2].upper().strip(), 'designacao': row[1], 'latitude': row[24], 'longitude': row[25],

					}
				professoresEscola.append(b)

professoresEscola = sorted(professoresEscola, key=lambda k: k['bairro']) 

for profEsc in professoresEscola:
	if profEsc['bairro'] != '':
		print("INSERT INTO Escola(NomeBairro,Nome,Latitude,Longitude,Designacao) VALUES ",end="")
		print(" (" + "'" + profEsc['bairro'].upper().strip() + "','" + profEsc['nome']+"'," 	+ profEsc['latitude']+","
			+ profEsc['longitude']+",'" + profEsc['designacao']+"')",end="")
		print(";")


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


i = 0
print("INSERT INTO Disciplina(Sigla,Nome,Descricao) VALUES ", end="");
for key in list(disciplina):
	print(" ('"+ disciplina[key] + "','" +key+ "',' ')",end="")
	if i != len(disciplina) - 1:
		print(",", end="")
	else:
		print(";")
	i = i + 1	



print("\n\n\n")

# Preenchendo a Tabela de EscolaDisciplina


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

disciplinaEscola = sorted(disciplinaEscola, key=lambda k: k['sigla']) 			

for discEsc in disciplinaEscola:
	print("INSERT INTO DisciplinaEscola(numeroProfessores,Sigla,Designacao) VALUES ",end="")
	print(" (" + discEsc['numeroProfessores'] + ",'" + discEsc['sigla'] + "','" + discEsc['designacao'] + "')", end="")
	print(";")
	

