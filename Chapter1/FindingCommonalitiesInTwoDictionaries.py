# Created by Admin at 5/8/2022
a = {
    'x': 1,
    'y': 2,
    'z': 3
}
b = {
    'w': 10,
    'x': 11,
    'y': 2
}
a.keys() & b.keys()
a.keys() - b.keys()
a.items() & b.items()
c = {key: a[key] for key in a.keys() - {'z', 'w'}}
