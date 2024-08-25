import curses
import math

def main(stdscr):
    curses.curs_set(0)
    stdscr.nodelay(1)
    stdscr.timeout(100)
    height, width = stdscr.getmaxyx()

    radius = 10
    angle = 0
    center_y, center_x = height // 2, width // 2

    while True:
        stdscr.clear()

        # Calculate circle position
        y = int(center_y + radius * math.sin(angle))
        x = int(center_x + radius * math.cos(angle))

        # Ensure the coordinates are within the bounds of the screen
        if 0 <= y < height and 0 <= x < width:
            stdscr.addch(y, x, 'O')

        # Refresh the screen
        stdscr.refresh()

        # Update the angle
        angle += 0.1
        if angle >= 2 * math.pi:
            angle = 0

        # Break the loop if 'q' is pressed
        key = stdscr.getch()
        if key == ord('q'):
            break

curses.wrapper(main)
