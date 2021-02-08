class Point:
    # usando um nome de variável curto para representar o número de
    # coordenadas para que eu possa encaixá-las no diagrama de ambiente
    n = 2


class Rectangle:
    pass


def find_center(rect):
    p = Point()
    p.x = rect.corner.x + rect.width/2
    p.y = rect.corner.y + rect.height/2
    return p


def print_point(p):
    print('(', p.x, ',', p.y, ')')


def grow_rectangle(rect, dwidth, dheight):
    rect.width = rect.width + dwidth
    rect.height = rect.height + dheight


def move_rectangle(rect, dx, dy):
    rect.corner.x += dx
    rect.corner.y += dy


def shifted_rectangle(rect, dx, dy):
    new_rect = Rectangle()  # cria uma nova instância
    # altura e largura devem ser iguais
    new_rect.width = rect.width
    new_rect.height = rect.height
    # o canto do retângulo é diferente, contudo
    # importante, fazemos uma nova instância de Point para o canto
    new_rect.corner = Point()
    new_rect.corner.x = rect.corner.x + dx
    new_rect.corner.y = rect.corner.y + dy
    return new_rect


box = Rectangle()
box.width = 100.0
box.height = 200.0
box.corner = Point()
box.corner.x = 0.0
box.corner.y = 0.0

center = find_center(box)
print_point(center)  # exibe ( 50, 100 )


# Modificar objeto diretamente ou por funções
box.width = box.width + 50
box.height = box.height + 100

print(box.width, box.height)  # exibe 150.0 300.0
grow_rectangle(box, 50, 100)
print(box.width, box.height)  # exibe 200.0 400.0

print(box.corner.x, box.corner.y)  # exibe 0.0 0.0
move_rectangle(box, 10, 20)
print(box.corner.x, box.corner.y)  # exibe 10.0 20.0


# Funções puras
print(box.corner.x, box.corner.y)  # exibe 10.0 20.0
new_box = shifted_rectangle(box, 15, 25)
print(box.corner.x, box.corner.y)  # exibe 10.0 20.0
print(new_box.corner.x, new_box.corner.y)  # exibe 25.0 45.0
