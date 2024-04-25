from pakudex import Pakudex

def main():
    print("Welcome to Pakudex: Tracker Extraordinaire!")
    while True:
        try:
            capacity = int(input("Enter max capacity of the Pakudex: "))
            if capacity < 1:
                print("Please enter a valid size.")
            else:
                print(f"The Pakudex can hold {capacity} species of Pakuri.")
                break
        except:
            print("Please enter a valid size.")

    pakudex = Pakudex(capacity)

    while True:
        while True:
            try:
                choice = int(input("\nPakudex Main Menu\n-----------------\n1. List Pakuri\n2. Show Pakuri\n3. Add Pakuri\n4. Evolve Pakuri\n5. Sort Pakuri\n6. Exit\nWhat would you like to do? "))
                break
            except:
                print("Unrecognized menu selection!")

        if choice == 1:
            if pakudex.get_species_array():
                print("Pakuri In Pakudex: ")
                for i in range(len(pakudex.get_species_array())):
                    print(f"{i+1}.{pakudex.get_species_array()[i]}")
            else:
                print("No Pakuri in Pakudex yet!")

        elif choice == 2:
            name = input("Enter the name of the species to display: ")
            if pakudex.get_stats(name) == None:
                print("Error: No such Pakuri!")
            else:
                print(f"\nSpecies: {name}")
                print(f"Attack: {pakudex.get_stats(name)[0]}\nDefense: {pakudex.get_stats(name)[1]}\nSpeed: {pakudex.get_stats(name)[2]}")

        elif choice == 3:
            if pakudex.get_size() == capacity:
                print("Error: Pakudex is full!")
            else:
                species = input("Enter the name of the species to add: ")
                if pakudex.add_pakuri(species) == True:
                    print(f"Pakuri species {species} successfully added!")
                else:
                    print("Error: Pakudex already contains this species!")

        elif choice == 4:
            name = input("Enter the name of the species to evolve: ")
            if pakudex.get_stats(name) == None:
                print("Error: No such Pakuri!")
            else:
                pakudex.evolve_species(name)
                print(f"{name} has evolved!")

        elif choice == 5:
            pakudex.sort_pakuri()
            print("Pakuri have been sorted!")

        elif choice == 6:
            print("Thanks for using Pakudex! Bye!")
            exit()

        else:
            print("Unrecognized menu selection!")

if __name__ == "__main__":
    main()




