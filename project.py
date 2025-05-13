from utils import *

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pixel Art Program")

### here im looping through the columns and rows i have and their stored into this list here. Its how im setting up the actual grid
### you can see that the append here is adding the rows and column colors. 
def init_grid(rows, cols, color):
    grid = []

    for i in range(rows):
        grid.append([])
        for _ in range(cols):
            grid[i].append(color)

    return grid

### enumerate here helps give me i = 0 and the row that ist corresponds to in the grd.
def draw_grid(win, grid):
    for i, row in enumerate(grid):
        for j, pixel in enumerate(row):
            pygame.draw.rect(win, pixel, (j * PIXEL_SIZE, i *
                                          PIXEL_SIZE, PIXEL_SIZE, PIXEL_SIZE))  ### I draw a rectangle in each pixel, and this is calucalted from pixel size. 
                                          ###There is a row and col for each pixel and to know which square were on I mult by the pixel_size im on. 0, 0 being the top left corner. 

    if DRAW_GRID_LINES:
        for i in range(ROWS + 1):      ##draws horizontal lines 
            pygame.draw.line(win, BLACK, (0, i * PIXEL_SIZE),
                             (WIDTH, i * PIXEL_SIZE))

        for i in range(COLS + 1):       ##draws vert. lines 
            pygame.draw.line(win, BLACK, (i * PIXEL_SIZE, 0),
                             (i * PIXEL_SIZE, HEIGHT - TOOLBAR_HEIGHT))


def draw(win, grid, buttons):
    win.fill(BG_COLOR)
    draw_grid(win, grid)

    for button in buttons:
        button.draw(win)

    pygame.display.update()


def get_row_col_from_pos(pos):  ### had to use integer division here because the pos needs to round to nearest pixel that the user clicked on. 
    x, y = pos
    row = y // PIXEL_SIZE
    col = x // PIXEL_SIZE

    if row >= ROWS:
        raise IndexError

    return row, col


run = True
clock = pygame.time.Clock()
grid = init_grid(ROWS, COLS, BG_COLOR)
drawing_color = BLACK

### these are the buttons im drawing down under the canvas, their colors are referenced from settings.
button_y = HEIGHT - TOOLBAR_HEIGHT/2 - 25   
buttons = [
    Button(10, button_y, 50, 50, BLACK),
    Button(70, button_y, 50, 50, RED),
    Button(130, button_y, 50, 50, GREEN),
    Button(190, button_y, 50, 50, BLUE),
    Button(250, button_y, 50, 50, BROWN),
    Button(310, button_y, 50, 50, LAVENDER),
    Button(380, button_y, 50, 50, WHITE, "Erase", BLACK),
    Button(450, button_y, 50, 50, WHITE, "Clear", BLACK)
]

while run:
    clock.tick(FPS)  ###using clock i set the frame rate for consistent performance

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if pygame.mouse.get_pressed()[0]:   ### did the user press left, middle, or right, in this case, did they press left. If so do the following: change pixel color. 
            pos = pygame.mouse.get_pos()   ###gives x,y pos of where user pressed their mouse. 

            try:
                row, col = get_row_col_from_pos(pos) 
                grid[row][col] = drawing_color
            except IndexError:   ###if the user didnt press anywhere then continue the program.
                for button in buttons:
                    if not button.clicked(pos):
                        continue

                    drawing_color = button.color
                    if button.text == "Clear":
                        grid = init_grid(ROWS, COLS, BG_COLOR)  ###actually changes color of pixel if the user does click on a pixel. 
                        drawing_color = BLACK

    draw(WIN, grid, buttons)

pygame.quit()