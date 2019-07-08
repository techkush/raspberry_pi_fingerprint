var mysql = require('mysql');

var con = mysql.createConnection({
    host: "localhost",
    user: "root",
    password: "",
    database: "sliit_att"
});

con.connect(function (err) {
    if (err) throw err;
    var adr = 'en16504262';
    //Escape the address value:
    var sql = 'SELECT * FROM fo_dd WHERE id = ' + mysql.escape(adr);
    con.query(sql, function (error, result) {

        if(result.length){
            console.log(result);
        }else{
            console.log("Error");
        }
    });
});