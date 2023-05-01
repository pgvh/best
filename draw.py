import math
import pygame

screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

#colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)


def myP(x, y, color):
    screen.set_at((x, y), color)
    pygame.display.flip()


# Our line algorithm will be according to Bresenham
def myLine(x1, y1, x2, y2, color):
    deltaX = x2 - x1
    deltaY = y2 - y1
    # Determine how steep the line is
    is_steep = abs(deltaY) > abs(deltaX)

    # Rotate line
    if is_steep:
        x1, y1 = y1, x1
        x2, y2 = y2, x2

    # Swap start and end points if necessary and store swap state
    swapped = False
    if x1 > x2:
        x1, x2 = x2, x1
        y1, y2 = y2, y1
        swapped = True

    # Recalculate detla x and delta y
    deltaX = x2 - x1
    deltaY = y2 - y1

    # getting our error
    err = int(deltaX / 2.0)
    if y1 < y2:
        currentYstep = 1
    else:
        currentYstep = -1
    points = []
    tempY = y1
    #creating our line
    for tempX in range(x1, x2 + 1):
        coord = (tempY, tempX) if is_steep else (tempX, tempY)
        points.append(coord)
        err -= abs(deltaY)
        if err < 0:
            tempY += currentYstep
            err += deltaX
    if swapped:
        points.reverse()
    for point in points:
        myP(point[0], point[1], color)


def parallelogram(x1, y1, x2, y2):
    extra = round(math.sqrt(((x1 - x2) ** 2) + ((y1 - y2) ** 2)) / 2)
    #create points 3 and 4 from input points 1 and 2
    if x1 > x2:
        x3 = x1 + extra
        y3 = y1
        x4 = x2 - extra
        y4 = y2
    else:
        x3 = x1 - extra
        y3 = y1
        x4 = x2 + extra
        y4 = y2
    #if on the same y axis
    if abs(y3 - y4) < 100:
        x3 = x1
        x4 = x2
        y3 = y3 + extra
        y4 = y4 - extra


    # drawing the output result of the lines
    myLine(x1, y1, x3, y3, WHITE)
    myLine(x4, y4, x1, y1, WHITE)
    myLine(x2, y2, x4, y4, WHITE)
    myLine(x3, y3, x2, y2, WHITE)
    myLine(x3, y3, x4, y4, WHITE)
    return x3, y3, x4, y4


def myCircle(xc, yc, radius):
    tempX, tempY = 0, radius
    d = 3 - 2 * radius
    drawCircle(xc, yc, tempX, tempY)
    while tempY >= tempX:
        tempX += 1

        #   update x, d, y according to the checking process decision parameter
        if d > 0:
            tempY -= 1
            d = d + (tempX - tempY) * 4 + 10

        else:
            d = d + tempX*4 + 6
        drawCircle(xc, yc, tempX, tempY)


def updateCurve(screen, curve):
    pygame.draw.rect(screen, pygame.Color(0, 0, 0), (200, 0, 200, 50))
    strNum = "{}".format(curve)
    myfont = pygame.font.SysFont('Comic Sans MS', 30)
    textsurface = myfont.render('Curve Value: ' + strNum, False, (WHITE))
    screen.blit(textsurface, (200, 0))


def drawCircle(midX, midY, tempX, tempY):
    myP(midX + tempX, midY + tempY, RED)
    myP(midX - tempX, midY + tempY, RED)
    myP(midX + tempX, midY - tempY, RED)
    myP(midX - tempX, midY - tempY, RED)
    myP(midX + tempY, midY + tempX, RED)
    myP(midX - tempY, midY + tempX, RED)
    myP(midX + tempY, midY - tempX, RED)
    myP(midX - tempY, midY - tempX, RED)


def getBerzVal(x1, x2, x3, x4, t):
    deltaA = -x1 + 3 * x2 - 3 * x3 + x4
    deltaB = 3 * x1 - 6 * x2 + 3 * x3
    deltaC = -3 * x1 + 3 * x2
    deltaD = x1
    result = deltaA * t ** 3 + deltaB * t ** 2 + deltaC * t + deltaD
    return round(result)


def myCurve(x1, x2, x3, x4, y1, y2, y3, y4, curve):
    xt1 = x1
    yt1 = y1

    for t in range(0, curve + 1):
        pX = getBerzVal(x1, x4, x3, x2, t / curve)
        pY = getBerzVal(y1, y4, y3, y2, t / curve)
        myLine(xt1, yt1, pX, pY, BLUE)
        xt1 = pX
        yt1 = pY


def draw_btn(screen):
    currentFont = pygame.font.SysFont('Comic Sans MS', 30)
    textsurface = currentFont.render('clear', False, (WHITE))
    screen.blit(textsurface, (0, 0))
    textsurface = currentFont.render('+ -', False, (WHITE))
    screen.blit(textsurface, (74, 0))


def main():
    #init progrem
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    draw_btn(screen)
    positions = []
    counter = 0
    running = True
    curve = 3
    updateCurve(screen, curve)

    #waiting for user 2 input points
    while running:
        clock.tick(30)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONUP:
                #get user input
                pos = pygame.mouse.get_pos()
                #if the user clicked ont the cleaar btn
                if pos[0] < 73 and pos[1] < 43:
                    positions = []
                    counter = 0
                    screen.fill((0, 0, 0))
                    draw_btn(screen)
                #if the user clicked on the plus btn
                elif 75 < pos[0] < 91 and pos[1] < 43:
                    curve = curve + 1
                    print("curve update", curve)
                    updateCurve(screen, curve)
                # if the user clicked on the minus btn
                elif 92 < pos[0] < 110 and pos[1] < 43:
                    if curve > 2:
                        curve = curve - 1
                    updateCurve(screen, curve)
                #if there are less then 2 points add them to the screen
                elif counter < 2:
                    print(pos)
                    positions.append(pos[0])
                    positions.append(pos[1])
                    myP(pos[0], pos[1], WHITE)
                    counter += 1
                #if there are 2 points create all ths shapes
                if counter == 2:
                    x1 = positions[0]
                    y1 = positions[1]
                    x2 = positions[2]
                    y2 = positions[3]
                    myLine(x1, y1, x2, y2, WHITE)
                    x3, y3, x4, y4 = parallelogram(x1, y1, x2, y2)
                    #ger the middle point
                    midX = int(abs(x1 + x2) / 2)
                    midY = int(abs(y1 + y2) / 2)
                    r = math.sqrt(((x1 - midX) ** 2) + ((y1 - midY) ** 2))
                    myCircle(midX, midY, int(r))
                    myCurve(x1, x2, x3, x4, y1, y2, y3, y4, curve)
                    #restare
                    positions = []
                    counter = 0
    #exit
    pygame.quit()

main()
