// This is a simple Hello World program that demonstrates how easy
//   it is to write HTTP API's in Go

// ... Also, Go uses double-backslash for comments

// All Go files must belong to a package.
//   Executable programs must be in package main
//   ... For a shared library, you can use whatever package name you like

package main

import (
       "fmt"        //package for Printing output
       "net/http"   //package for handling HTTP messages
       )


//Functions connected to HTTP endpoints should have two inputs
// A  http.ResponseWriter  input
// A *http.Request         input
//     ... the * means that the function takes a pointer to the http.Request
//         this is similar to C where pointers are memory addresses

func hello(writer http.ResponseWriter, req *http.Request){

     // Fprintf prints to any type of io.Writer
     //   Our variable writer is of type http.ResponseWriter
     //    and http.ResponseWriter is a type of io.Writer
     
     fmt.Fprintf( writer, "Hello World! ")

}

func main() {

    // This connects the function hello with the HTTP endpoint "/"
	http.HandleFunc("/banana", hello)
	

    
    // This tells Go to listen for HTTP on the given port
	fmt.Printf("Listening on Port :5555")	
	http.ListenAndServe(":5555", nil)
}
