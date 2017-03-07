# This program plays a game. The game is basically an aim and shooter, where you aim a piece of garbage at a garbage can, and try to get a highscore by getting consecutive garbage into the garbage can.
# Written by Rohan Gupta.

# Needed to import all the pygame functions and run the pygame engine.
from pygame import *
init()

# Sets constants for the colours that will be used later in the program.
RED = (255, 0, 0)
BLACK = (0, 0, 0)
GREEN = (0, 102, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)

# Used to store the highscore. A text document is used in order to store the highscore.
score = 0
scorepage = open("Scores.txt", "r")
Highscore = int(scorepage.readline())
scorepage.close()

# Sets the width and height of the screen.
width = 600
height = 600

# Makes the size of the screen.
SIZE = (width, height)
screen = display.set_mode(SIZE)

# Initializes the value of the boolean variables used in the program.
throwing = False
collecting = False
running = True
playing = False
showMe = False
HowPage = False

# Sets the size of the two buttons on the main menu.
rectPlay = Rect(width/4, height/4, width/2, height/6)
rectMiddle  = Rect(width/4, height/2, width/2, height/6)
rectQuit = Rect(width/4, height/(4/3), width/2, height/6) 

# Initializes the position of the garbage and garbage can.
mx,my = 0,0
trashx,trashy = 300,550

# Sets a value for the speed at which the garbage gets released.
xforce = 0
yforce = 7

# Initializes the value of boolean expressions for the piece of garbage.
goup = True
godown = False

# Initializes the value of boolean expressions for the garbage can.
canLeft = True
canRight = False
canx,cany = 300,200
canSpeed = 1

# Sets the limit of how far up the screen the ball will go to.
ballLimit = 100

# Creates a rectange around the garbage and garbage can so that collisions can be taken into account.
trashRect = Rect(canx,cany,124,167)
ballRect = Rect(trashx,trashy,80,90)

# Sets another value for a boolean expression for returning to the menu.
endMenu = False

# Defines the screen when start is clicked.
def start():
  draw.rect(screen, GREEN, (0, 0, width, height))
  
# A definition that is the screen of the "How to Play" menu
def howPage():
  how = image.load("Instructions.png")
  screen.blit(how, (0,0,100,100))
       
# Loads up the image of the piece of garbage.
def garbage(x, y):
  page = image.load("Garbage 3.png")
  screen.blit(page, (x,y,100,100)) 

# Loads up the image of the garbage can.
def garbagecan(x,y):
  garbagecan = image.load("GarbageCan.png")
  screen.blit(garbagecan, (x,y,100,100))

