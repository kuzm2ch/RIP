# используется для сортировки
from operator import itemgetter


class Prog:
    """Программа"""
    def __init__(self, id, appName, cost, comp_id):
        self.id = id
        self.appName = appName
        self.cost = cost
        self.comp_id = comp_id


class Comp:
    """Компьютер"""
    def __init__(self, id, name):
        self.id = id
        self.name = name


class ProgComp:
    """
    'Ученики класса' для реализации
    связи многие-ко-многим
    """
    def __init__(self, prog_id, comp_id):
        self.prog_id = prog_id
        self.comp_id = comp_id


# Классы
comps = [
    Comp(1, 'PC1'),
    Comp(2, 'PC2'),
    Comp(3, 'PC3'),
    Comp(4, 'PC4'),
]

# Ученики
progs = [
    Prog(1, 'Zoom', 0, 1),
    Prog(2, 'Kaspersky Anti-Virus', 3300, 2),
    Prog(3, 'Photoshop', 5000, 3),
    Prog(4, 'Discord', 0, 3),
    Prog(5, 'WinRAR', 1000, 4),
]

progs_comps = [
    ProgComp(1, 1),
    ProgComp(2, 2),
    ProgComp(3, 3),
    ProgComp(4, 4),
    ProgComp(5, 4),
]


def main():
    """Основная функция"""

    # Соединение данных один-ко-многим
    one_to_many = [(s.appName, s.cost, k.name)
                   for k in comps
                   for s in progs
                   if s.comp_id == k.id]

    # Соединение данных многие-ко-многим
    many_to_many_temp = [(k.name, sk.comp_id, sk.prog_id)
                         for k in comps
                         for sk in progs_comps
                         if k.id == sk.comp_id]

    many_to_many = [(s.appName, s.cost, comp_name)
                    for comp_name, comp_id, prog_id in many_to_many_temp
                    for s in progs if s.id == prog_id]

    print('Задание Г1')
    res_11 = [(s.appName, k.name)
                for k in comps
                for s in progs
                if (s.comp_id == k.id) and (k.name == "PC1" or k.name == "PC2")]
    print(res_11)


    print('\nЗадание Г2')
    res_12_unsorted = []

    for k in comps:

        k_progs = list(filter(lambda i: i[2] == k.name, one_to_many))

        if len(k_progs) > 0:

            k_costs = [cost for _, cost, _ in k_progs]

            k_costs_max = max(k_costs)
            res_12_unsorted.append((k.name, k_costs_max))


    res_12 = sorted(res_12_unsorted, key=itemgetter(1), reverse=True)
    print(res_12)

    print('\nЗадание Г3')
    res_13 = sorted(many_to_many, key=itemgetter(2))
    print(res_13)



if __name__ == '__main__':
    main()