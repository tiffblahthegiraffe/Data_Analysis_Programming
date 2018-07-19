# Rock-Paper-Scissors
This is a rock, paper, scissors game that users can interact with computer.

This is a popular game, and you must create a computer player.

Game setup. 

Each game round consists two turns, the first by the computer and the second by a human. The computer continues playing rounds until the human chooses to quit.

 The computer chooses one of Rock, Paper, and Scissors, but keeps its choice secret.
 The computer asks for the human's input.
 The human chooses one of Rock, Paper, and Scissors, or Quit.
 Unless the human quits, the computer figures out the result of thegame, as follows:

   Rock smashes Scissors, so Rock beats Scissors.
   Scissors can cut up paper, so Scissors beat Paper.
   Paper covers Rock, so Paper beats Rock.
    
   If both players chose the same, it is a draw. The computer reports the result of this round.
 If the human chooses to quit, the computer reports:
  the number of games played, and the number of times the human won.


Computer's brains. 

The computer must be able to exploit some human biases. If the human has played Rock most often, the computer should assume that he or she will play Rock in the next round, so the computer
should play Paper. If the human has played Rock and Paper equally often,
and Scissors less often, the computer should assume that the human is going
to play either Rock or Paper (both equally likely) in the next round. (What
should the computer play?)
Hence, your program should remember how many Rock, Paper,
or Scissors were played by the human. Note that we don't need to
remember the order in which the human chooses these; the total counts so
far for each choice will be enough.
Gotchas.
 User input: How you want to receive the user's input is up to you,
but you must check the user's input to make sure it is valid (you can
assume that the user input is of the correct type). If it isn't, request
the user for input again.
