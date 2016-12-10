var express      = require('express');
var path         = require('path');
var favicon      = require('serve-favicon');
var logger       = require('morgan');
var cookieParser = require('cookie-parser');
var bodyParser   = require('body-parser');
var mysql        = require('mysql');


// importando os controllers
var index = require('./routes/index');

var app = express();

var connection = mysql.createConnection({
  host     : 'localhost',
  user     : 'root',
  password : 'root',
  database : 'trabTeste'
});

connection.connect();



//connection.end();


// view engine setup
app.set('views', path.join(__dirname, 'views'));
app.set('view engine', 'jade');

// uncomment after placing your favicon in /public
//app.use(favicon(path.join(__dirname, 'public', 'favicon.ico')));
app.use(logger('dev'));
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: false }));
app.use(cookieParser());
app.use(express.static(path.join(__dirname, 'public')));

app.use('/', index);

app.get('/consulta01',function(req,res){ 
	connection.query('SELECT CodigoCRE AS Codigo, sum(TotalAprovados) AS SomaAprovados FROM FrequenciaAprovados GROUP BY CodigoCRE;', function(err, rows, fields) {
  		if (err) throw err;
  		res.render('consulta01', { dados: rows});
	});	 
});

	
app.get('/consulta02',function(req,res){ 
	var query02 = 'SELECT Nome AS NomeEscola, numeroProfessores, Sigla FROM ResultadoEscola;';
	connection.query(query02, function(err, rows, fields) {
		if (err) throw err;
  		res.render('consulta02', { dados: rows});
	});	 
});

app.get('/consulta03',function(req,res){ 
	var query03 = 'SELECT Disciplina.Nome as NomeDisciplina , numeroProfessores, ResultadoEscola.nome as NomeEscola from ResultadoEscola left outer join Disciplina on Disciplina.Sigla = ResultadoEscola.Sigla where numeroProfessores > 10;';
	connection.query(query03, function(err, rows, fields) {
		if (err) throw err;
  		res.render('consulta03', { dados: rows});
	});	 
});

app.get('/consulta04',function(req,res){ 
	var query04 = 'select Serie.Descricao, CodigoCRE,PercAprovados, TotalAprovados from Serie natural join FrequenciaAprovados as FA inner join CRE on CRE.Codigo = FA.CodigoCRE  where TotalAprovados = some (select max(TotalAprovados) from FrequenciaAprovados group by CodigoCRE);';
	connection.query(query04, function(err, rows, fields) {
		if (err) throw err;
  		res.render('consulta04', { dados: rows});
	});	 
});

app.get('/consulta05',function(req,res){ 
	var query05 = 'select d.Sigla, e.NomeBairro,sum(numeroProfessores) AS NumProf from Disciplina d natural join DisciplinaEscola de inner join Escola e on de.Designacao = e.Designacao natural join QuantBairro2013 q group by d.Sigla,e.NomeBairro;';
	connection.query(query05, function(err, rows, fields) {
		if (err) throw err;
  		res.render('consulta05', { dados: rows});
	});	 
});


app.get('/consulta06',function(req,res){ 
	var query06 = '(select NomeBairro, Total, 2012 AS Ano from QuantBairro2012 where Total < 200) union (select NomeBairro, Total, 2013 AS Ano from QuantBairro2013 where Total < 200) order by Ano, NomeBairro;';
	connection.query(query06, function(err, rows, fields) {
		if (err) throw err;
  		res.render('consulta06', { dados: rows});
	});	 
});

app.get('/consulta07',function(req,res){ 
	var query07 = 'select codigoCRE,sum(distinct TotalAprovados) AS TotalAprovados from FrequenciaAprovados group by CodigoCRE;';

	connection.query(query07, function(err, rows, fields) {
		if (err) throw err;
  		res.render('consulta07', { dados: rows} );
	});	 
});

app.get('/consulta08',function(req,res){
	var query08 = 'select codigoCRE,avg(distinct TotalAprovados)  AS MediaAprovados  from FrequenciaAprovados group by CodigoCRE;';

	connection.query(query08, function(err, rows, fields) {
		if (err) throw err;
  		res.render('consulta08', { dados: rows} );
	});	 
});

app.get('/consulta09',function(req,res){
	var query09 = 'select  Nome, avg(numeroProfessores) AS MediaProfessores from DisciplinaEscola natural join Disciplina group by Sigla;';

	connection.query(query09, function(err, rows, fields) {
		if (err) throw err;
  		res.render('consulta09', { dados: rows} );
	});	 
});

app.get('/consulta10',function(req,res){
 res.render('consulta10'); 
});

// catch 404 and forward to error handler
app.use(function(req, res, next) {
  var err = new Error('Not Found');
  err.status = 404;
  next(err);
});

// error handler
app.use(function(err, req, res, next) {
  // set locals, only providing error in development
  res.locals.message = err.message;
  res.locals.error = req.app.get('env') === 'development' ? err : {};

  // render the error page
  res.status(err.status || 500);
  res.render('error');
});

module.exports = app;
