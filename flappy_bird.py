import pygame, sys, random, time
pygame.init()

#initialise window
display = pygame.display.set_mode((500,500))
pygame.display.set_caption("Game")
clock = pygame.time.Clock()
cloned_images = []

# Timer to track intervals
last_clone_time = pygame.time.get_ticks()
clone_interval = 2000 

#get assets
bird = pygame.image.load("assets/bird.png")
pipe = pygame.image.load("assets/pipe.jpg")
bg = pygame.image.load("assets/bg.jpg")

#rescaling
bg = pygame.transform.scale(bg,(500,500))
bird = pygame.transform.scale(bird,(100,70))
pipe = pygame.transform.scale(pipe,(160,250))
pipe2 = pygame.transform.flip(pipe, False, True)

#setting movement for bird
speed=2.5
x=40
y=40

#setting movement for pipes
speed_p = 2.5
x_p = 500
y_p = random.randint(250,350)
x_p2 = 500
y_p2 = random.randint(-250,-50)
y_p2 = y_p-396

#if (y_p+y_p2)!=550:
    #y_p=550-((y_p2)*-1)
    #y_p2=550-y_p
#print(y_p)
#print(y_p2)


#loop
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False
    keys = pygame.key.get_pressed()
    y+=speed
    x_p-=speed_p
    x_p2-=speed_p

    current_time = pygame.time.get_ticks()
    if current_time - last_clone_time >= clone_interval:
        # Clone the image and add to the list
        cloned_images.append(pipe.copy())
        cloned_images.append(pipe2.copy())
        last_clone_time = current_time  


    if keys[pygame.K_SPACE]:
        y=y-6*speed

    if y>=450 or y<=0:
        running = False

   # if x==(x_p-20) and (y>y_p2+50 and y<y_p+50):
        #running = False
    
    display.blit(bg,(0,0))
    display.blit(bird,(x,y))

    display.blit(pipe,(x_p,y_p))
    display.blit(pipe2, (x_p2,y_p2) )   
    
    for i, img in enumerate(cloned_images):
        display.blit(img, (100 + (i * 50), 100))

    pygame.display.flip()
    pygame.time.Clock().tick(60)


print("GAME OVER")
pygame.quit()
sys.exit()
