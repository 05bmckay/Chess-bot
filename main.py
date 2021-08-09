from stockfish import Stockfish
import os

import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="""
    Enter your chess move. 
    """)
    parser.add_argument("move", help="The move you want to make example: d2d4")
  

    args = parser.parse_args()

    sys_input = args.move



stockfish = Stockfish(r"stockfish-10-linux/Linux/stockfish_10_x64")

c = open(r"board.txt", "r")

# stockfish.set_fen_position('"'+c.read()+'"')

filesize = os.path.getsize("board.txt")

current_position = []

stockfish.set_fen_position(str(c.read()))

def white_turn():
 
    
    blacks_mover = sys_input

    current_position.append(blacks_mover,)

    stockfish.make_moves_from_current_position([str(sys_input)])

    
    

    

def black_turn():


    
    blacks_best_move = stockfish.get_best_move() # d2d4

    # print(blacks_best_move)
    
    stockfish.make_moves_from_current_position([str(blacks_best_move)])

    

    a = stockfish.get_fen_position()
    print('https://chessboardimage.com/'+a.replace(" ", "%20")+'.png')
    


white_turn()
black_turn()

a = stockfish.get_fen_position()

w = open("board.txt", "w")
w.write(a)
w.close()



