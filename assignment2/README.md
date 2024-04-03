## Goals for Assignments 1 and 2

Here are my goals for assignment 1 and assignment 2:

- Provide a bit more practice with Flask
- Provide a first experience with Docker
- Provide an example of machine-to-machine communication using JSON and an HTTP API
- Provide an experience writing code that is part of a larger project
- Provide an experience integrating code writen by different people
- Provide an opportunity to think critically about the design of APIs used for machine-to-machine communication

With these goals in mind, I am asking you and your colleagues to implement a system with several components that need to interfact with each other.

## Overview of the System

You will be creating a system that allows a human to watch two AI algorithms play Connect Four games against each other.

There are three components of the system:

1. A first AI Player
   
2. A second AI Player
   
3. A web server that manages the games and provides an interface for a human to watch the games

Fortunately, this code has already been written. You wrote Component 1 during previous Assignment. Component 2 was written by some of your colleagues on a different team during the previous Assignment. I (Matt) wrote Component 3 while you were working on the previous Assignment.

You will receive via email the code for Components 2 and 3. You will then integrate this code into a system that satisfies the requirements provided below.

## Assignment Two Requirements

The system that build MUST meet the following requirements:

- You must have three docker containers, one for each of the three components (listed above)
- A human must be able to watch multiple games at once in different tabs. (I put some delays into my web server code which allows the games to play out slowly enough to watch two games at the same time in different tabs.)
- The players in the games must make legal moves and the game must correctly stop when one player wins (or if the board fills and it is a tie).
- The system must be reasonably well-tested and largely free of bugs

The three components were each tested by the authors who writing them. 
Therefore, the code that you are starting with should be mostly correct and free from major bugs. 
(My apologies if you encounter a significant bug. Sadly, I am human, and sometimes we mess up)

In order to integrate the code into a complete system, you will likely need to make some minor edits to some of the code that you are given. 
You are welcome to make the changes you feel are necessary. 
However, I would ask that you please keep the AI strategies/algorithms as similar as possible. 
(That is, don't completely re-write the AI code. Use the AI logic and strategies from the Assignment 1 code. I realize these might not be brilliant AI strategies, but you should utilize them anyway. For example, if you are given code that always makes vertical stacks of pieces to try and win, then the AI player in your system should also be focused on making vertical stacks). 

**Please reach out to me if you have any questions.** 
For the purposes of this project, I am a senior collegue who is contributing code to a sytem that you are working on.

**Every member of your team should turn in a Zip file containing everything that one needs to run your system.** 
I expect that every team member will turn in identical code. 
If there is anything that I should know in order to build and run your system, please put brief instructions in a README file. 

## Reflective Writing

In addittion to 

1. Thinking about the design of the API. What lessons can you take forward to design better APIs in the future

2. Thinking about integrating code written by different people. What should developers do to make integration of the pieces as easy as possible
3. 
