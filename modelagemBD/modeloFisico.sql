-- Geração de Modelo físico
-- Sql ANSI 2003 - brModelo.



CREATE TABLE Bairro (
NomeBairro varchar(100) PRIMARY KEY,
Latitude float,
Longitude float
);

CREATE TABLE Escola (
Designacao varchar(100) PRIMARY KEY,
Nome varchar(100),
Latitude float,
Longitude float,
NomeBairro varchar(100),
FOREIGN KEY(NomeBairro) REFERENCES Bairro (NomeBairro)
);

CREATE TABLE QtdadeBairro (
Ano year PRIMARY KEY,
NomeBairro varchar(100),
FOREIGN KEY(NomeBairro) REFERENCES Bairro (NomeBairro)
);

CREATE TABLE QtadeAlunosBairro (
Total int
);

CREATE TABLE EscolaDisciplina (
NumProfessores int,
Sigla varchar(25),
Designacao varchar(100),
FOREIGN KEY(Designacao) REFERENCES Escola (Designacao)
);

CREATE TABLE Disciplina (
Nome varchar(100),
Sigla varchar(25) PRIMARY KEY,
Descricao varchar(100)
);

CREATE TABLE EscolaSerie (
CodigoSerie int,
Designacao varchar(100),
FOREIGN KEY(Designacao) REFERENCES Escola (Designacao)
);

CREATE TABLE Telefone (
Telefone int
);

CREATE TABLE FrequenciaAprovacao (
TotalAvaliados int,
TotalAprovados int,
TotalReprovados int,
PercentAprov float,
AnoLetivo year PRIMARY KEY,
PercentFreq float,
CodigoConselho int,
CodigoSerie int
);

CREATE TABLE ConselhoRegionalEducacao (
CodigoConselho int PRIMARY KEY,
NomeInicial varchar(25),
UltimoNome varchar(25),
ImagemSatelite varchar(100)
);

CREATE TABLE Serie (
CodigoSerie int PRIMARY KEY,
Descricao varchar(100)
);

ALTER TABLE EscolaDisciplina ADD FOREIGN KEY(Sigla) REFERENCES Disciplina (Sigla);
ALTER TABLE EscolaSerie ADD FOREIGN KEY(CodigoSerie) REFERENCES Serie (CodigoSerie);
ALTER TABLE FrequenciaAprovacao ADD FOREIGN KEY(CodigoConselho) REFERENCES ConselhoRegionalEducacao (CodigoConselho);
ALTER TABLE FrequenciaAprovacao ADD FOREIGN KEY(CodigoSerie) REFERENCES Serie (CodigoSerie);