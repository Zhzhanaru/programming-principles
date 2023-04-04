import pygame

#init 
pygame.init()

#display
screen = pygame.display.set_mode((1280,720))
pygame.display.set_caption("MP3 Player v2.0")
running = True

#clock
clock = pygame.time.Clock()
#music
cnt = 0
song = ['Atack on Titan Opening 2','Backstreet Boys Everybody','Backstreet Boys Shape of my Heart' ,'Night Changes']
mus = ['music\_musics\_atack_on_titan_opening2.mp3','music\_musics\Backstreet_Boys everybody.mp3','music\_musics\Backstreet_Boys_-_Shape_of_My_Heart_.mp3','music\_musics\One Direction - Night Changes.mp3']
#buttons and background
# 'music\_fonts\_backstreet_boys.jpg','music\_fonts\Backstreet.jpg'
background = ['music\_fonts\_atack_on_titan.jpg','music\_fonts\Backstreet.jpg','music\_fonts\_bs.jpg','music\_fonts\_one_direction.jpg']
play_button = pygame.image.load('music\icons\_1pause.png').convert_alpha()
pause_button = pygame.image.load('music\icons\pause.png').convert_alpha()
next_button = pygame.image.load('music\icons\_newnext.png').convert_alpha()
previous_button = pygame.image.load('music\icons\previous.png').convert_alpha()
#text
font = pygame.font.SysFont('Times New Roman',25)
rem = True
mainmenu = True
#program
while running:
    #name of the songs
    x,y = pygame.mouse.get_pos()
    for event in pygame.event.get():
        #quit the program
        if event.type == pygame.QUIT:
            running = False
        #binds     
        elif rem and event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and 560 < x < 760  and 450 < y < 650 :
            mainmenu = False
            rem = False
            pygame.mixer.music.load(mus[cnt])
            pygame.mixer.music.play(0)
            screen.blit(pygame.image.load(background[cnt]).convert(),(0,0))
            screen.blit(font.render(song[cnt],True,(255,255,255)),(500,0))    
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and rem == False and 560 < x < 760  and 450 < y < 650:
                pygame.mixer.music.stop()
                rem = True   
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and 760 <x< 960 and 450<y<650 :
            cnt += 1
            pygame.mixer.music.load(mus[cnt])
            pygame.mixer.music.play(0)
            screen.blit(pygame.image.load(background[cnt]).convert(),(0,0))
            screen.blit(font.render(song[cnt],True,(255,255,255)),(500,0))
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and 360<x<560 and 450<y<650:
            cnt -= 1
            pygame.mixer.music.load(mus[cnt])
            pygame.mixer.music.play(0)
            screen.blit(pygame.image.load(background[cnt]).convert(),(0,0))
            screen.blit(font.render(song[cnt],True,(255,255,255)),(500,0))

    #main screen
    if mainmenu:
        screen.blit(pygame.image.load(background[0]).convert(),(0,0))
     
    if rem:
        screen.blit(pygame.image.load(background[cnt]).convert(),(0,0))
        screen.blit(play_button,(560,450))
    else:
        
        screen.blit(pause_button,(560,450))            
    if cnt == 0:
        screen.blit(next_button,(760,450))
    if cnt == 3:
        screen.blit(previous_button,(360,450))
    if 0 < cnt < 3:
        screen.blit(previous_button,(360,450))
        screen.blit(next_button,(760,450))
                 
    pygame.display.update()       
    #fps
    clock.tick(60)      
              
pygame.quit()