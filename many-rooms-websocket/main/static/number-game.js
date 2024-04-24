// This function is called from within fetchUpdate()
// This function changes the webpage based on the new numbers from the server
// Global Variable to store the websocket object
var socket;

// Global Variable to store the room number and player name
var room_num;
var play_name;


// This function is called when the page loads
function initializeNumbers(){
    // Set the Room Number based on the URL
    var pathArray = location.pathname.split('/');
    play_name = pathArray[3];
    room_num = pathArray[2];
    
    //Open the Websocket when the page loads
    sock_url = "ws://" + location.host + "/openSocket";
    sock_url = sock_url + "/" + room_num + "/" + play_name
    
    console.log(sock_url)
    
    socket = new WebSocket(sock_url);
 
    // Fetch the initial numbers from the server
    fetchUpdate();

    // Fetch a new update whenever the socket receives a message
    socket.onmessage = function(event){
	fetchUpdate();
    }

}


// This function is called periodically to fetch updates from the server
function fetchUpdate() {
    URL = "/getupdate/" + room_num;
    fetch(URL).then( response => response.json()).then( the_json => applyUpdate(the_json) );
}

function applyUpdate(the_json) {
    room_elem = document.getElementById("roomNumber");
    room_elem.innerHTML = room_num;
    
    new_red = the_json['red'];
    new_blue = the_json['blue'];
  
    red_elem = document.getElementById("redText");
    blue_elem = document.getElementById("blueText");
    
    red_elem.innerHTML = new_red;
    blue_elem.innerHTML = new_blue;

    names_elem = document.getElementById("playerNames");
    names_elem.innerHTML = the_json['names']
}


// This function runs when the user requests to change rooms
function leaveRoom(){
    
    // Alert the server that a player has left the room
    URL = "/leaveroom/" + room_num + "/" + play_name;
    fetch(URL).then( response => changeRoom() );
}

function changeRoom(){
    URL = "/requestRoomNum/" + play_name;
    fetch(URL).then( response => response.json()).then( the_json => redirectRoom(the_json) );
}

function redirectRoom(the_json){
    room_number = the_json['num'];

    URL = "/gameRoom/" + room_number + "/" + play_name;

    URL = "http://" + location.host + URL;

    location.href = URL;
}


// The following functions change the numbers when the buttons are clicked
// Each function also notifies the server of the change

function numUpBlue(){
    //First change the number on the screen
    blue_elem = document.getElementById("blueText");
    old_blue = parseInt(   blue_elem.innerHTML   );
    blue_elem.innerHTML = old_blue + 1;

    //Then tell the server about the change
    URL = "/blueUp/" + room_num;
    fetch(URL);
}

function numDownBlue(){
    //First change the number on the screen
    blue_elem = document.getElementById("blueText");
    old_blue = parseInt(   blue_elem.innerHTML   );
    blue_elem.innerHTML = old_blue - 1;

    //Then tell the server about the change
    URL = "/blueDown/" + room_num;
    fetch(URL);
}

function numUpRed(){
    //First change the number on the screen
    red_elem = document.getElementById("redText");
    old_red = parseInt(   red_elem.innerHTML   );
    red_elem.innerHTML = old_red + 1;

    //Then tell the server about the change
    URL = "/redUp/" + room_num;
    fetch(URL);
}

function numDownRed(){
    //First change the number on the screen
    red_elem = document.getElementById("redText");
    old_red = parseInt(   red_elem.innerHTML   );
    red_elem.innerHTML = old_red - 1;

    //Then tell the server about the change
    URL = "/redDown/" + room_num;
    fetch(URL);
}


    
