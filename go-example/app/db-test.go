// This is a simple program that shows how to use Go to talk
//  to a relational database like MySQL or Postgress-Sql

package main

// Note: Before we can inport, we do the following
//      First, we make a module file that lists dependences
//	     go mod init example/my-module-name

// Now that we have created our go.mod file (using the init command)
//     We now want to add the mysql module as a dependency:
//           go get github.com/go-sql-driver/mysql@latest

//   The @latest tells go that you want to install the most recent version

import (
	"fmt"
	"log"
	"database/sql"
	"net/http"
	"encoding/json"
	"github.com/go-sql-driver/mysql"
       )


//Functions connected to HTTP endpoints should have two inputs
// A  http.ResponseWriter  input
// A *http.Request         input
//     ... the * means that the function takes a pointer to the http.Request
//         this is similar to C where pointers are memory addresses


// This is the "/" endpoint
func hello(writer http.ResponseWriter, req *http.Request){

// The first input to Fprintf indicates where you want to print/write
//    ... We want to print to the HTTP Response
     fmt.Fprintf( writer, "Hello World! ")
}


// This is the "/json" endpoint
func returnJson(writer http.ResponseWriter, req *http.Request){

// The map[string] is the go dictionary interface
//   the string indicates that the keys for the dictionary are strings
// More Info - https://bitfieldconsulting.com/golang/map-string-interface
	
	data := map[string]interface{}{
		"id": 1234,
		"name": "Lepinski",
		"major": "Computer Science",
	}

	jsonData, err := json.Marshal(data)
	if err != nil {
		log.Fatal(err)
	}

	writer.Write(jsonData)	
	
}

// This is the "/test" endpoint
func testDB(writer http.ResponseWriter, req *http.Request){
    // This db variable will be a pointer to our Database Connection
    //    ...this is sometimes called a Database "Handle"
    var db *sql.DB

    // Capture connection properties.
    cfg := mysql.Config{
        User:   "webapp",
        Passwd: "novovoom1web",
        Net:    "tcp",
        Addr:   "db:3306",
        DBName: "NovoVoom",
    }
    // Connect to the MySQL database
    var err error
    db, err = sql.Open("mysql", cfg.FormatDSN())
    if err != nil {
        log.Fatal(err)
    }

    // Ping the database to see if the conneciton is working
    pingErr := db.Ping()
    if pingErr != nil {
        log.Fatal(pingErr)
    }
    fmt.Fprintf(writer, "Connected!")
}

// This is the "/internal/submit" endpoint
func directSubmit(writer http.ResponseWriter, req *http.Request){
	var db *sql.DB

    // Capture connection properties.
	cfg := mysql.Config{
		User:   "webapp",
		Passwd: "novovoom1web",
		Net:    "tcp",
		Addr:   "db:3306",
		DBName: "NovoVoom",
	}
    // Connect to the MySQL database
	var err error
	db, err = sql.Open("mysql", cfg.FormatDSN())
	if err != nil {
		log.Fatal(err)
	}

	//  The FormValue command gives me a value from the form data
	//     that the user submitted
	last_name := req.FormValue("last")
	query := "SELECT first, last, dept, phone FROM Employee WHERE last = '" + last_name + "'"
	
	rows, err := db.Query(query)

	// Loop through the rows
	var output_str string = ""
	for rows.Next() {
		
		var first string
		var last string
		var dept string
		var phone string

		// Note: & is address of a variable
		//       this is similar to C
		rows.Scan(&first, &last, &dept, &phone)
		
		output_str += first + ",   " + last + ",   "
		output_str += dept + ",   " + phone + "\n"
	}

	fmt.Fprintf(writer, output_str)		

}


// This is the "/directory" endpoint
func direct(writer http.ResponseWriter, req *http.Request){
     http.ServeFile(writer, req, "./html/direct_form.html")
}

func main() {
    // This serves up static files form the ./static directory
	fs := http.FileServer(http.Dir("./static"))
	http.Handle("/static/", http.StripPrefix("/static/", fs))

	
    // This connects the functions to the HTTP endpoints
	http.HandleFunc("/", hello)
	http.HandleFunc("/test", testDB)
	http.HandleFunc("/json", returnJson)
	http.HandleFunc("/directory", direct)
	http.HandleFunc("/internal/submit", directSubmit)

    // This tells Go to listen for HTTP on the given port
	http.ListenAndServe(":5555", nil)
}
