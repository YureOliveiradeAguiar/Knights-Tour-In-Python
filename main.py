n = int(input("Enter the value n for the n by n matrix: "))
start_x = int(input(f"Enter the starting row (1 to {n}): ")) - 1
start_y = int(input(f"Enter the starting column (1 to {n}): ")) - 1
movimentos = [(2, 1), (1, 2), (-1, 2), (-2, 1),
    (-2, -1), (-1, -2), (1, -2), (2, -1)]

tabuleiro = [[-1 for _ in range(n)] for _ in range(n)]

def dentro_do_tabuleiro(x, y):
    return 0 <= x < n and 0 <= y < n

def resolver(x, y, passo):
    tabuleiro[x][y] = passo

    if passo == n * n - 1:
        return True

    for dx, dy in movimentos:
        nx, ny = x + dx, y + dy
        if dentro_do_tabuleiro(nx, ny) and tabuleiro[nx][ny] == -1:
            if resolver(nx, ny, passo + 1):
                return True

    tabuleiro[x][y] = -1
    return False

if dentro_do_tabuleiro(start_x, start_y):
    if resolver(start_x, start_y, 0):
        for linha in tabuleiro:
            print(" ".join(f"{cel:2}" for cel in linha))
    else:
        print("Nenhuma solução encontrada a partir dessa posição.")
else:
    print("Posição inicial inválida.")
