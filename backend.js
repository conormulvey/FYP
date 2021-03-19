// JavaScript source code
const express = require('express')
const request = require('request');

app = express();
const PORT = 3000;

app.get('/home', function (req, res) {
    request('http://127.0.0.1:5000/flask', function (error, response, body) {
        console.error('error:', error);
        console.log('statusCode:', response && response.statusCode);
        console.log('body:', body);
        res.send(body);
    });
});

app.listen(PORT, function () {
    console.log('Listening on Port 3000');
});