# Loads up the image of the background used on the main menu.
def MenuDraw():
    home = image.load("Cropped Home 2.png")
    screen.blit(home, (0,0,100,100)) 
    
    # Determines the font and colour of the text of the title on the main menu.
    fontTitle = font.SysFont("Comic Sans MS", width//16)	
    titleText = fontTitle.render("Garbage Shooter", 1, GREEN)
    titleSize = fontTitle.size("Garbage Shooter")
  
    # The font and colour of the text of the buttons on the main menu.
    fontMenu = font.SysFont("Comic Sans MS", width//15)	
    menuText1 = fontMenu.render("Start Program", 1, WHITE)
    menuText2 = fontMenu.render("How to Play", 1, WHITE)
    menuText3 = fontMenu.render("Exit Game", 1, WHITE)
    text1Size = fontMenu.size("Start Program")
    text2Size = fontMenu.size("How to Play")
    text3Size = fontMenu.size("Exit Game")
    
    # This determines the position of each of the buttons on the main menu.
    startRect = Rect(width/4, height/4, width/2, height/6)
    howRect  = Rect(width/4, height/2, width/2, height/6)
    exitRect = Rect(width/4, height/(4/3), width/2, height/6) 
    
    # Determines the colour of the background for the main menu buttons.
    colMenu1 = GREEN
    colMenu2 = GREEN
    colMenu3 = GREEN   
    
    # This draws all the menu options.  
    screen.blit(titleText, (width/2 - titleSize[0]/2, height/10 - titleSize[1]/2, titleSize[0], titleSize[1]))
    draw.rect(screen, colMenu1, startRect)
    screen.blit(menuText1, (width/2 - text1Size[0]/2, height/4 + height/10 - text1Size[1]/2, text1Size[0], text1Size[1]))
    draw.rect(screen, colMenu2, howRect)
    screen.blit(menuText2, (width/2 - text2Size[0]/2, height/2 + height/10 - text2Size[1]/2, text1Size[0], text1Size[1]))
    draw.rect(screen, colMenu3, exitRect)
    screen.blit(menuText3, (width/2 - text3Size[0]/2, height/(4/3) + height/10 - text3Size[1]/2, text1Size[0], text1Size[1]))   

# Needed to initialize the variable type for time.
myClock = time.Clock()

# A loop is created that keeps on going until the program is stopped.
while running:
  # Initializing score because when the user starts to play the game, the score is 0.
  score = 0
  # Draws the main menu and displays it.
  MenuDraw()
  display.flip()    
  # This loop checks for any events occuring in the program.  
  for evt in event.get():
    # If "Quit" is clicked, then the program will stop running.
    if evt.type == QUIT:
      running = False
    # This tracks the mouse movements.
    if evt.type == MOUSEBUTTONDOWN: 
      mx,my = evt.pos
    # This takes into account if the mouse clicked falls into any of the menu options. If "Play" is selected, then the loop will continue.       
      if rectPlay.collidepoint(mx,my):
        playing = True
        collecting = True
      # If "How to.." is clicked, the instructions will pop up.
      elif rectMiddle.collidepoint(mx,my):
        HowPage = True
      # If "Quit" is clicked, the loop will end.
      elif rectQuit.collidepoint(mx,my):
        running = False
  # While the instructions are being displayed, what will happen when the mouse is clicked.
  while HowPage:
    howPage()
    display.flip()    
    for evt in event.get():
      if evt.type == MOUSEBUTTONDOWN: 
        HowPage = False  
      if evt.type == QUIT:
        running = False  
        HowPage = False
  # All the text that will be displayed on the screen.
  if showMe:
    start()
    textFont = font.SysFont("Comic Sans MS", width//12)    
    scoreDisplay = textFont.render("Your score: " + str(youScore),1,WHITE)
    HighscoreDisplay = textFont.render("Highscore: " + str(Highscore),1,WHITE)
    screen.blit(scoreDisplay, (150,200))
    screen.blit(HighscoreDisplay, (150,300))
    display.flip()    
    time.wait(2000)
    showMe = False
   
  # While the user is playing, what will be displayed is the background and the garbage at first. 
  if playing:
    start()
    garbage(trashx,trashy)
    display.flip()
  # What is occuring while the game is being played.
  while playing:
    textFont = font.SysFont("Comic Sans MS", width//15)
    scoreDisplay = textFont.render(str(score),1,WHITE)
    directionDisplay = textFont.render(str(xforce),1,WHITE)
    # If the X is clicked, the entire game will close.
    if evt.type == QUIT:
      running = False
      playing = False
      playing = False
    # The garbage can moving from one side to the other.
    if canLeft:
      canx -= 1*canSpeed
    elif canRight:
      canx += 1*canSpeed
    if canx <= 0:
      canLeft = False
      canRight = True
    if canx + 124 >= width:
      canLeft = True
      canRight = False
    trashRect = Rect(canx,cany,124,167)
    # If any of the arrow keys are pressed, what is happening to the direction that the garbage will travel.
    if collecting:
      for evnt in event.get():
        if evnt.type == KEYDOWN:
          if evnt.key == K_RIGHT:
            xforce += 1
          elif evnt.key == K_LEFT:
            xforce -= 1
          elif evnt.key == K_SPACE:
            collecting = False
            throwing = True
     # This entire loop is for the garbage when it is released. Baisically, what will happen when the garbage can rebounds and either hits the garbage can, or doesn't.      
    if throwing:
      trashx += xforce
      if goup and trashy < ballLimit:
          godown= True
      if godown:
        trashy += yforce
        ballRect = Rect(trashx,trashy,80,90)
        # If the garbage gets into the garbage can.
        if trashRect.colliderect(ballRect):
          score += 1
          trashx = 300
          trashy = 550
          goup = True
          godown = False
          xforce = 0
          collecting = True
          throwing = False
          # An if statement that increases the speed of the garbage can, so every time the user hits a milestone in the game, the difficuilty increases.
          if score % 10 == 0:
            canSpeed += 1
        elif trashy >= 600:
          youScore = score
          # Creates a new highscore.
          if score > Highscore:
            Highscore = score
            scorepage = open("Scores.txt","w")
            scorepage.write(str(Highscore))
            scorepage.close()
           # If the garbage misses the can. 
          trashx = 300
          trashy = 550
          goup = True
          godown = False
          xforce = 0
          collecting = True
          playing = False
          throwing = False
          mx,my = 0,0
          showMe = True
      elif goup:
        trashy -= yforce
        
    # What will be displayed after all the game functions.    
    start()
    garbage(trashx,trashy)
    garbagecan(canx,cany)
    screen.blit(scoreDisplay, (0,0))
    screen.blit(directionDisplay, (0, 550))
    # Displays everything for a minute if the game is still left open by the user.
    display.flip()
    myClock.tick(60)            

# Quits the program.
quit()