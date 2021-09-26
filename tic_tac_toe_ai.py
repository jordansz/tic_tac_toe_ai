# tic-tac-toe
import pygame
import pygame.freetype
import copy
from pygame.constants import RESIZABLE, VIDEORESIZE
pygame.init()
pygame.freetype.init()

WIDTH, HEIGHT = 750, 600
FPS = 20
movePos = '0'
turn = 'X'
gameOver = False
clock = pygame.time.Clock()
win = pygame.display.set_mode((WIDTH, HEIGHT), RESIZABLE)
pygame.display.set_caption("Tic-Tac-Toe")

# pictures
intro_text = pygame.image.load('assets/intro_text.png').convert_alpha()
o_img = pygame.image.load('assets/tic_tac_o.png').convert_alpha()
x_img = pygame.image.load('assets/tic_tac_x.png').convert_alpha()
board_img = pygame.image.load('assets/tic_tac_toe_board.png').convert_alpha()

# used to get the properties of the intro text picture for re-scaling
intro_rec = intro_text.get_rect()
board_rec = board_img.get_rect()
o_img_rec = o_img.get_rect()
x_img_rec = x_img.get_rect()

board_pos_on_screen = [(115, 415), (305, 415), (495, 415), (115, 225), (305, 225), (495, 225), (115, 35), (305, 35), (495, 35)]

# font/text for winner
font = pygame.font.Font(pygame.font.get_default_font(), 90)
font2 = pygame.font.Font(pygame.font.get_default_font(), 60)




player = ''
bot = ''
board = {'1' : ' ', '2' : ' ', '3' : ' ', 
        '4' : ' ', '5' : ' ', '6' : ' ',
        '7' : ' ', '8' : ' ', '9' : ' '}

