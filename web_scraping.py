import requests
import pygame
import socket
from bs4 import BeautifulSoup

pygame.init()

userinput = input("please enter url:")

continue_ = input("press any key to continue")

r = requests.get(userinput)

print(r)

soup = BeautifulSoup(r.content, 'html.parser')
print(soup.title)
print(soup.title.name)
print(soup.title.parent.name)


def get():
	r = requests.get(userinput)
	print(r)
	# print(r.content)




#running = True

#while running:
    # event handling, gets all event from the eventqueue
 #   for event in pygame.event.get():
        # check for keypress and check if it was Esc
#        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
  #          running = False
 #       else:
 #           get()



