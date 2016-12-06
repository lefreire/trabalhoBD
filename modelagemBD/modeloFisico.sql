-- Geração de Modelo físico
-- Sql ANSI 2003 - brModelo.



CREATE TABLE Bairro (
	NomeBairro VARCHAR() PRIMARY KEY,
	Latitude FLOAT,
	Longitude FLOAT
)

CREATE TABLE QuantBairro2013 (
	NomeBairro VARCHAR() PRIMARY KEY,
	Total INT,
	FOREIGN KEY(NomeBairro) REFERENCES Bairro (NomeBairro)
)

CREATE TABLE QuantBairro2012 (
	NomeBairro VARCHAR() PRIMARY KEY,
	Total INT,
	FOREIGN KEY(NomeBairro) REFERENCES Bairro (NomeBairro)
)

CREATE TABLE CRE (
	Codigo VARCHAR() PRIMARY KEY,
	NomeIniciail VARCHAR(),
	UltimoNome VARCHAR(),
	imagemSatelite BLOB
)

CREATE TABLE Telefone (
	Codigo_conselho VARCHAR(),
	Telefone VARCHAR(),
	PRIMARY KEY(Codigo_conselho,Telefone),
	FOREIGN KEY(Codigo_conselho) REFERENCES CRE (Codigo) ON DELETE CASCADE
)

CREATE TABLE Serie (
	Codigo INT PRIMARY KEY,
	Descrição VARCHAR()
)

CREATE TABLE Escola (
	Designacao VARCHAR() PRIMARY KEY,
	Nome VARCHAR(),
	Latitude FLOAT,
	Longitude FLOAT,
	NomeBairro VARCHAR(),
	FOREIGN KEY(NomeBairro) REFERENCES Bairro (NomeBairro)
)

CREATE TABLE Disciplina (
	Nome VARCHAR(),
	Sigla VARCHAR() PRIMARY KEY,
	Descricao VARCHAR()
)

CREATE TABLE DisciplinaEscola (
	numeroProfessores INT,
	Sigla VARCHAR(),
	Designacao VARCHAR(),
	PRIMARY KEY(Sigla,Designacao),
	FOREIGN KEY(Sigla) REFERENCES Disciplina (Sigla),
	FOREIGN KEY(Designacao) REFERENCES Escola (Designacao)
)

CREATE TABLE EscolaSerie (
	Codigo INT,
	Designacao VARCHAR(),
	PRIMARY KEY(Codigo,Designacao),
	FOREIGN KEY(Codigo) REFERENCES Serie (Codigo),
	FOREIGN KEY(Designacao) REFERENCES Escola (Designacao)
)

CREATE TABLE FrequenciaAprovados (
	TotalAvaliados INT,
	TotalAprovados INT,
	TotalReprovados INT,
	PercAprovados FLOAT,
	Ano Letivo INT,
	PercFrequencia VARCHAR(),
	Codigo INT,
	CodigoCRE VARCHAR(),
	PRIMARY KEY(Ano Letivo,Codigo,CodigoCRE),
	FOREIGN KEY(Codigo) REFERENCES Serie (Codigo),
	FOREIGN KEY(CodigoCRE) REFERENCES CRE (Codigo)
)