def get_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        
        if event.type == VIDEORESIZE:
            global WIDTH, HEIGHT, intro_rec, intro_text
            # limit the size the screen can be minimized
            WIDTH, HEIGHT = event.size

            if WIDTH < 750:
                WIDTH = 750
            if HEIGHT < 600:
                HEIGHT = 400

        
            win = pygame.display.set_mode((WIDTH, HEIGHT), RESIZABLE)
            # win.blit(intro_text, (0, 0))
            pygame.display.update()
            return '0'

        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            global player, gameOver
            if player == '':
                global bot
                # wasn't able to the collidepoint function working with o_img_rec/x_img_rec to work properly
                # so made a quick fix
                x_rect = pygame.Rect((WIDTH - (WIDTH // 4) - (x_img_rec.width // 2)), (HEIGHT - x_img_rec.height - 50), x_img_rec.width, x_img_rec.height)
                o_rect = pygame.Rect(((WIDTH // 4) - (o_img_rec.width // 2)), (HEIGHT - o_img_rec.height - 50), o_img_rec.width, o_img_rec.height)
                if o_rect.collidepoint(x, y):
                    player = 'O'
                    bot = 'X'
                elif x_rect.collidepoint(x, y):
                    player = 'X'
                    bot = 'O'
                break   # need break to stop from auto clicking game screen
            elif gameOver:
                # keep_playing_rec = pygame.Rect(85, 350, 590, 95)
                if pygame.Rect(85, 350, 590, 95).collidepoint(x, y):
                    revert_game_state()
                    main()
                elif pygame.Rect(90, 200, 565, 95).collidepoint(x, y):
                    pygame.quit()
                    exit()

            elif player != '':
                global movePos
                count = 1
                for i in board_pos_on_screen:
                    test_rect = pygame.Rect(i[0], i[1], o_img_rec.width, o_img_rec.height)
                    if test_rect.collidepoint(x, y):
                        movePos = str(count)
                        return
                    count += 1
            
                
     


def intro():
    #win.fill((0, 0, 0))
    redraw_intro()
    while player == '':
        # x, y = pygame.mouse.get_pos()
        clock.tick(FPS)
        get_events()
        clock.tick(FPS)

def game_outcome(winner):
    fade_screen = pygame.Surface((WIDTH, HEIGHT))
    fade_screen.fill((0, 0, 0))
    for alpha in range (0, 300):
        fade_screen.set_alpha(alpha)
        draw_board()
        win.blit(fade_screen, (0, 0))
        pygame.display.update()
        pygame.time.delay(5)
    rematch = True
    if winner == "X":
        text = font.render("Player X Wins", 1, (255, 255, 255))
    elif winner == "O":
        text = font.render("Player O Wins", 1, (255, 255, 255))
    else:
        text = font.render("Tie Game!", 1, (255, 255, 255))
    end_game_text = font.render("Stop Playing", 1, (255, 255, 255))
    keep_playing_text = font.render("keep Playing", 1, (255, 255, 255))
    while rematch:
        get_events()
        win.fill((0, 0 ,0))
        text_rec = text.get_rect()
        text_rec2 = end_game_text.get_rect()
        text_rec3 = keep_playing_text.get_rect()
        win.blit(end_game_text, ((WIDTH // 2) - (text_rec2.width // 2), 200))
        win.blit(keep_playing_text, ((WIDTH // 2) - (text_rec2.width // 2), 350))
        win.blit(text, ((WIDTH // 2) - (text_rec.width //2), 40))
        pygame.display.update() 
  

def redraw_intro():
    win.fill((0,0,0))
    # w, h = pygame.display.get_surface().get_size()
    win.blit(intro_text, ((WIDTH // 2) - (intro_rec.width // 2), 20))
    win.blit(o_img, ((WIDTH // 4) - (o_img_rec.width // 2), HEIGHT - o_img_rec.height - 50))
    win.blit(x_img, ((WIDTH - (WIDTH // 4) - (x_img_rec.width // 2), HEIGHT - x_img_rec.height - 50)))
    pygame.display.update()


def checkWin(turn):
    # diagonal check
    if board['7'] == board['5'] and board['7'] == board['3'] and board['7'] == turn:
        return True
    elif board['1'] == board['5'] and board['9'] == board['5'] and board['1'] == turn:
        return True
    
    # column check
    if board['7'] == board['4'] and board['7'] == board['1'] and board['7'] == turn:
        return True
    if board['8'] == board['5'] and board['2'] == board['8'] and board['8'] == turn:
        return True
    if board['3'] == board['9'] and board['3'] == board['6'] and board['3'] == turn:
        return True
    
    # row check
    if board['7'] == board['8'] and board['7'] == board['9'] and board['7'] == turn:
        return True
    if board['4'] == board['5'] and board['4'] == board['6'] and board['4'] == turn:
        return True
    if board['1'] == board['2'] and board['3'] == board['1'] and board['3'] == turn:
        return True
    
    return False


def checkFullBoard(b):
    for val in b.values():
        if val == ' ':
            return False
    return True

def draw():
    print(board['7'] + '|' + board['8'] + '|' + board['9'] + "    7|8|9")
    print("-----    -----")
    print(board['4'] + '|' + board['5'] + '|' + board['6'] + "    4|5|6")
    print("-----    -----")
    print(board['1'] + '|' + board['2'] + '|' + board['3'] + "    1|2|3")
    print("\n")

def revert_game_state():
    global movePos, board, gameOver, player, bot, turn
    gameOver = False
    turn = 'X'
    movePos = '0'
    player = ''
    bot = ''
    for key in board:
        board[key] = ' '
    
def validMove(p, val):
    if movePos not in board:
        return False
    if board[p] == ' ':
        board[p] = val
        return True
    return False


def draw_board():
    win.fill((0,0,0))
    win.blit(board_img, (((WIDTH // 2) - (board_rec.width // 2)), (HEIGHT // 2) - (board_rec.height // 2)))

    for i in range(1, 10):
        if board[str(i)] == 'X':
            win.blit(x_img, board_pos_on_screen[i-1])
        elif board[str(i)] == 'O':
            win.blit(o_img, board_pos_on_screen[i-1])


def evaluate_game_state():
    global gameOver
    if checkFullBoard(board):
        gameOver = True
        game_outcome('Tie')
    if checkWin(turn):
        gameOver = True
        game_outcome(turn)

# def play():
#     global board
#     run = True
#     clock = pygame.time.Clock()
#     count = 0

#     while run:
#         global turn, movePos, gameOver
#         draw_board()
#         get_events()    
#         # if count == 9:
#         #     gameOver = True
#         #     game_outcome('tie')

#         valid = validMove(movePos, turn)
#         if valid:
#             if checkFullBoard(board):
#                 gameOver = True
#                 game_outcome(turn)
#             if checkWin(turn):
#                 gameOver = True
#                 game_outcome(turn)
#             turn = 'X' if turn == 'O' else 'O'
#             count += 1

#         pygame.display.update()
#         clock.tick(FPS)

def play():
    global board
    run = True
    clock = pygame.time.Clock()
    count = 0

    while run:
        global turn, movePos
        draw_board()
        if player == 'X' and turn == 'X':
            get_events()
            valid = validMove(movePos, turn)
            if valid:
                evaluate_game_state()
                turn = 'X' if turn == 'O' else 'O'

        elif player == 'O' and turn == 'O':
            get_events()
            valid = validMove(movePos, turn)
            if valid:
                evaluate_game_state()
                turn = 'X' if turn == 'O' else 'O'

        elif bot == 'O' and turn == 'O':
            print("bots turn")
            bot_move()
            evaluate_game_state()
            turn = 'X' if turn == 'O' else 'O'
        
        elif bot == 'X' and turn == 'X':
            bot_move()
            evaluate_game_state()
            turn = 'X' if turn == 'O' else 'O'
        


        pygame.display.update()
        clock.tick(FPS)


def mini_max(b, depth, is_max):
    if checkWin(player):
        return -1
    if checkWin(bot):
        return 1
    if checkFullBoard(b):
        return 0
    
    if is_max:
        best_score = -1000
        for key in b.keys():
            if b[key] == ' ':
                b[key] = bot
                score = mini_max(b, depth + 1, False)
                b[key] = ' '
                if best_score < score:
                    best_score = score
        return best_score
    
    else:
        best_score = 1000
        for key in b.keys():
            if b[key] == ' ':
                b[key] = player
                score = mini_max(b, depth + 1, True)
                b[key] = ' '
                if best_score > score:
                    best_score = score
        return best_score

def bot_move():
    global board
    b = copy.deepcopy(board)
    best_score = -1000
    best_pos = 0
    for key in b.keys():
        if (b[key] == ' '):
            b[key] = bot
            score = mini_max(b, 0, False)
            b[key] = ' '
            if (score > best_score):
                best_score = score
                best_pos = key

    validMove(best_pos, bot)
    return


def main():
    intro()
    play()
main()

# note to self, re-sizing window messes up board for now, also 
# messing with texts/fonts and trying to scale is not worth it, just use pictures
#dont forget to check on the tie game for text stuff endgame, check gameover variable