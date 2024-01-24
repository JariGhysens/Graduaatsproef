import os
import pygame
from .constants import WIDTH, HEIGHT, SQUARE_SIZE, RED, BLUE, WHITE
from .board import Board

ASSETS_PATH = os.path.join(os.path.dirname(__file__), 'assets')

class Game:

    def start_main_screen():
        pygame.init()
        main()


    def __init__(self, win):
        self._init()
        self.win = win
        self.winner_screen = False

    def update(self):
        if self.winner_screen:
            self.draw_winner_screen()
        else:
            self.board.draw(self.win)
            self.draw_valid_moves(self.valid_moves)
            pygame.display.update()

    def draw_winner_screen(self):
        self.win.fill((255, 255, 255))  

        font = pygame.font.SysFont(None, 36)
        winner_color = self.winner()
        if winner_color:
            winner_text = font.render(f"Proficiat {self.translate_color(winner_color)}! Je hebt gewonnen!", True, winner_color)

        else:
            winner_text = font.render("Het is een gelijkspel!", True, (0, 0, 0))
        self.win.blit(winner_text, (WIDTH // 2 - winner_text.get_width() // 2, 50))

        again_button_rect = pygame.Rect(WIDTH // 2 - 75, 190, 150, 50)
        pygame.draw.rect(self.win, (28, 28, 28), again_button_rect)
        again_button_text = font.render("Again", True, (255, 255, 255))
        self.win.blit(again_button_text, (again_button_rect.centerx - again_button_text.get_width() // 2, again_button_rect.centery - again_button_text.get_height() // 2))

        pygame.display.update()

    def translate_color(self, rgb_tuple):
         # Map RGB values to color names
         color_mapping = {(255, 255, 255): 'Wit', (50, 121, 168): 'Blauw'}
         return color_mapping.get(rgb_tuple, rgb_tuple)

    

    def handle_winner_screen_click(self, pos):
        home_button_rect = pygame.Rect(WIDTH // 2 - 75, 120, 150, 50)
        again_button_rect = pygame.Rect(WIDTH // 2 - 75, 190, 150, 50)

        if home_button_rect.collidepoint(pos):
            self.go_to_main_screen()
        elif again_button_rect.collidepoint(pos):
            self.reset()
            self.winner_screen = False  # Set winner_screen to False
            return True
        

    def _init(self):
        self.selected = None
        self.board = Board()
        self.turn = BLUE
        self.valid_moves = {}
        self.winner_screen = False

    def winner(self):
        return self.board.winner()

    def reset(self):
        self._init()

    def select(self, row, col):
        if self.selected:
            result = self._move(row, col)
            if not result:
                self.selected = None
                self.select(row, col)
        
        piece = self.board.get_piece(row, col)
        if piece != 0 and piece.color == self.turn:
            self.selected = piece
            self.valid_moves = self.board.get_valid_moves(piece)
            return True
            
        return False

    def _move(self, row, col):
        piece = self.board.get_piece(row, col)
        if self.selected and piece == 0 and (row, col) in self.valid_moves:
            self.board.move(self.selected, row, col)
            skipped = self.valid_moves[(row, col)]
            if skipped:
                self.board.remove(skipped)
            self.change_turn()
        else:
            return False

        return True


    def handle_winner_screen_click(self, pos):
        home_button_rect = pygame.Rect(WIDTH // 2 - 75, 120, 150, 50)
        again_button_rect = pygame.Rect(WIDTH // 2 - 75, 190, 150, 50)

        if home_button_rect.collidepoint(pos):
          self.go_to_main_screen()
        elif again_button_rect.collidepoint(pos):
          self.reset()
          self.winner_screen = False

    def draw_valid_moves(self, moves):
        for move in moves:
            row, col = move
            pygame.draw.circle(self.win, RED, (col * SQUARE_SIZE + SQUARE_SIZE//2, row * SQUARE_SIZE + SQUARE_SIZE//2), 15)

   
    def change_turn(self):
        self.valid_moves = {}
        if self.winner():
            self.winner_screen = True
        else:
            if self.turn == BLUE:
                self.turn = WHITE
            else:
                self.turn = BLUE

    def handle_winner_screen_click(self, pos):
        home_button_rect = pygame.Rect(WIDTH // 2 - 75, 120, 150, 50)
        again_button_rect = pygame.Rect(WIDTH // 2 - 75, 190, 150, 50)

        if home_button_rect.collidepoint(pos):
            self.go_to_main_screen()
        elif again_button_rect.collidepoint(pos):
            self.reset()
            self.winner_screen = False

    def go_to_main_screen(self):
        self.reset()
        self.winner_screen = False
        start_main_screen()

   