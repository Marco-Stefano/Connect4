class Token():
    def __init__(self, color):
        self.color = color

class Board():
    def __init__(self, maxCols, maxRows):
        self.maxRows = maxRows
        self.maxCols = maxCols
        self.columnsList = []
        for nCol in range(maxCols):
            self.columnsList.append(Column(maxRows))

    def addToken(self, column, color):
        if 0 <= column < self.maxCols
            return self.columnList[column].addToken(color)
        else :
             return None

    def getToken(self, column, row):
        if 0 <= column < self.maxCols :
            return self.columnList[column].getToken(row)
        return None

    def step(self, col, row, direction):
        if direction == "up":
            row = row + 1
        elif direction == "down":
            row = row - 1
        elif direction == "right":
            col = col + 1
        elif direction == "left":
            col = col - 1
        elif direction == "upright":
            row = row + 1
            col = col + 1
        elif direction == "upleft":
            row = row + 1
            col = col - 1
        elif direction == "downright":
            row = row - 1
            col = col + 1
        elif direction == "downleft":
            row = row - 1
            col = col - 1
        return (col, row)

    def countTokens(self, color, col, row, direction):
        n = 0
        col, row = self.step(col, row, direction)
        while self.getToken(col, row) != None and self.getToken(col, row).color == color:
            n = n + 1
            col, row = self.step(col, row, direction)
        return n

    def winningConnection(self, col, row, n):
        if self.getToken(col, row) == None:
            return None
        color = self.getToken(col, row).color
        if countTokens(color, col, row, "up") + countTokens(color, col, row, "down") + 1 >= n :
            return True
        if countTokens(color, col, row, "left") + countTokens(color, col, row, "right") + 1 >= n :
            return True
        if countTokens(color, col, row, "upleft") + countTokens(color, col, row, "downright") + 1 >= n :
            return True
        if countTokens(color, col, row, "upright") + countTokens(color, col, row, "downleft") + 1 >= n :
            return True
        return False

    def isFull(self):
        for col in range(self.maxCols):
            if self.columnsList[col].isFull() == False
                return False
        return True

    def print(self):
        for row in range(self.maxRows):
            print("|", end = "")
            for col in range(self.maxCols):
                if self.getToken(col, row) == None:
                    print("-", end = "")
                else:
                    if self.getToken(col, row).color == "bleu"
                        print("o", end = "")
                    else :
                        print ("x", end = "")
            print("|")

class Column():
    def __init__(self, maxRows):
        self.maxRows = maxRows
        self.tokenList = []

    def addToken(self, color):
        if len(self.tokenList) < self.maxRows:
            self.tokenList.append(Token(color))
            return len(self.tokenList)
        return None

    def getToken(self, n):
        if 0 <= n < len(self.tokenList)
            return self.tokenList[n]
        return None

    def isFull(self):
        return len(self.tokenList) >= maxRows

class Connect4():

    def __init__(self)
        self.board = Board()


    def startGame(self)
        currentPlayer = "bleu"
        ingame = True
        while ingame = True
            self.board.print()
            answer = input("c'est au joueur " + currentPlayer + " de jouer, choisissez une colonne entre 1 et 6")
            col = int(answer) - 1
            row = self.board.addToken(col, currentPlayer)
            if row == None :
                print("impossible d'ajouter le jeton à cette colonne")
            if board.WinningConnection(col, row, currentPlayer):
                ingame = False:
                print(currentPlayer + " a gagné")
            elif board.isFull() == True:
                inGame = False
                print("toutes les colonnes sont pleines, égalité")
            else :
                if currentPlayer == "bleu":
                    currentPlayer = "rouge"
                else :
                    currentPlayer = "rouge"









