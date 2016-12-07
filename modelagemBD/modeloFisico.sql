-- Gera��o de Modelo f�sico
-- Sql ANSI 2003 - brModelo.



CREATE TABLE Bairro (
	NomeBairro VARCHAR(50) PRIMARY KEY,
	Latitude FLOAT,
	Longitude FLOAT
);

CREATE TABLE QuantBairro2013 (
	NomeBairro VARCHAR(50) PRIMARY KEY,
	Total INT,
	FOREIGN KEY(NomeBairro) REFERENCES Bairro (NomeBairro)
);

CREATE TABLE QuantBairro2012 (
	NomeBairro VARCHAR(50) PRIMARY KEY,
	Total INT,
	FOREIGN KEY(NomeBairro) REFERENCES Bairro (NomeBairro)
);

CREATE TABLE CRE (
	Codigo VARCHAR(2) PRIMARY KEY,
	NomeIniciail VARCHAR(20),
	UltimoNome VARCHAR(20),
	imagemSatelite BLOB
);

CREATE TABLE Telefone (
	Codigo_conselho VARCHAR(2),
	Telefone VARCHAR(9),
	PRIMARY KEY(Codigo_conselho,Telefone),
	FOREIGN KEY(Codigo_conselho) REFERENCES CRE (Codigo) ON DELETE CASCADE
);

CREATE TABLE Serie (
	Codigo INT PRIMARY KEY,
	Descricao VARCHAR(20)
);

CREATE TABLE Escola (
	Designacao VARCHAR(10) PRIMARY KEY,
	Nome VARCHAR(70),
	Latitude FLOAT,
	Longitude FLOAT,
	NomeBairro VARCHAR(50),
	FOREIGN KEY(NomeBairro) REFERENCES Bairro (NomeBairro)
);

CREATE TABLE Disciplina (
	Nome VARCHAR(25),
	Sigla VARCHAR(10) PRIMARY KEY,
	Descricao VARCHAR(50)
);

CREATE TABLE DisciplinaEscola (
	numeroProfessores INT,
	Sigla VARCHAR(10),
	Designacao VARCHAR(10),
	PRIMARY KEY(Sigla,Designacao),
	FOREIGN KEY(Sigla) REFERENCES Disciplina (Sigla),
	FOREIGN KEY(Designacao) REFERENCES Escola (Designacao)
);

CREATE TABLE EscolaSerie (
	Codigo INT,
	Designacao VARCHAR(10),
	PRIMARY KEY(Codigo,Designacao),
	FOREIGN KEY(Codigo) REFERENCES Serie (Codigo),
	FOREIGN KEY(Designacao) REFERENCES Escola (Designacao)
);

CREATE TABLE FrequenciaAprovados (
	TotalAvaliados INT,
	TotalAprovados INT,
	TotalReprovados INT,
	PercAprovados FLOAT,
	AnoLetivo INT,
	PercFrequencia FLOAT(2,1),
	Codigo INT,
	CodigoCRE VARCHAR(2),
	PRIMARY KEY(AnoLetivo,Codigo,CodigoCRE),
	FOREIGN KEY(Codigo) REFERENCES Serie (Codigo),
	FOREIGN KEY(CodigoCRE) REFERENCES CRE (Codigo)
);

