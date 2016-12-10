
var express = require('express');
var router = express.Router();

/* GET home page. */
router.get('/consulta01', function(req, res, next) {
  // res.render('consulta01');
  res.send('Send the answer!');
});

module.exports = router;
