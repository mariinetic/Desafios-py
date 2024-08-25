import curses

def draw_heart(stdscr):
    heart = [
        "  **     **  ",
        " *  *   *  * ",
        "*    * *    *",
        "*     *     *",
        " *         * ",
        "  *       *  ",
        "   *     *   ",
        "    *   *    ",
        "     * *     ",
        "      *      "
    ]

    height, width = stdscr.getmaxyx()
    y = height // 2 - len(heart) // 2
    x = width // 2 - len(heart[0]) // 2

    while True:
        stdscr.clear()
        
        for i, line in enumerate(heart):
            if y + i < height and x < width:
                stdscr.addstr(y + i, x, line)
        
        stdscr.refresh()

        key = stdscr.getch()
        if key == ord('q'):
            break

curses.wrapper(draw_heart)
