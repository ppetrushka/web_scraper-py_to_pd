#!/usr/bin/env python
#
#
#
#
#

# documentation string of this module
"""
tutorial 01: first blit
"""
# some informational variables
__author__    = "$Author: DR0ID $"
__version__   = "$Revision: 112 $"
__date__      = "$Date: 2007-04-03 18:09:43 +0200 (Di, 03 Apr 2007) $"
__license__   = 'public domain'
__copyright__ = "DR0ID (c) 2007   http://mypage.bluewin.ch/DR0ID"

#----------------------------- actual code --------------------------------

# import the pygame module, so you can use it
import pygame
import socket

# define a main function
def main():
    
    # initialize the pygame module
    pygame.init()
    
    # load and set the logo
    logo = pygame.image.load("logo32x32.png")
    pygame.display.set_icon(logo)
    pygame.display.set_caption("movement")
    
    # create a surface on screen that has the size of 240 x 180
    screen_width = 480
    screen_height = 360
    screen = pygame.display.set_mode((screen_width, screen_height))

    bg_r_value = 128
    bg_g_value = 225
    bg_b_value = 225

    # instead of blitting the background image you could fill it 
    screen.fill((bg_r_value, bg_g_value, bg_b_value))

    # determining the upper and lower limits of the animation
    r_upperlimit = 225
    r_lowerlimit = 128
    g_upperlimit = 255
    g_lowerlimit = 225


    # we will use these steps later to incrementally increase our rgb values. bkz. mainloop
    step_r = 10
    step_g = 10
    step_b = 10
    
    
    # update the screen to make the changes visible (fullscreen update)
    pygame.display.flip()
    
    # a clock for controlling the fps later
    clock = pygame.time.Clock()

    # create a socket which we will use to transmit game information to pure data
    s = socket.socket()
    host = socket.gethostname()
    port = 3000
    
    port2 = 2000
    s2 = socket.socket()
    
    s.connect((host,port))
    s2.connect((host,port2))
    
    # define a variable to control the main loop
    running = True
    # main loop
    while running:
        # event handling, gets all event from the eventqueue
        for event in pygame.event.get():
            # only do something if the event if of type QUIT
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    if r_upperlimit + 10 < 255:
                        r_upperlimit += 10
                        r_lowerlimit += 10
                        g_upperlimit += 10
                        g_lowerlimit += 10
                        print("limits are " + str(r_upperlimit) + "-" + str(r_lowerlimit) + "-" + str(g_upperlimit) + "-" + str(g_lowerlimit))
                    else: 
                        pass
                if event.key == pygame.K_DOWN:
                    if r_upperlimit - 10 > 0:
                        r_upperlimit -= 10
                        r_lowerlimit -= 10
                        g_upperlimit -= 10
                        g_lowerlimit -= 10
                        print("limits are " + str(r_upperlimit) + "-" + str(r_lowerlimit) + "-" + str(g_upperlimit) + "-" + str(g_lowerlimit))
                    else: 
                        pass
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False
            # check for keypress and check if it was Esc
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running = False
                
        # gülçin: by incrementally resetting the alpha value of the smiley blit, i'll attempt to make it "flash"

        if bg_r_value + 10 > r_upperlimit or bg_r_value - 10 < r_lowerlimit :
            step_r = -step_r
        if bg_g_value + 10 > g_upperlimit or bg_g_value - 10 < g_lowerlimit:
            step_g = -step_g
        
        bg_r_value += step_r
        bg_g_value += step_g

        # with each loop, update the red value and send it to the given socket, which was defined earlier

        r_mess = str(bg_r_value)
        r_msg = r_mess + " ;"
        s.send(r_msg.encode('utf-8'))

        g_mess = str(bg_g_value)
        g_msg = g_mess + " ;"
        s2.send(g_msg.encode('utf-8'))
        
        # first erase the screen (just blit the background over anything on screen)
        screen.fill((bg_r_value, bg_g_value, bg_b_value))
        pygame.display.flip() 

        
        # this will slow it down to 10 fps, so you can watch it, 
        # otherwise it would run too fast
        clock.tick(20)
            
# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__=="__main__":
    # call the main function
    main()