// This function is called from within fetchUpdate()
// This function changes the webpage based on the new numbers from the server
// Global Variable to store the websocket object
var socket;



// This function is called periodically to fetch updates from the server
function fetchUpdate() {
    URL = "/getupdate/";
    fetch(URL).then( response => response.json()).then( the_json => applyUpdate(the_json) );
}

function applyUpdate(the_json) {
    new_red = the_json['red'];
    new_blue = the_json['blue'];
  
    red_elem = document.getElementById("redText");
    blue_elem = document.getElementById("blueText");
    
    red_elem.innerHTML = new_red;
    blue_elem.innerHTML = new_blue;
}

// This function is called when the page loads
function initializeNumbers(){
    // Open the Websocket when the page loads
    socket = new WebSocket("/openSocket");
    
    // Fetch the initial numbers from the server
    fetchUpdate();

    // Fetch a new update whenever the socket receives a message
    socket.onmessage = function(event){
	fetchUpdate();
    }
}


// The following functions change the numbers when the buttons are clicked
// Each function also notifies the server of the change

function numUpBlue(){
    socket.send("Hello World");
    
    //First change the number on the screen
    blue_elem = document.getElementById("blueText");
    old_blue = parseInt(   blue_elem.innerHTML   );
    blue_elem.innerHTML = old_blue + 1;

    //Then tell the server about the change
    URL = "/blueUp/";
    fetch(URL);
}

function numDownBlue(){
    //First change the number on the screen
    blue_elem = document.getElementById("blueText");
    old_blue = parseInt(   blue_elem.innerHTML   );
    blue_elem.innerHTML = old_blue - 1;

    //Then tell the server about the change
    URL = "/blueDown/";
    fetch(URL);
}

function numUpRed(){
    //First change the number on the screen
    red_elem = document.getElementById("redText");
    old_red = parseInt(   red_elem.innerHTML   );
    red_elem.innerHTML = old_red + 1;

    //Then tell the server about the change
    URL = "/redUp/";
    fetch(URL);
}

function numDownRed(){
    //First change the number on the screen
    red_elem = document.getElementById("redText");
    old_red = parseInt(   red_elem.innerHTML   );
    red_elem.innerHTML = old_red - 1;

    //Then tell the server about the change
    URL = "/redDown/";
    fetch(URL);
}


    
