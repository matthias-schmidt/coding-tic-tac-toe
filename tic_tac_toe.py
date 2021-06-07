# simplified version without choice of token

# display board

def show(board):
    for line in board:
        print(*line, sep = "|")


# check for win

def check(board, token):
    if len(set(board[k][k] for k in range(3)) | {token}) == 1: return True
    if len(set(board[k][-k-1] for k in range(3)) | {token}) == 1: return True
    for j in range(3):
        if len(set(board[j]) | {token}) == 1: return True
        if len(set(board[k][j] for k in range(3)) | {token}) == 1: return True
    return False


# game

if __name__ == "__main__":

    tokens = ("X", "O")
    eingabe = "j"

    while eingabe != "n":
    
        # create game board
        board = [["_","_","_"],["_","_","_"],[" "," "," "]]
        show(board)

        # play game
        for i in range(0,9):
            
            token = tokens[i%2]

            # input position by present player
            chk = 0
            while chk == 0:
                chk = 1
                eingabe = input(f"Spieler {i%2+1} setzt auf Position x,y: ")
                try: 
                    position = [int(x)-1 for x in eingabe.split(",")]
                    if not 0 <= position[0] <= 2:
                        print('Unzulässige Werte')
                        chk = 0
                        continue
                    if not 0 <= position[1] <= 2:
                        print('Unzulässige Werte')
                        chk = 0
                        continue
                    if board[position[0]][position[1]] not in {"_", " "}:
                        print('Schon besetzt!')
                        chk = 0
                        continue
                except:
                    print('Falsche Eingabe')
                    chk = 0
            
            # put token
            board[position[0]][position[1]] = token  

            # display board in present state
            show(board)

            # check for win 
            if check(board, token):
                print(f"Spieler {i%2+1} hat gewonnen!")
                break

        else:
            print('Unentschieden:)')

        eingabe = input("Neue Runde j/n? ")
        
    print('Ciao!')

