import curses

def draw_balloon(stdscr, x, y):
    balloon = [
        "───▄▀▀▀▄▄▄▄▄▄▄▀▀▀▄───",
        "───█▒▒░░░░░░░░░▒▒█───",
        "────█░░█░░░░░█░░█────",
        "─▄▄──█░░░▀█▀░░░█──▄▄─",
        "█░░█─▀▄░░░░░░░▄▀─█░░█"
    ]

    for i, line in enumerate(balloon):
        if 0 <= y + i < curses.LINES:
            stdscr.addstr(y + i, x, line[:curses.COLS - x])

def main(stdscr):
    curses.curs_set(0)
    stdscr.nodelay(1)
    stdscr.timeout(100)
    height, width = stdscr.getmaxyx()

    x = width // 2 - 16
    y = height // 2 - 5

    dy = 1

    while True:
        stdscr.clear()

        draw_balloon(stdscr, x, y)
        stdscr.refresh()

        y += dy

        if y <= 0 or y >= height - 5:
            dy = -dy

        key = stdscr.getch()
        if key == ord('q'):
            break

curses.wrapper(main)
