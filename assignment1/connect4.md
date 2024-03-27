You are to code an API for the two-player game of Connect Four. 
In essence your API will be providing an AI player that makes moves in Connect Four. 
You need not make intelligent moves, but you must make legal moves.
(Ideally, if you are given a board state where you can win, you should ... but the most important thing is that you make legal moves.)

You can find information about the game at the following links:
- [Wikipedia Page](https://en.wikipedia.org/wiki/Pente)
- [How to Play Document](https://www.wikihow.com/Play-Connect-4)

---

## Board Encoding

The two players are denoted X and O. Player X is the player who moves first. Blank squares are denoted by the dash character \-

The state of the game is encoded as a string with the following format:

  player#board

The components of the game state are as follows:
- **player** is a single character (either X or O) indicating who's turn it is. That is, the next player to move.
- **board** is a string of 42 characters (one for each space of the board) indicating which piece is on each square. Each character should be X, O or dash.
- The first 7 characters represent the first row of the board, the second 7 characters represent the second row, and so forth ...


## API Endpoint - New Game

Your API is essentially implementing a simple AI for the Pente game. You are NOT asked to make good moves, but you must make legal moves.

/newgame/player

Input: **player** is either X or O indicating whether your AI is playing as X or as O

Output is a JSON Object:

  {
  'ID': gameID
  }

The **gameID** should be an integer that can be used to reference a particular game. (Each gameID should be unique)

## API Endpoint - Next Move

/nextmove/gameID/oppCol/state

Input: 
-- **gameID** is the unique ID that was associated with the game when it was created. 
-- **oppCol** is the column in which your opponent most recently placed their piece.
-- **state** is a game state encoded as indicated above. Note that the gamestate must indicate that it is your player's turn to move. (The player that you were assigned when the game was created.)

Your AI player should make a legal move. 
That is, you should identify a column (that is NOT already full) where you would like to place a piece.

Output is a JSON Object:

  {
  'ID': gameID
  'col': myCol
  'state' : new_gamestate
  }

The **gameID** should be the same as was provided in the input

**myCol** should be the column where your AI player is placing a piece.

The **gamestate** should be the new state of the game incorporating your move. This game state should indicate that it is your opponent's turn.

## Submission

Please submit this assignment on Moodle. Everyone on your team should submit identical files. You MUST put a comment at the top of your code file(s) with the names of everyone on your team. 
