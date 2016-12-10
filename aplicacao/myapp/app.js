var express      = require('express');
var path         = require('path');
var favicon      = require('serve-favicon');
var logger       = require('morgan');
var cookieParser = require('cookie-parser');
var bodyParser   = require('body-parser');
var mysql        = require('mysql');


// importando os controllers
var index = require('./routes/index');

var consulta01 = require('./routes/consulta01');

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

app.get('/consulta02',function(req,res){ res.render('consulta02'); });
app.get('/consulta03',function(req,res){ res.render('consulta03'); });
app.get('/consulta04',function(req,res){ res.render('consulta04'); });
app.get('/consulta05',function(req,res){ res.render('consulta05'); });
app.get('/consulta06',function(req,res){ res.render('consulta06'); });
app.get('/consulta07',function(req,res){ res.render('consulta07'); });
app.get('/consulta08',function(req,res){ res.render('consulta08'); });
app.get('/consulta09',function(req,res){ res.render('consulta09'); });
app.get('/consulta10',function(req,res){ res.render('consulta10'); });

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
