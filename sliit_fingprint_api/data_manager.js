const express = require('express');
const app = express();
const morgan = require('morgan');
const bodyParser = require('body-parser');
var mysql = require('mysql');
//-----------------------------------------------------

//get feedback from client
app.use(morgan('dev'));
app.use(bodyParser.urlencoded({ extended: false }));
app.use(bodyParser.json());

//set configurations with sql database
var con = mysql.createConnection({
    host: 'localhost',
    user: 'root',
    password: '',
    database: 'sliit_att'
});

//post methods
app.post('/', (req, res, next) => {

    var lec_sql = "SELECT * FROM lecturers_info WHERE fing = " + mysql.escape(req.body.fingprint);
    var stu_sql = "SELECT * FROM " + mysql.escape(req.body.subject) + " WHERE id = " + mysql.escape(req.body.fingprint);
    var att_sql = "UPDATE " + mysql.escape(req.body.subject) + " SET " + mysql.escape(req.body.week) + " = 1 WHERE id = " + mysql.escape(req.body.fingprint);

    con.connect(function (err) {
        if (err) throw err;
        if (!!err) {
            console.log("Not Connected! API is not working.");
        } else {
            console.log("Connected! API is working. ");
            //check lecturers
            //{ "method": 1, "fingprint": "123df"}
            if (req.body.method === 1) {
                con.query(lec_sql, function (err, result) {
                    if (err) throw err;
                    if (result.length) {
                        console.log("Send data.");
                        res.status(200).json({
                            message: 1,
                            name: result[0].name
                        });
                    } else {
                        console.log("No data.");
                        res.status(200).json({
                            message: 0
                        });
                    }
                });
            }
            //check students
            //{ "method": 2, "subject": "in_en", "fingprint": "en16504263", "week": "week1"}
            if (req.body.method === 2) {
                con.query(stu_sql, function (err, result) {
                    if (err) throw err;
                    if (result.length) {
                        console.log("Find data.");
                        con.query(att_sql, function (err, result) {
                            if (err) throw err;
                            if (result.length) {
                                console.log("Marked.");
                                res.status(200).json({
                                    message: 1,
                                    id: result[0].id,
                                    name: result[0].name
                                });
                            } else {
                                console.log("Method 2 Error --> 2 .");
                                res.status(200).json({
                                    message: 0
                                });
                            }
                        });
                    } else {
                        console.log("Method 2 Error --> 1 .");
                        res.status(200).json({
                            message: 0
                        });
                    }
                });
            }
            //register
            //{ "method": 3, "id": 1234456, "fingprint": 'gsgs5242524'}
            if (req.body.method === 3) {

            }
        }


    });


    //check lecturer
    if (req.body.method === 1) {

    }
    //check student { "method": 2, "subject": "in_en", "fingprint": "en16504263", "week": "week1"}
    if (req.body.method === 2) {

    }
    //register { "method": 3, "id": 1234456, "fingprint": 'gsgs5242524'}
    if (req.body.method === 3) {

    }
});

//-----------------------------------------------------
//Error Handling.
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
//-----------------------------------------------------