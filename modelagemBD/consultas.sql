--1 consulta envolvendo apenas as operações de seleção e projeção;
SELECT CodigoCRE, sum(TotalAprovados)
FROM FrequenciaAprovados
GROUP BY CodigoCRE;

--2  consultas envolvendo a junção de apenas duas relações,sendo que uma deve conter junção externa;
-- cria uma visão com o Nome da escola, o numero de professores e  a sigla de cada disciplina que tem naquela escola
-- create view ResultadoEscola AS SELECT Nome, numeroProfessores, Sigla FROM DisciplinaEscola NATURAL JOIN Escola;
SELECT *
FROM ResultadoEscola;

--usa a visão e pega o nome da Disciplina, o número de professores que ela possui em uma determinada escola, sendo que o número de professores deve ser maior que 10
SELECT Disciplina.Nome, numeroProfessores, ResultadoEscola.nome
FROM ResultadoEscola
LEFT OUTER JOIN Disciplina
ON Disciplina.Sigla = ResultadoEscola.Sigla
WHERE numeroProfessores > 10;

--2 consultas	envolvendo	a	junção	de	três	ou	mais	 relações;
-- selecionar a série mais aprovada em cada CRE -- ERRADO
SELECT PercAprovados, Serie.Descricao, CodigoCRE, TotalAprovados
FROM Serie
NATURAL JOIN FrequenciaAprovados AS FA
INNER JOIN CRE
ON CRE.Codigo = FA.CodigoCRE
WHERE TotalAprovados = some (
SELECT max(TotalAprovados)
FROM FrequenciaAprovados
GROUP BY CodigoCRE);

-- numero de professores em determinada disciplina naquele bairro
SELECT d.Sigla, e.NomeBairro,sum(numeroProfessores) AS NumProf
FROM Disciplina d
NATURAL JOIN DisciplinaEscola de
INNER JOIN Escola e
ON de.Designacao = e.Designacao
NATURAL JOIN QuantBairro2013 q
GROUP BY d.Sigla,e.NomeBairro;

--1 consulta envolvendo uma das operações sobre conjuntos (união, diferença ou intersecção);
-- seleciona os bairros que em 2012 e 2013 tiveram menos de 400 alunos
(SELECT NomeBairro, Total, 2012 AS Ano
   FROM QuantBairro2012
   WHERE Total < 400)
UNION
(SELECT NomeBairro, Total, 2013 AS Ano
   FROM QuantBairro2013
   WHERE Total < 400)
ORDER BY Ano, NomeBairro;

--3 consultas envolvendo funções de agregação;
-- conta o total de aprovados em cada CRE
SELECT codigoCRE,sum(distinct TotalAprovados) AS TotalAprovados
FROM FrequenciaAprovados
GROUP BY CodigoCRE;

-- media de alunos aprovados por serie em cada CRE ( verificar se é isso mesmo haha)
SELECT codigoCRE,avg(distinct TotalAprovados) AS MediaAprovados
FROM FrequenciaAprovados
GROUP BY CodigoCRE;

-- media de professores por disciplina
SELECT  Nome, avg(numeroProfessores) AS MediaProfessores
FROM DisciplinaEscola
NATURAL JOIN Disciplina
GROUP BY Sigla;

--1 consulta envolvendo subconsultas aninhadas.
-- bairros que não possuem escola
SELECT NomeBairro
FROM Bairro
WHERE NomeBairro NOT IN
(SELECT NomeBairro
   FROM Escola);
