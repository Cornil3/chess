from gui import GUI
from soldier import Soldier, Board
import pygame

def main():
    board = Board()
    GUI().run(board)
    print("hi")

if __name__ == '__main__':
    main()