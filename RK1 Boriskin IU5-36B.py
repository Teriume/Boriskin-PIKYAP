from operator import itemgetter


class HDD:
    def __init__(self, id, model, capacity, price, surname, comp_id):
        self.id = id
        self.model = model
        self.capacity = capacity
        self.price = price
        self.surname = surname
        self.comp_id = comp_id


class Computer:
    def __init__(self, id, name):
        self.id = id
        self.name = name


class HDDComputer:
    def __init__(self, comp_id, hdd_id):
        self.comp_id = comp_id
        self.hdd_id = hdd_id


computers = [
    Computer(1, 'Альфа-ПК'),
    Computer(2, 'Игровой ПК'),
    Computer(3, 'Офисный ПК'),
    Computer(4, 'Архивный ПК'),
]


hdds = [
    HDD(1, 'Seagate Barracuda', 1000, 5000, 'Иванов', 1),
    HDD(2, 'WD Blue', 2000, 7000, 'Петров', 1),
    HDD(3, 'Toshiba P300', 1000, 4500, 'Сидорова', 2),
    HDD(4, 'Samsung 870 EVO', 2000, 6000, 'Кузнецов', 2),
    HDD(5, 'Kingston A400', 500, 3500, 'Иваненко', 3),
]


hdds_computers = [
    HDDComputer(1, 1),
    HDDComputer(1, 2),
    HDDComputer(1, 3),
    HDDComputer(2, 2),
    HDDComputer(2, 3),
    HDDComputer(3, 4),
    HDDComputer(4, 1),
    HDDComputer(4, 5),
    HDDComputer(4, 2),
]


def main():

    one_to_many = [
        (h.model, h.surname, h.price, c.name)
        for c in computers
        for h in hdds
        if h.comp_id == c.id
    ]

    many_to_many_temp = [
        (c.name, link.comp_id, link.hdd_id)
        for c in computers
        for link in hdds_computers
        if c.id == link.comp_id
    ]

    many_to_many = [
        (h.model, h.price, comp_name)
        for comp_name, comp_id, hdd_id in many_to_many_temp
        for h in hdds
        if h.id == hdd_id
    ]

    print('Задание Д1')

    res_11 = [
        (model, comp_name)
        for model, surname, price, comp_name in one_to_many
        if surname.endswith('ов')
    ]

    print(res_11)

    print('\nЗадание Д2')

    res_12_unsorted = []

    for c in computers:

        c_hdds = list(
            filter(lambda i: i[3] == c.name, one_to_many)
        )

        if len(c_hdds) > 0:

            c_prices = [price for _, _, price, _ in c_hdds]

            c_prices_sum = sum(c_prices)

            c_prices_avg = c_prices_sum / len(c_prices)

            res_12_unsorted.append((c.name, c_prices_avg))

    res_12 = sorted(
        res_12_unsorted,
        key=itemgetter(1),
        reverse=True
    )

    print(res_12)

    print('\nЗадание Д3')

    res_13 = {}

    for c in computers:

        if c.name.startswith('А'):

            c_hdds = list(
                filter(lambda i: i[2] == c.name, many_to_many)
            )

            c_hdds_names = [x for x, _, _ in c_hdds]

            res_13[c.name] = c_hdds_names

    print(res_13)


if __name__ == '__main__':
    main()