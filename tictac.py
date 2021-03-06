LIMIT = 8

def returnPermutationArray():
  from itertools import permutations
  return list(permutations(range(9)))
  
def inserted( board , pos , value ):
  newboard = board[0:pos] + value + board[pos+1:]
  assert len(newboard) == len(board)
  return newboard
  
def convertToBoard(board, limit):
  newBoard = '---------'
  mark = ['X','O']
  for i in range(limit):
    newBoard = inserted(newBoard,board.index(i),mark[i%2])
  return newBoard

def convertToBoards(board, limit):
  boards = []
  for i in range(limit+1):
    newBoard = convertToBoard(board,i)
    boards.append(newBoard)
  return boards
  
def isRowWin(board):
  assert len(board) == 9
  for i in range(0,9,3):
    if board[i] == board[i+1] == board[i+2] != '-':
      return board[i]
  return False
  
def isColWin(board):
  assert len(board) == 9
  for i in range(3):
    if board[i] == board[i+3] == board[i+6] != '-':
      return board[i]
  return False
  
def isDiaWin(board):
  assert len(board) == 9
  if board[0] == board[4] == board[8] != '-':
    return board[0]
  if board[2] == board[4] == board[6] != '-':
    return board[2]
  return False

def isBoardWin(board):
  return isDiaWin(board) or isRowWin(board) or isColWin(board)
  
def makeBoards():
  database = {}
  perms = returnPermutationArray()
  for perm in perms:
    for board in convertToBoards(perm,LIMIT):
      if isBoardWin(board):
        continue
      database[board] = [9]*9
  return database
  
print(len(makeBoards()))

