import sys, pygame
from time import sleep

def play():
    pygame.mixer.init()
    pygame.mixer.music.load("74.mp3")
    pygame.mixer.music.play(-1)

def lyrics():
    linhas = [
    ("", 1),
    ("Keep it rockin', doin' the same thing", 0.06),
    ("And we get high on the break down", 0.06),
    ("And we're just watching from the same time", 0.06),
    ("But that don't change what I think now", 0.06),
    ("And we were talking 'bout the same crime", 0.06),
    ("No, we don't hide when it rains now", 0.06),
    ("I learned my lesson at the same time", 0.06),
    ("Oooh, where did it all", 0.17), 

    ("Go, back on 74 (when I noticed you)", 0.09),
    ("Call this place my home", 0.08),
    ("Never gonna cry anymore", 0.08),
    ("Where did it all", 0.18), 
    ("            ", 0.01)
    ]

    delays = [1.7, 0.9, 0.9, 0.8, 1.1, 0.8, 0.8, 0.9, 0.5, 1.0, 1.0, 1.4, 1.0, 1.0]
    
    for i, (linha, atraso_caractere) in (enumerate(linhas)):
        for atraso in linha:
            print(atraso, end="")
            sys.stdout.flush()
            sleep(atraso_caractere)
        sleep(delays[i])
        print("")

play()
lyrics()
pygame.mixer.music.stop()