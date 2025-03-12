import pygame, sys, random, time
pygame.init()

#initialise window
display = pygame.display.set_mode((500,500))
pygame.display.set_caption("Game")
clock = pygame.time.Clock()


#get assets
bird = pygame.image.load("assets/bird.png")
pip = pygame.image.load("assets/pipe.jpg")
bg = pygame.image.load("assets/bg.jpg")

#rescaling
bg = pygame.transform.scale(bg,(500,500))
bird = pygame.transform.scale(bird,(100,70))
pipe = pygame.transform.scale(pip,(160,250))

#setting movement for bird
bspeed=2.5
bx=40
by=40


# Pipe settings
PIPE_WIDTH = 70
PIPE_GAP = 80
pipe_speed = 3
pipes = []

class Pipe:
    def __init__(self, x):
        self.x = x
        self.image = pipe
        self.height = random.randint(300, 420)  
        self.top_y = self.height-(PIPE_GAP+350)
        self.bottom_y = self.height
        self.passed = False

    def move(self):
        self.x -= pipe_speed  

    def draw(self):
        display.blit(self.image, (self.x, self.bottom_y)) 
        display.blit(pygame.transform.flip(self.image, False, True), (self.x, self.top_y)) 

# Function to spawn pipes
def spawn_pipe():
    pipes.append(Pipe(500))

#score
score = 0

#spawn pipes
spawn_timer = 0

#loop
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False
    keys = pygame.key.get_pressed()

    # spawning pipes at intervals
    spawn_timer += 1
    if spawn_timer >= 90:  
        spawn_pipe()
        spawn_timer = 0
    
    #fall motion for bird
    by+=bspeed

    #jumping motion for bird
    if keys[pygame.K_SPACE]:
        by=by-4*bspeed
    
    #if bird touches top or botton of window
    if (by>=450 or by<=0):
        running = False

    display.blit(bg,(0,0))
    display.blit(bird,(bx,by))

 
    # Move and draw pipes
    for pi in pipes:
        pi.move()
        pi.draw()
        if pi.x==0:
             pipes.remove(pi)
        if not pi.passed and bx > pi.x + PIPE_WIDTH:  
             pi.passed = True  
             score += 1
        if (bx + 20 > pi.x and bx < pi.x + PIPE_WIDTH) and (by-100 < pi.top_y or by+20 > pi.bottom_y):
             running = False
            
    
    font = pygame.font.Font(None, 36)
    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    display.blit(score_text, (10, 10))

    display.blit(bird,(bx,by))
    pygame.display.flip()
    pygame.time.Clock().tick(60)

with open('score.txt','w+') as file:
        file.write(str(score))
        file.seek(0)

print("GAME OVER")
pygame.quit()
sys.exit()


#-----------------------------------------------------------PREVIOUS_CODE----------------------------------------------------------------
"""
if (y_p+y_p2)!=550:
    y_p=550-((y_p2)*-1)
    y_p2=550-y_p
print(y_p)
print(y_p2)

# Remove off-screen pipes
    #pipes = [pipe for pipe in pipes if pipe.x + PIPE_WIDTH > 0]
"""
