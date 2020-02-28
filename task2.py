from random import randint


class SearchPoint:
    '''Класс искомой точки'''

    def __init__(self, w, h):
        '''инициализация случайных координат искомой точки'''
        self.__x = randint(0, w)
        self.__y = randint(0, h)

    def where_is_point(self, x, y):
        '''Описывает положение искомой точки относительно текущей.
        Возможные варианты: "R", "RU", "RD", "L", "LU", "LD", "U", "D" , ""
        '''
        pos_x = pos_y = ''
        if x > self.__x:
            pos_x = 'L'
        elif x < self.__x:
            pos_x = 'R'
        if y > self.__y:
            pos_y = 'D'
        elif y < self.__y:
            pos_y = 'U'
        return pos_x + pos_y


# возвращает новые координаты точки, измененные на заданный шаг
def take_step(x, y, pos, step_x, step_y, w, h):
    x_new = x
    y_new = y
    for pos_part in pos:
        if pos_part == 'L':
            x_new = max(x_new - step_x, 0)
        elif pos_part == 'R':
            x_new = min(x_new + step_x, w)
        elif pos_part == 'U':
            y_new = min(y_new + step_y, h)
        else:
            y_new = max(y_new - step_y, 0)
    return x_new, y_new


# возвращает шаги по горизонтали и вертикали, уменьшенные в заданное число раз
def decrease_steps(step_x, step_y, k, prev_pos, pos):
    # если меняем направление по горизонтали, уменьшаем шаг по Х
    if 'L' in pos and 'L' not in prev_pos or 'R' in pos and 'R' not in prev_pos:
        step_x = max(1, int(step_x / k))
    # если по вертикали, то по Y
    if 'U' in pos and 'U' not in prev_pos or 'D' in pos and 'D' not in prev_pos:
        step_y = max(1, int(step_y / k))
    return step_x, step_y


def main():
    # считываем ширину и высоту сетки, координаты стартовой точки
    try:
        w, h = (int(val) for val in input("w h ").split())
        x0, y0 = (int(val) for val in input("x0 y0 ").split())
        if x0 > w or y0 > h:
            raise Exception(f'the point ({x0}, {y0}) is out of range [0, {w}]x[0, {h}]')
    except Exception as e:
        print(e)
        return

    # создаем искомую точку
    SP = SearchPoint(w, h)

    # шаг, на который будем перемещать текущую точку по X и по Y
    step_x = int(w / 2) + 1
    step_y = int(h / 2) + 1
    # коэффициент, на который будем уменьшать шаг
    k = 2
    # шагаем по направлению к искомой точке
    # если направление изменилось, то уменьшаем шаг в k раз
    prev_pos = ""
    while True:
        pos = SP.where_is_point(x0, y0)
        # точка найдена
        if pos == "":
            break
        if prev_pos != "" and pos != prev_pos:
            step_x, step_y = decrease_steps(step_x, step_y, k, prev_pos, pos)
        x0, y0 = take_step(x0, y0, pos, step_x, step_y, w, h)
        print(f'({x0}, {y0})')
        prev_pos = pos

    print(f'desired point is ({x0}, {y0})')


if __name__ == '__main__':
    main()
