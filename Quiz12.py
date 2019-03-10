def quicksort(animal):
    if len(animal) < 2:
        return animal
    else:
        pivot = animal[0]
        border = 0
        for x in range(len(animal)-1):
            if animal[x + 1] < pivot:
                animal[x + 1],animal[border +1 ] = animal[border + 1], animal[x + 1]
                border += 1
        animal[0],animal[border] = animal[border],animal[0]
        placeholder = quicksort(animal[:border])
        placeholder1 = quicksort(animal[border + 1:])
        placeholder.append(animal[border])
        return placeholder + placeholder1

def file():
    zoo = open("input.txt", "r")
    code = zoo.readlines()
    bcode = list(code)
    for i in bcode:
        if "\n" in i:
            i.strip("\n")
    return bcode

def main():
    alist = file()
    alist2 = []
    alist3 = []
    for creature in alist:
        if("\n" in creature):
            creature2 = creature.strip("\n")
            #print(creature2)
            alist2.append(creature2)
            alist3 = [creature2.capitalize() for creature2 in alist2]

    print(quicksort(alist3))

main()