import pygame
import sys



# Khởi tạo Pygame
pygame.init()

# Lấy thông tin màn hình
info = pygame.display.Info()
screen_width = info.current_w
screen_height = info.current_h

# Đặt kích thước cửa sổ bằng 80% kích thước màn hình
width = int(screen_width * 0.8)
height = int(screen_height * 0.8)
screen = pygame.display.set_mode((width, height))

# Đặt tiêu đề cho cửa sổ
pygame.display.set_caption("Game Caro")

# Màu sắc
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

WIN = 1
DRAW = 0
LOSE = -1

INF = 1e9 + 7

# Kích thước bàn cờ
rows = 5
columns = 6
cell_size = min(width, height) // min(rows, columns)  # Kích thước mỗi ô

# Tạo bàn cờ
board = [[None for _ in range(columns)] for _ in range(rows)]  # None: trống, True: X, False: O

# Lượt chơi (True: X, False: O)
player = True

# Các hướng kiểm tra chiến thắng
north = [(-4, 0), (-3, 0), (-2, 0), (-1, 0), (0, 0)]
north_east = [(-4, 4), (-3, 3), (-2, 2), (-1, 1), (0, 0)]
east = [(0, -4), (0, -3), (0, -2), (0, -1), (0, 0)]
south_east = [(4, 4), (3, 3), (2, 2), (1, 1), (0, 0)]
south = [(4, 0), (3, 0), (2, 0), (1, 0), (0, 0)]
south_west = [(4, -4), (3, -3), (2, -2), (1, -1), (0, 0)]
west = [(0, 4), (0, 3), (0, 2), (0, 1), (0, 0)]
north_west = [(-4, -4), (-3, -3), (-2, -2), (-1, -1), (0, 0)]

directions = [north, north_east, east, south_east, south, south_west, west, north_west]

def is_win(position) -> bool:
    x, y = position[0], position[1]
    for direction in directions:
        count = 0
        for horizontal, vertical in direction:
            X, Y = x + horizontal, y + vertical
            if 0 <= X < rows and 0 <= Y < columns:
                count += (bool)(board[X][Y] == player)
        if count == 5:
            return True
    return False

# Vòng lặp chính của trò chơi
def main():
    global player
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:  # Thoát bằng phím ESC
                    running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Lấy vị trí chuột
                mouse_x, mouse_y = pygame.mouse.get_pos()
                # Chuyển đổi vị trí chuột thành chỉ số ô trên bàn cờ
                col = mouse_x // cell_size
                row = mouse_y // cell_size
                # Kiểm tra ô đó có trống không
                if 0 <= row < rows and 0 <= col < columns and board[row][col] is None:
                    board[row][col] = player
                    if is_win((row, col)):
                        print(f"Người chơi {'X' if player else 'O'} đã chiến thắng!")
                        running = False
                    # Đổi lượt chơi
                    player = not player

        # Vẽ nền
        screen.fill(WHITE)

        # Vẽ bàn cờ
        for row in range(rows):
            for col in range(columns):
                # Vẽ ô vuông
                pygame.draw.rect(screen, BLACK, (col * cell_size, row * cell_size, cell_size, cell_size), 1)
                # Vẽ X hoặc O
                if board[row][col] == True:
                    pygame.draw.line(screen, RED, (col * cell_size, row * cell_size), 
                                    ((col + 1) * cell_size, (row + 1) * cell_size), 3)
                    # Thay vì vẽ thì tôi có thể đồ họa cho đẹp hơn được không ?
                    pygame.draw.line(screen, RED, ((col + 1) * cell_size, row * cell_size),
                                    (col * cell_size, (row + 1) * cell_size), 3)
                elif board[row][col] == False:
                    pygame.draw.circle(screen, BLUE, (col * cell_size + cell_size // 2, row * cell_size + cell_size // 2),
                                       cell_size // 2 - 5, 3)

        # Cập nhật màn hình
        pygame.display.flip()

        # Giới hạn tốc độ khung hình
        pygame.time.Clock().tick(60)

    # Kết thúc Pygame
    pygame.quit()
    sys.exit()

# Chạy trò chơi
if __name__ == "__main__":
    main()