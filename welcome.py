#  greet a website user in their language


db = {'english': 'Welcome','czech': 'Vitejte','danish': 'Velkomst',
        'dutch': 'Welkom','estonian': 'Tere tulemast','finnish': 'Tervetuloa',
        'flemish': 'Welgekomen','french': 'Bienvenue', 'german': 'Willkommen',
        'irish': 'Failte', 'italian': 'Benvenuto', 'latvian': 'Gaidits',
        'lithuanian': 'Laukiamas','polish': 'Witamy', 'spanish': 'Bienvenido',
        'swedish': 'Valkommen', 'welsh': 'Croeso'}

def greet(language):
    try:
        return db[language]
    except:
        return db['english']


def greet2(language):
    """"""
    db.get(language,'Welcome')


test1 = print(greet('english'))
test2 = print(greet('french'))
test3 = print(greet(2))
