# PYTHON - MIT - UNICAMP
# =============================================================================
# Created By   : Matheus Percário Bruder
# Created Date : February 11th, 2021
# ============================================================================


def print_grid(grid):
    for l in grid:
        print(l)


class Ant:

    def __init__(self, lin, col, direction):
        self.lin = lin
        self.col = col
        self.direction = direction
        self.coords = [lin, col]
        self.steps = 0

    def move(self):
        if self.direction == 0:  # NORTE
            self.lin -= 1
        elif self.direction == 1:  # LESTE
            self.col += 1
        elif self.direction == 2:  # SUL
            self.lin += 1
        elif self.direction == 3:  # OESTE
            self.col -= 1

        self.coords = [self.lin, self.col]
        self.steps += 1

    def turn(self, rule):
        if rule == 'L':
            self.direction = (self.direction - 1) % 4  # 4= direções possíveis
        else:
            self.direction = (self.direction + 1) % 4

    def __str__(self):
        return f"-------------------\nANT\ncoords ={self.coords}\ndirection ={self.direction}\n"


def run_langton(rules, size):
    # Criar grid
    grid = [[0] * size for line in range(size)]

    # cores baseadas nos indices das regras
    colors = [k for k in range(len(rules))]

    # Instanciar formiga
    ant = Ant(size // 2, size // 2, 0)

    while True:
        # Dar primeiro passo
        lin, col = ant.coords
        if lin < 0 or lin >= size or col < 0 or col >= size:
            break

        grid[lin][col] = (grid[lin][col] + 1) % len(colors)  # mudar cor
        ant.move()  # alterar coordenadas formiga

        lin, col = ant.coords
        if lin < 0 or lin >= size or col < 0 or col >= size:
            break

        dir = rules[grid[lin][col]]  # rules[0] -> 'R' or rules[1] -> 'L' ...
        ant.turn(dir)  # virar formiga de acordo com a cor

    # Movimentação formiga
    print_grid(grid)
    print(ant)

    return ant.steps, grid


# Início programa ---------------------------------
_rules = 'RLRLL'
_size = 151

steps, grid = run_langton(_rules, _size)
# print(steps)
