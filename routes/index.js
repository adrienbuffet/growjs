var express = require('express');
var router = express.Router();
var fs = require('fs');
var path = require('path');
var core = require('../core.js');

var parameters = JSON.parse(fs.readFileSync(path.join(__dirname, '../', 'parameters.json'), 'UTF-8'));
var plantscount = Object.keys(parameters.plants).length;

/* GET home page. */
router.get('/', function(req, res, next) {
	res.render('index', {
		title: 'GrowJS',
		description: 'Grow your plants, monitor them in real-time and tweak their environment !',
		plantscount: plantscount,
		parameters: parameters		
	});
});

module.exports = router;
