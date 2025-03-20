import pygame

# Initialize Pygame
pygame.init()

# Screen dimensions
screen_width = 1920
screen_height = 1080
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Isometric Grid")

# Colors
white = (255, 255, 255)
black = (0, 0, 0)

# Tile dimensions
tile_width = 32
tile_height = 32

# Grid dimensions
grid_width = tile_width * 4
grid_height = tile_height * 4

# Number of grids
num_grids_x = 8
num_grids_y = 8

# Create a list to store the grid positions
grid_positions = []
for y in range(num_grids_y):
    for x in range(num_grids_x):
        # Calculate the isometric position of each grid
        grid_x = (x * grid_width / 2) + (y * grid_width / 2)
        grid_y = (y * grid_height / 2) - (x * grid_height / 2)
        grid_positions.append((grid_x, grid_y))

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the background
    screen.fill(white)

    # Draw the grid
    for grid_x, grid_y in grid_positions:
        # Draw the grid background (optional)
        #pygame.draw.rect(screen, black, (grid_x, grid_y, grid_width, grid_height), 1)

        # Draw the tiles within the grid
        for tile_y in range(4):
            for tile_x in range(4):
                # Calculate the isometric position of each tile
                tile_x_offset = (tile_x * tile_width / 2) + (tile_y * tile_width / 2)
                tile_y_offset = (tile_y * tile_height / 2) - (tile_x * tile_height / 2)

                # Draw the tile
                tile_rect = pygame.Rect((grid_x + tile_x_offset) + screen_width / 4, (grid_y + tile_y_offset) + screen_height / 2, tile_width, tile_height)
                pygame.draw.rect(screen, black, tile_rect, 1)

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()