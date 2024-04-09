"""
MAX(x): aims to maximize the score
MIN(O) : Aims to minimize the score,

There are three chances that can occur, 
1. X win: Lets say if score value is -1
2. No Win: if values is Zero
3. O wins : if score value is One.

Psuedo Code
1. So: Initial State
2. Player(s) : returns which player to move in state s
3. Actions(s) : returns legal moves in state s
4. Result(s, a): returns state after actions a taken in state s
5. Terminal(s): Checks if state s is a terminal state
"""
"""
* GIven a state s:
    *Max picks action a in the Action(s) that produces 
    Highest value of the MIN-values(result(s, a))
    * MIN picks action a in Actions(s) that produces smallest
    value of MAX-VALUE(Result(s,a))
"""
"""
Peducode for Minimax Algorithms
function minimax(board, depth, maximizingPlayer)
    if game_over(board) or depth == 0
        return evaluate(board)
    
    if maximizingPlayer
        maxEval = -infinity
        for each empty_cell in board
            board[empty_cell] = maximizingPlayer's symbol
            eval = minimax(board, depth - 1, FALSE)
            maxEval = max(maxEval, eval)
            board[empty_cell] = empty
        return maxEval
    else
        minEval = +infinity
        for each empty_cell in board
            board[empty_cell] = other_player's symbol
            eval = minimax(board, depth - 1, TRUE)
            minEval = min(minEval, eval)
            board[empty_cell] = empty
        return minEval

# Initial call for maximizing player
minimax(board, depth, TRUE)

"""


