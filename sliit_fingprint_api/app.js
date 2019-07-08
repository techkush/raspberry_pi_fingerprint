const express = require('express');
const app = express();
const morgan = require('morgan');
const bodyParser = require('body-parser');
var mysql = require('mysql');

//get feedback from client
app.use(morgan('dev'));
app.use(bodyParser.urlencoded({ extended: false }));
app.use(bodyParser.json());

var connection = mysql.createConnection({
    host: 'localhost',
    user: 'root',
    password: '',
    database: 'sliit_att'
});

connection.connect(function (error) {
    if (!!error) {
        console.log('Error');
    } else {
        console.log('Connected! Working the program.');
    }
});

app.post('/', (req, res, next) => {

    console.log(req.body);
    //check lecturer
    if (req.body.method === 1) {
        connection.connect(function (err) {
            connection.query("SELECT * FROM lecturers_info WHERE fing =" + connection.escape(req.body.fingprint), function (err, result) {
                if (result.length) {
                    res.status(200).json({
                        message: 1,
                        name: result[0].name
                    });
                } else {
                    res.status(200).json({
                        message: 0,
                    });
                }
            });
        });
    }
    //check student { "method": 2, "subject": "in_en", "fingprint": "en16504263", "week": "week1"}
    if (req.body.method === 2) {
        connection.connect(function (err) {
            connection.query("SELECT * FROM " + req.body.subject + " WHERE fing =" + connection.escape(req.body.fingprint), function (err, result) {
                if (result.length) {
                    connection.query("UPDATE " + req.body.subject + " SET " + req.body.week + " = 1 WHERE fing = " + connection.escape(req.body.fingprint), function (err, result_un) {
                        console.log(result);
                        res.status(200).json({
                            message: 1,
                            id: result[0].id,
                            name: result[0].name
                        });
                    });
                } else {
                    res.status(200).json({
                        message: 0,
                    });
                }
            });
        });
    }
    //register { "method": 3, "id": 1234456, "fingprint": 'gsgs5242524'}
    if (req.body.method === 3) {
        connection.connect(function (err) {
            var subjects = ["fo_dd", "im_mm", "in_en", "po_am"];

            for (i = 0; i < 4; i++) {
                console.log(subjects[i]);
                connection.query("SELECT * FROM " + subjects[i] + " WHERE id =" + connection.escape(req.body.id), function (err, result) {
                    console.log(result);
                    if (result.length) {
                        connection.query("UPDATE " + subjects[i] + " SET fing =" + connection.escape(req.body.fingprint) + " WHERE id =" + connection.escape(req.body.id), function (err, result_un) {
                            console.log(result_un);
                            // res.status(200).json({
                            //     message: 1,
                            //     id: result[0].id,
                            //     name: result[0].name
                            // });
                        });
                    } else {
                        // res.status(200).json({
                        //     message: 0,
                        // });
                    }
                });
            }
        });
    }
});

app.use((req, res, next) => {
    const error = new Error('Not found');
    error.status = 404;
    next(error);
});

app.use((error, req, res, next) => {
    res.status(error.status || 500);
    res.json({
        error: {
            message: error.message
        }
    })
});

module.exports = app;

