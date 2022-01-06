import pygame
import time

class GUI:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode([800,800])
    def print_board(self):
        board_img = pygame.image.load('assets\\board.png')
        self.screen.blit(board_img, (0,0))
        pygame.display.flip()
    def print_soldiers(self, board):
        for i in range(8):
            for j in range(8):
                soldier_img_path = 'assets\\' + str(board.board[i][j].kind) + str(board.board[i][j].side) + '.png'
                soldier_img = pygame.image.load(soldier_img_path)
                self.screen.blit(soldier_img, (j * 100, i * 100))
                pygame.display.flip()
    def run(self, board):
        self.print_board()
        self.print_soldiers(board)
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            # Flip the display
            pygame.display.flip()
        pygame.quit()
