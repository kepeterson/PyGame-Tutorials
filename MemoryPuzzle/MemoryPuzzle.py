import random, pygame, sys
from pygame.locals import *

FPS = 30
WINDOWWIDTH = 640
WINDOWHEIGHT = 480
REVEALSPEED = 8
BOXSIZE = 40
GAPSIZE = 10
BOARDWIDTH = 10
BOARDHEIGHT = 7
assert (BOARDWIDTH * BOARDHEIGHT) % 2 == 0, 'Need even number of Tiles'
XMARGIN = int((WINDOWWIDTH - (BOARDWIDTH * (BOXSIZE + GAPSIZE)))/2)
YMARGIN = int((WINDOWHEIGHT - (BOARDHEIGHT * (BOXSIZE + GAPSIZE)))/2)

GRAY = (100,100,100)
NAVYBLUE = (60,60,100)
WHITE = (255,255,255)
RED=(255,0,0)
GREEN=(0,255,0)
BLUE=(0,0,255)
YELLOW=(255,255,0)
ORANGE=(255,128,0)
PURPLE=(255,0,0255)
CYAN=(0,255,255)

BGCOLOR = NAVYBLUE
LIGHTBGCOLOR = GRAY
HIGHLIGHTCOLOR = BLUE
DONUT = 'donut'
SQUARE = 'square'
DIAMOND = 'diamond'
LINES = 'lines'
OVAL = 'oval'

ALLCOLORS = (RED, GREEN, BLUE, YELLOW, ORANGE, PURPLE, CYAN)
ALLSHAPES = (DONUT, SQUARE, DIAMOND, LINES, OVAL)
assert len(ALLCOLORS) * len(ALLSHAPES) * 2 >= BOARDWIDTH * BOARDHEIGHT, "Board is too big for the number of shapes/colors defined."
def main():
    global FPSCLOCK, DISPLAYSURF
    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH,WINDOWHEIGHT))

    mousex = 0
    mousey = 0
    pygame.display.set_caption('Memory Game')

    mainBoard = getRandomizedBoard()
    revealedBoxes = generateRevealedBoxesData(False)

    firstSelection = None

    DISPLAYSURF.fill(BGCOLOR)
    startGameAnimation(mainboard)

    while True: #main loop
        mouseClicked = False

        DISPLAYSURF.fill(BGCOLOR)
        drawBoard(mainBoard, revealedBoxes)

        for event in pygame.event.get():
            if event.type == QUIT \
            or (event.type == KEYUP and event.key == K_ESPACE):
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEMOTION:
                mousex, mousey = event.pos
            elif event.type == MOUSEBUTTONUP:
                mousex, mousey = event.pos
                mouseClicked = True

            boxx, boxy = getBoxAtPixel(mousex,mousey)
            if boxx != None and boxy != None:
                #over a box
                if not revealedBoxes[boxx][boxy]:
                    drawHighlightBox(boxx,boxy)
                if not revealedBoxes[boxx][boxy] and mouseClicked:
                    revealBoxesAnimation(mainBoard, [(boxx,boxy)])
                    revealedBoxes[boxx][boxy] = True
                    if firstSelection == None:
                        firstSelect = (boxx, boxy)
                    else:
                        #check for match
                        icon1shape, icon1color = getShapeandColor(mainboard,
                                                                  firstSelection[0],
                                                                  firstSelection[1])
                        icon2shape, icon2color = getShapeAndColor(mainboard,
                                                                  boxx,
                                                                  boxxy)

                        if icon1shape != icon2shape or icon1color != icon2color:
                            #no match
                            pygame.time.wait(1000)
                            coverBoxesAnimation(mainboard,
                                                [(firstSelection[0],firstSelection[1]),
                                                (boxx,boxy)])
                            revealedBoxes[firstSelection[0]][firsSlection[1]] = False
                            revealedBoxes[boxx][boxy] = False
                        elif hasWon(revealedBoxes):
                            gameWonAnimation(mainBoard)
                            pygame.time.wait(2000)

                            #Reset
                            mainBoard = getRandomizedBoard()
                            revealedBoes = generateRevealedBoxesData(False)

                            #show the board momentarily
                            drawBoard(mainBoard, revealedBoxes)
                            pygame.display.updated()
                            pygame.time.wait(1000)

                            startGameAnimation(mainBoard)
                        firstSelection = None

            pygame.display.update()
            FPSCLOCK.tick(FPS)

def generateRevealedBoxesData(val):
    revealedBoxes = []
    for i in range(BOARDWIDTH):
        revealedBoxes.append([val] * BOARDHEIGHT)
    return revealBoxes
                    
def getRandomizedBoard():
    icons = []
    for color in AllCOLORS:


        
