import pygame 
import sys 
 
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load("slow-2021-08-17_-_8_Bit_Nostalgia_-_www.FesliyanStudios.com.mp3")
pygame.mixer.music.play(-1)

effect = pygame.mixer.Sound("gameboy-pluck-41265-[AudioTrimmer.com].wav")



width,height=1200,900

screen=pygame.display.set_mode((width,height))
pygame.display.set_caption("First pygame screen")

#colors
white=(255,255,255)
blue=(0,0,255)
box_size=50
speed=3
clock = pygame.time.Clock()
mazes = [
    [  # Seviye 1 (ilk yaptığımız labirent)
      "  WWWWWWWWWWWWWWWWWW",
    "W       W     W    W",
    "W WWWWW W WWW W WW W",
    "W W   W W   W W W  W",
    "W W W W WWW W W W WW",
    "W   W W     W W   W",
    "WWW W W WWWWW WWWW W",
    "W W W WWW   W W    W",
    "W WWW WWWWW W WW W W",
    "W     W W W W   W  W",
    "W WWWWW W W WWWWW WW",
    "W       W           W",
    "W WWWWWWW WWWWWWWWWWW",
    "W                  GW",  # ← burası çıkış!
    "WWWWWWWWWWWWWWWWWWWW",
    ],

[
    "WWWWWWWWWWWWWWWWWWWW",
    "W                  W",
    "W WWWW WWWW WWWWWW W",
    "W W    W  W W      W",
    "W W WW W  W WWWWWW W",
    "W W W  W    W    WWW",
    "W W WW WWWWWW WW W W",
    "W W    W      W  W W",
    "W WWWWWW WWWW WW W W",
    "W      W W    W  W W",
    "WWWWWW W W WW WWWW W",
    "W      W W W      GW",
    "W WWWWWW W WWWWWWW W",
    "W                W W",
    "WWWWWWWWWWWWWWWWWWWW",
],
[
    "WWWWWWWWWWWWWWWWWWWW",
    "W  W       W W     W",
    "WW W WWWWW W W WWWW",
    "W    W   W   W    W",
    "W WWWW W WWWWWWWW W",
    "W W      W        GW",
    "W W WWW WWWWWWWWW W",
    "W W W   W   W W W W",
    "W W W WWW W W W W W",
    "W   W   W W   W   W",
    "WWWWW W W WWWWW WWW",
    "W     W W       W W",
    "W WWWWW W WWWWWWW W",
    "W                 W",
    "WWWWWWWWWWWWWWWWWWWW",
]

    
]


exit_tile=None
current_level = 0
maze = mazes[current_level]


for row_index,row in enumerate(maze):
    for col_index, cell in enumerate(row):
        if cell=='G':
            exit_tile=(col_index,row_index)

tile_size = 60
player_tile_x, player_tile_y = 1, 1  # labirentteki konum
box_size = 50

def draw_maze(maze,screen):
 for row_index,row in enumerate(maze):
        for col_index,cell in enumerate(row):
            if cell=='W':
                rect=pygame.Rect(col_index*60,row_index*60,60,60)
                pygame.draw.rect(screen,(0,0,0),rect)     
            elif cell=='G':
                rect=pygame.Rect(col_index*60,row_index*60,60,60)
                pygame.draw.rect(screen,(0,255,0),rect)

def handle_movement(player_pos,maze):
    x, y = player_pos

    keys= pygame.key.get_pressed()
    moved=False
    won=False
    
    if keys[pygame.K_RIGHT]:
        if maze[y][x+1]!='W':
            x+=1
            moved=True
    elif keys[pygame.K_LEFT]:
        if maze[y][x-1]!='W':
            x-=1
            moved=True

    elif keys[pygame.K_UP]:
        if maze[y-1][x]!='W':
            y-=1
            moved=True

    elif keys[pygame.K_DOWN]:
        if maze[y+1][x]!='W':
            y+=1
            moved=True
    if maze[y][x]=='G':
        won=True
    
    if moved:
        effect.play()

    return (x,y),won

def check_win(player_pos,maze):
    x, y = player_pos
    if  maze[y][x]== 'G':
        font=pygame.font.SysFont(None,73)
        text=font.render("YOU WON!!",True,(255,0,0))
        text_rect=text.get_rect( center=(width//2,height//2))
        pygame.Rect(text_rect.x-20, text_rect.y-10, text_rect.width+40, text_rect.height+2)
        bg_rect = pygame.Rect(text_rect.x-20, text_rect.y-10, text_rect.width+40, text_rect.height+20)
        pygame.draw.rect(screen,(0,255,0),bg_rect)
        screen.blit(text,text_rect) 
      

    
def event():
    for i in pygame.event.get():
         if i.type== pygame.QUIT:
            pygame.quit()
            sys.exit()

def say_cong(message):
    font=pygame.font.SysFont(None,73)
    text=font.render(message,True,(255,0,0))
    text_rect=text.get_rect(center=(width//2,height//2))
    bg_rect=pygame.Rect(text_rect.x-20,text_rect.y-10,text_rect.width+40,text_rect.height+20)
    pygame.draw.rect(screen, (0, 255, 0), bg_rect)
    screen.blit(text, text_rect)
    pygame.display.update()
    pygame.time.delay(10000)

def draw_visible_area(maze, player_pos, screen):
    x, y = player_pos
    radius = 2
    # Önce G'nin konumunu bul
    exit_x, exit_y = None, None
    for row_index, row in enumerate(maze):
        for col_index, cell in enumerate(row):
            if cell == 'G':
                exit_x, exit_y = col_index, row_index
                break

    for row_index, row in enumerate(maze):
        for col_index, cell in enumerate(row):
            rect = pygame.Rect(col_index * tile_size, row_index * tile_size, tile_size, tile_size)
           
            if cell == 'G':
                pygame.draw.rect(screen, (0, 255, 0), rect)
            elif abs(row_index - y) <= radius and abs(col_index - x) <= radius:
                if cell == 'W':
                    pygame.draw.rect(screen, (0, 0, 0), rect)
                else:
                    pygame.draw.rect(screen, (255, 255, 255), rect) 
            else:
                pygame.draw.rect(screen, (0,0,0), rect) 
won=False


while True:

  


    keys= pygame.key.get_pressed()
    moved=False
    
    player_pos,won= handle_movement((player_tile_x, player_tile_y),mazes[current_level])

    player_tile_x,player_tile_y=player_pos
    

    screen.fill((0,0,0))

    draw_visible_area(mazes[current_level], (player_tile_x, player_tile_y), screen)
    pygame.draw.rect(screen, blue, (player_tile_x * tile_size + 5, player_tile_y * tile_size + 5, box_size, box_size))
    event()
    
    
    if mazes[current_level][player_tile_y][player_tile_x] == 'G':
        current_level += 1
        if current_level >= len(mazes):
            say_cong("Congratulations, you finished the game")
        else:
            player_tile_x, player_tile_y = 1, 1
            screen.fill((0, 0, 0))
            effect.play()
    


    pygame.display.update()
    clock.tick(10)
    