import curses
import sys
import time

import life


def parse_file(fname, size):
    pattern = set()
    dx, dy = size[0]/2, size[1]/2

    with open(fname) as f:
        for row in f:
            x, y = [int(x.strip()) for x in row.split(',')]
            pattern.add((x + dx, y + dy))
    return pattern


def main(sc, pattern_file):
    curses.curs_set(0)
    sc.nodelay(1)
    size = sc.getmaxyx()

    l = life.Life(size, parse_file(pattern_file, size))
    while True:
        sc.clear()
        for x, y in l.get_board():
            sc.addch(x, y, '*')
        sc.refresh()
        l.evaluate()

        if sc.getch() == ord('q'):
            break

        time.sleep(0.5)

    curses.curs_set(1)


if __name__ == '__main__':
    if len(sys.argv) < 2:
        sys.exit('Usage: {0} pattern_file'.format(sys.argv[0]))
    curses.wrapper(main, sys.argv[1])
