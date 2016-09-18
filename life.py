class Life:
    def __init__(self, size, board):
        self._max_x, self._max_y = size
        self._board = board

    def _get_neighbours(self, cell):
        x, y = cell
        ds = ((-1, -1), (0, -1), (1, -1),
              (-1, 0), (1, 0),
              (-1, 1), (0, 1), (1, 1))

        for dx, dy in ds:
            nx, ny = x + dx, y + dy
            if nx >= self._max_x:
                nx = 0
            if nx < 0:
                nx = self._max_x - 1
            if ny >= self._max_y:
                ny = 0
            if ny < 0:
                ny = self._max_y - 1
            yield (nx, ny)

    def _count_live_neighbours(self, cell):
        return sum([int(n in self._board) for n in
                    self._get_neighbours(cell)])

    def _get_dead_neighbours(self, cell):
        return {n for n in self._get_neighbours(cell)
                if n not in self._board}

    def evaluate(self):
        board = set()
        dead_cells = set()

        for cell in self._board:
            if 2 <= self._count_live_neighbours(cell) <= 3:
                board.add(cell)
            dead_cells.update(self._get_dead_neighbours(cell))

        for cell in dead_cells:
            if self._count_live_neighbours(cell) == 3:
                board.add(cell)

        self._board = board

    def get_board(self):
        return self._board
