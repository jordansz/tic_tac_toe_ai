# tic-tac-toe
import pygame
import pygame.freetype
from pygame.constants import RESIZABLE, VIDEORESIZE
pygame.init()
pygame.freetype.init()
clock = pygame.time.Clock()

WIDTH, HEIGHT = 750, 750
FPS = 20
win = pygame.display.set_mode((WIDTH, HEIGHT), RESIZABLE)
pygame.display.set_caption("Tic-Tac-Toe")

# board and peices
board_img = pygame.image.load('assets/tic_tac_toe_board.png')
o_p = pygame.image.load('assets/tic_tac_o.png')
x_p = pygame.image.load('assets/tic_tac_o.png')

# font/ text
text1 = "Tic-Tac-Toe"
text_size1 = 72
font1 = pygame.freetype.SysFont('Arial', 72)
# textIntro = font1.render("Tic-Tac-Toe", True, (0, 255, 255))

# font1 = pygame.font.Font(pygame.font.get_default_font(), 72)
# font2 = pygame.font.Font(pygame.font.get_default_font(), 60)
# textIntro = font1.render("Tic-Tac-Toe", True, (0, 255, 255))
# textCharacters = font2.render("Choose Your Character", True, (0, 255, 255))

# pictures
o_img = pygame.image.load('assets/tic_tac_o.png').convert_alpha()
x_img = pygame.image.load('assets/tic_tac_x.png').convert_alpha()
board = pygame.image.load('assets/tic_tac_toe_board.png').convert_alpha()




player1 = ''
player2 = ''
board = {'1' : ' ', '2' : ' ', '3' : ' ', 
        '4' : ' ', '5' : ' ', '6' : ' ',
        '7' : ' ', '8' : ' ', '9' : ' '}

def rescale_window(w, h):
    width_scale = w // WIDTH
    height_scale = h // HEIGHT
    text_scale = min(width_scale, height_scale)
    WIDTH = w
    HEIGHT = h


def get_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        
        if event.type == VIDEORESIZE:
            newW, newH = w, h = pygame.display.get_surface().get_size()
            rescale_window(newW, newH)
        # right mouse button click
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            print("here")
            x, y = pygame.mouse.get_pos()
            return x, y

def intro():
    intro = True

    # text_rec1 = textIntro.get_rect(center = (WIDTH // 2, 100))
    # text_rec2 = textCharacters.get_rect(center = (WIDTH //2, text_rec1[1] + 100))

    # print(text_rec1.bottomleft)
    # print(text_rec2.topleft)
    # print(text_rec2.bottomright)

    # print("testing")
    # print(text_rec1)
    # print("done testing")
    # print("next vals:")
    # print(text_rec2)
    # win.blit(textIntro, text_rec1)
    # win.blit(textCharacters, text_rec2)
    pygame.display.update()
    while intro:
        clock.tick(FPS)
        # x, y = pygame.mouse.get_pos()
        # print(x,y)
        get_events()
        redraw_intro()


def redraw_intro():
    win.fill((0,0,0))
    # text_rec1 = font1.get_rect(text1, size = text_size1)
    # print(text_rec1)
    w, h = pygame.display.get_surface().get_size()
    scaleText1 = min(w, h)
    # scaleText2
    font1.render_to(win, text_rec1, "Tic-Tac-Toe", (0, 255, 255), size = int(72))
    pygame.display.update()


def redraw_window():
    win.blit(board_img, (0, 0))
    pygame.display.update()
    # pass


def checkWin():
    # diagonal check
    if board['7'] == board['5'] and board['7'] == board['3'] and board['7'] != ' ':
        return True
    elif board['7'] == board['5'] and board['7'] == board['3'] and board['7'] != ' ':
        return True
    
    # column check
    if board['7'] == board['4'] and board['7'] == board['1'] and board['7'] != ' ':
        return True
    if board['8'] == board['5'] and board['2'] == board['8'] and board['8'] != ' ':
        return True
    if board['3'] == board['9'] and board['3'] == board['6'] and board['3'] != ' ':
        return True
    
    # row check
    if board['7'] == board['8'] and board['7'] == board['9'] and board['7'] != ' ':
        return True
    if board['4'] == board['5'] and board['4'] == board['6'] and board['4'] != ' ':
        return True
    if board['1'] == board['2'] and board['3'] == board['1'] and board['3'] != ' ':
        return True
    
    return False

def draw():
    print(board['7'] + '|' + board['8'] + '|' + board['9'] + "    7|8|9")
    print("-----    -----")
    print(board['4'] + '|' + board['5'] + '|' + board['6'] + "    4|5|6")
    print("-----    -----")
    print(board['1'] + '|' + board['2'] + '|' + board['3'] + "    1|2|3")
    print("\n")

def revertBoard():
    for key in board:
        board[key] = ' '
    
def validMove(p, val):
    if board[p] == ' ':
        board[p] = val
        return True
    elif int(p) < 1 or int(p) > 9:
        print("Number out of range, choose again.")
    else:
        print("Invalid move, pick another position.")
    draw()
    return False

def main():
    intro()
    global board
    run = True
    clock = pygame.time.Clock()
    # player1 = input("Choose your character, X goes first, O goes second. ")
    # print("\n\n\n")
    # player2 = 'O' if player1 =='X' else 'X'
    # turn = 'X'
    # draw()
    # print("To place an X or an O, input the numbered square you want to move")

    while run:
        redraw_window()
        get_events()
        # for event in pygame.event.get():
        #     if event.type == pygame.QUIT:
        #         run = False
        #         pygame.quit()
        movePos = '0'
        
        valid = False
        # while valid == False:
        #     movePos = input("Player " + turn + ", where would you like to move? ")
        #     valid = validMove(movePos, turn)
        # draw()
        if checkWin():
            print("Player " + turn + " wins!")
            val = input("Would you like to play again? (y/n) ")
            if val == 'y':
                revertBoard()
                draw()
                turn = 'X'
                continue
            else:
                run = False
        # turn = 'X' if turn == 'O' else 'O'
    redraw_window()
    
main()