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

    def turn(self, rule):
        if rule == 'L':
            self.direction = (self.direction - 1) % 4  # 4= direções possíveis
        else:
            self.direction = (self.direction + 1) % 4

    def __str__(self):
        return f"-------------------\nANT\ncoords ={self.coords}\ndirection ={self.direction}\n"


def run_langton(rules, size):
    # cores baseadas nos indices das regras
    colors = [k for k in range(len(rules))]
    #print(f"colors ={colors}")

    # Criar & ver grid
    grid = [[0] * size for line in range(size)]

    # Instanciar formiga
    ant = Ant(size // 2, size // 2, 0)
    # print(ant)
    count = 0

    while True:
        # Dar primeiro passo
        lin, col = ant.coords

        if lin < 0 or lin >= size or col < 0 or col >= size:
            #print(f"ENTROUU BREAK!")
            break

        grid[lin][col] = (grid[lin][col] + 1) % len(colors)  # mudar cor
        dir = rules[grid[lin][col]]  # rules[0] -> 'R' or rules[1] -> 'L' ...
        ant.turn(dir)  # virar formiga de acordo com a cor
        ant.move()  # alterar coordenadas formiga
        count += 1

    # Movimentação formiga
    # print_grid(grid)
    # print(ant)

    return count, grid


# Início programa ---------------------------------
_rules = 'RL'
_size = 51

steps, grid = run_langton(_rules, _size)
print(steps)
