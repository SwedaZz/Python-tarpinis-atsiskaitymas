# Sukurkite klasę "Movie", kuri gebės sukurti objektus 3 savybėm ir 1 metodu. 
# Naudojant šią klasę sukurkite bent du skirtingus objektus.

# Savybės:
# title: string
# director: string
# budget: number

# Metodas: 
# was_expensive() - jeigu filmo "budget" yra daugiau nei 100 000 000 mln USD, tada grąžins True, kitu atveju False.

class Movie:
    def __init__(self, title, director, budget):
        self.title = title
        self.director = director
        self.budget = budget

    def __str__(self):
        return f'Informacija apie filmą - Pavadinimas "{self.title}", Režisierius {self.director}, Biudžetas {self.budget} €'

    def was_expensive(self):
        if self.budget > 100000000:
            return True
        else:
            return False

filmas1 = Movie('Good guy', 'Tadas Sved', 200000000)

print(filmas1)

print('Buvo brangus:',filmas1.was_expensive())

filmas2 = Movie('Cheap guy', 'Tadas Sved', 20000000)

print(filmas2)

print('Buvo brangus:',filmas2.was_expensive())