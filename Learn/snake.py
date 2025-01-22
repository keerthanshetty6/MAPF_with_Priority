import curses
import random
import time

def setup_window(stdscr, x, y):
    stdscr.clear()
    stdscr.refresh()

    # Set window dimensions
    win_height = x
    win_width = y

    win = curses.newwin(win_height, win_width, 0, 0)
    win.keypad(True)
    curses.noecho()
    curses.curs_set(0)
    win.border(0)
    win.nodelay(True)

    return win

def snake_game(stdscr):
    # Initial dimensions for the game window
    x = y = 60

    height, width = stdscr.getmaxyx()
    print(f"Terminal size: {height}x{width}")  # Debugging info
    win_height = min(x, height - 1)
    win_width = min(y, width - 1)

    win = setup_window(stdscr, win_height, win_width)

    # Initial snake position (3 segments)
    
    #snake = [(5, 5), (5, 4), (5, 3)]  # Snake coordinates
    head = (random.randint(4, win_height - 4), random.randint(4, win_width - 4))  # snake head
    snake = [(head[0], head[1]), (head[0], head[1] - 1), (head[0], head[1] - 2)] 
    
    # Generate food coordinates within the valid window area
    food = (random.randint(1, win_height - 2), random.randint(1, win_width - 2))  # Avoid placing food on borders
    win.addch(food[0], food[1], '*')  # Draw food

    key = curses.KEY_RIGHT

    vertical_speed = 0.1  # Speed for vertical movement (up/down)
    horizontal_speed = 0.1  # Speed for horizontal movement (left/right)

    while True:
        next_key = win.getch()
        key = key if next_key == -1 else next_key  # Keep current direction if no key is pressed

        # Move snake's head
        new_head = (snake[0][0], snake[0][1])  # Copy current head position

        # Horizontal move (right and left)
        if key == curses.KEY_RIGHT:
            new_head = (new_head[0], new_head[1] + 1)
            delay = horizontal_speed
        elif key == curses.KEY_LEFT:
            new_head = (new_head[0], new_head[1] - 1)
            delay = horizontal_speed

        # Vertical move (up and down)
        elif key == curses.KEY_UP:
            new_head = (new_head[0] - 1, new_head[1])
            delay = vertical_speed
        elif key == curses.KEY_DOWN:
            new_head = (new_head[0] + 1, new_head[1])
            delay = vertical_speed

        # Check for window boundaries (game over if out of bounds)
        if new_head[0] <= 0 or new_head[0] >= win_height or new_head[1] <= 0 or new_head[1] >= win_width:
            break  # End game if snake is out of bounds

        # Check if snake collides with itself (game over if it does)
        if new_head in snake:
            break  # End game if snake collides with itself

        snake.insert(0, new_head)  # Insert new head at the front of the snake

        if snake[0] == food:  # Snake eats the food
            food = (random.randint(1, win_height - 2), random.randint(1, win_width - 2))  # New food position
            win.addch(food[0], food[1], '*')  # Draw new food
        else:
            tail = snake.pop()  # Remove the tail
            # Remove the tail only if it is within bounds
            if 0 <= tail[0] < win_height and 0 <= tail[1] < win_width:
                win.addch(tail[0], tail[1], ' ')  # Erase tail from screen

        # Draw the entire snake
        win.addch(new_head[0], new_head[1], '#')#new head

        # Refresh the window after each update
        win.refresh()

        # Add a delay based on the current direction (vertical or horizontal)
        time.sleep(delay)

    # Show game over message and wait for a key press
    game_over_message = "Game Over! Press any key to exit."
    
    # Ensure the position is within bounds
    message_row = win_height // 2
    message_col = (win_width - len(game_over_message)) // 2

    win.addstr(message_row, message_col, game_over_message)
    win.refresh()

    # Debugging log: Show that we've reached this point and are waiting for user input
    print("Game Over screen shown. Waiting for user input...")

    # Wait for the user to press a key to exit
    win.getch()

    # Debugging log: Confirm that the program is ending after a key press
    print("User pressed a key, exiting game...")

# Start the game with curses wrapper
curses.wrapper(snake_game)
