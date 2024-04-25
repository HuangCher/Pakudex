from pakuri import Pakuri

class Pakudex:
    def __init__(self, capacity = 20):
        self.capacity = capacity
        self.items = []

    # gets the number of pakuris in our list
    def get_size(self):
        return len(self.items)

    # this gets the capacity the user inputs
    def get_capacity(self):
        return self.capacity

    # the list of names for our species
    def get_species_array(self):
        if len(self.items) >= 1:
            names = []
            for i in self.items:
                names.append(i.get_species())
            return names
        else:
            return None

    # gives the states of a given pakuri
    def get_stats(self, species):
        for i in self.items:
            stats = []
            if i.get_species() == species:
                stats.append(i.get_attack())
                stats.append(i.get_defense())
                stats.append(i.get_speed())
                return stats
        return None

    # sorts the pakuri in order alphabetically
    def sort_pakuri(self):
        self.items.sort()

    # adds a pakuri to our list of items if the pakuri not already in the list
    def add_pakuri(self, species):
        for i in self.items:
            if i.get_species() == species:
                return False
        self.items.append(Pakuri(species))
        return True

    # evolves a given pakuri
    def evolve_species(self, species):
        for i in self.items:
            if i.get_species() == species:
                i.evolve()
                return True
        return False