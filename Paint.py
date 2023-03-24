import pygame.time
from venv import *
import tensorflow as tf
from tensorflow import keras
import numpy as np

model = keras.models.load_model("numbermodel.h5")

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Guess the number")

def init_grid(rows, cols, color):
    grid = []

    for i in range(rows): #creating a 28x28 grid of lists
        grid.append([])
        for _ in range(cols): #_ is used when we don't use the variable in the loop
            grid[i].append(color)

    return grid

def draw_grid(win, grid):
    for i, row in enumerate(grid):
        for j, pixel in enumerate(row):
            pygame.draw.rect(win, pixel, (j * PIXEL_SIZE, i * PIXEL_SIZE, PIXEL_SIZE, PIXEL_SIZE)) #might have to change if I wanna paint bigger

    if DRAW_GRID_LINES: #if we wanna show the grid
        for i in range(ROWS + 1):
            pygame.draw.line(win, BLACK, (0, i * PIXEL_SIZE), (WIDTH, i * PIXEL_SIZE))

        for i in range(COLS + 1):
            pygame.draw.line(win, BLACK, (i * PIXEL_SIZE, 0), (i * PIXEL_SIZE, HEIGHT - TOOLBAR_HEIGHT))

def draw(win, grid, buttons):
    win.fill(BG_COLOR)
    draw_grid(win, grid) #calling the drawing of grid

    for button in buttons:
        button.draw(win)

    text_font = get_another_font("comicsans", 22)
    text_surface = text_font.render(prediction_text, 1, BLACK)
    WIN.blit(text_surface,
             (10 + 260 / 2 - text_surface.get_width() / 2, button_y + 75 + 55 / 2 - text_surface.get_height() / 2))

    text_surface2 = text_font.render(certainty_text, 1, BLACK)
    WIN.blit(text_surface2,
             (290 + 260 / 2 - text_surface2.get_width() / 2, button_y + 75 + 55 / 2 - text_surface2.get_height() / 2))
    pygame.display.update() #Update display everytime something changes

def get_row_col_from_pos(pos):
    x, y = pos
    row = y // PIXEL_SIZE #// tager det hele tal der kan divideres for at finde hvad pixel vi er i
    col = x // PIXEL_SIZE

    if row >= ROWS: #if we press outside the grid (e.g. toolbar)
        raise IndexError

    return row, col

def draw_text_for_model():
    pass

def predict():
    predicted_grid = []
    for i, row in enumerate(grid):
        predicted_grid.append([])
        for tuple in row:
            predicted_grid[i].append(min(tuple))

    for i, row in enumerate(predicted_grid):
        predicted_grid[i] = [-x + 255 for x in predicted_grid[i]] #reverse the list (0-255)

    predicted_array = np.array(predicted_grid)[None, :]
    predicted_array = predicted_array / 255

    prediction = model.predict(predicted_array)
    predicted_number = np.argmax(prediction)
    certainty = np.amax(prediction) * 100

    #prediction_text = f"Prediction: {predicted_number}"
    #certainty_text = f"Certainty: {certainty:.2f} %"

    return predicted_array, prediction, predicted_number, certainty

run = True
clock = pygame.time.Clock()
grid = init_grid(ROWS, COLS, BG_COLOR)
drawing_color = BLACK

prediction_text = "Prediction:     "
certainty_text = "Certainty:     "
button_y = HEIGHT - TOOLBAR_HEIGHT + 10
buttons = [
    Button(10, button_y, 30, 30, BLACK),
    Button(45, button_y, 30, 30, GREY),
    Button(80, button_y, 30, 30, WHITE),
    Button(115, button_y, 30, 30, RED),
    Button(150, button_y, 30, 30, ORANGE),
    Button(10, button_y + 35, 30, 30, YELLOW),
    Button(45, button_y + 35, 30, 30, GREEN),
    Button(80, button_y + 35, 30, 30, TURKISH),
    Button(115, button_y + 35, 30, 30, BLUE),
    Button(150, button_y + 35, 30, 30, PINK),

    Button(190, button_y, 100, 65, WHITE, "Erase", BLACK),
    Button(300, button_y, 100, 65, WHITE, "Clear", BLACK),
    Button(410, button_y, 140, 65, WHITE, "Predict", BLACK, False),
    Button(10, button_y + 75, 540, 55, WHITE, None, BLACK, False)
]

#pred_butt = Button(10, button_y + 65, 480, 50, WHITE, prediction_text, BLACK)

while run:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #Will quit the program if we press quit
            run = False

        if pygame.mouse.get_pressed()[0]: #[0] is the left-click on the mouse
            pos = pygame.mouse.get_pos() #getting the x,y position of the mouse
            try:
                row, col = get_row_col_from_pos(pos)
                grid[row][col] = drawing_color
                grid[row+1][col] = drawing_color
                grid[row+1][col+1] = drawing_color
                grid[row][col+1] = drawing_color
            except IndexError:
                for button in buttons:
                    if not button.clicked(pos):
                        continue
                    if not button.change_color == False:
                        drawing_color = button.color
                    if button.text == "Clear":
                        grid = init_grid(ROWS, COLS, BG_COLOR)
                        prediction_text = "Prediction:     "
                        certainty_text = "Certainty:     "
                        drawing_color = BLACK

                    if button.text == "Predict":
                        predicted_grid, prediction, predicted_number, certainty = predict()
                        prediction_text = f"Prediction: {predicted_number}"
                        certainty_text = f"Certainty: {certainty:.2f} %"


    draw(WIN, grid, buttons)

pygame.quit()