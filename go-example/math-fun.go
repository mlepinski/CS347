package main

import (
       "fmt"        //package for Printing output
)

// Return Type goes at the end
func add(x int, y int) int{
	return x + y
}


func main(){
	my_func := add

	//Declare variables x and y
	var x, y int

	x = 2
	y = 3

	// This declares z
	z := 5
	
	ans := my_func(x,y)

	ans = my_func(z,z)
	
	fmt.Println("Hello!")
	fmt.Println( ans )
}

