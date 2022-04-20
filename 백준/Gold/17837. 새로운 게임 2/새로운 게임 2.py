from collections import deque
import sys


class ChessPiece:
    def __init__(self, x, y, dir, name):
        self.name = name
        self.x = x
        self.y = y
        self.dir = dir
        self.bottom = None
        self.top = None

    def get_top(self):
        this = self
        while this.top is not None:
            this = this.top
        return this

    def get_bottom(self):
        this = self
        while this.bottom is not None:
            this = this.bottom
        return this

    def reverse(self):
        this = self.get_top()
        while this is not None:
            this.top, this.bottom = this.bottom, this.top
            this = this.top

    def get_count(self):
        this = self.get_top()
        count = 0
        while this is not None:
            count += 1
            this = this.bottom
        return count

    def mark(self, chess_board):
        chess_board[self.x][self.y] = self.get_top()

    def demark(self, chess_board):
        chess_board[self.x][self.y] = None

    def _move(self, x, y):
        this = self
        while this is not None:
            this.x, this.y = x, y
            this = this.top

    def move(self, chess_board, board_color):

        n = len(chess_board)
        nx, ny = self.x + self.dir[0], self.y + self.dir[1]

        if (nx < 0 or nx >= n or ny < 0 or ny >= n) or board_color[nx][ny] == 2:  # 파란색인 경우
            self.dir = (self.dir[0] * -1, self.dir[1] * -1)
            new_nx, new_ny = self.x + self.dir[0], self.y + self.dir[1]
            if (0 <= new_nx < n and 0 <= new_ny < n) and board_color[new_nx][new_ny] != 2:
                self.move(chess_board, board_color)

        elif board_color[nx][ny] == 0:  # 흰색인 경우

            if self.bottom is not None:
                self.bottom.top = None
                self.bottom.mark(chess_board)
            else:
                self.demark(chess_board)
            self.bottom = None
            self._move(nx, ny)
            if chess_board[nx][ny] is not None:
                self.bottom = chess_board[nx][ny]
                chess_board[nx][ny].top = self

            self.mark(chess_board)

        elif board_color[nx][ny] == 1:  # 빨간색인 경우

            if self.bottom is not None:
                self.bottom.top = None
                self.bottom.mark(chess_board)
            else:
                self.demark(chess_board)
            self.bottom = None
            self._move(nx, ny)
            self.reverse()
            bottom = self.get_bottom()
            if chess_board[nx][ny] is not None:
                bottom.bottom = chess_board[nx][ny]
                chess_board[nx][ny].top = bottom
            self.mark(chess_board)


        if self.get_count() >= 4:
            return False
        return True


dxy = {1: (0, 1), 2: (0, -1), 3: (-1, 0), 4: (1, 0)}
N, K = map(int, sys.stdin.readline().split())
board_color = [list(map(int, sys.stdin.readline().split())) for i in range(N)]
board = [[None for i in range(N)] for i in range(N)]
chess_pieces = [list(map(int, sys.stdin.readline().split())) for i in range(K)]
seq = 1
c = []
for x, y, dir in chess_pieces:
    c.append(ChessPiece(x-1, y-1
                        , dxy[dir], str(seq)))
    seq+=1
for _ in c:
    _.mark(board)

turn = 1
for i in range(1001):
    for chess_piece in c:
        if not chess_piece.move(board, board_color):
            print(turn)
            sys.exit()
    turn +=1

if turn>1000:
    print(-1)



