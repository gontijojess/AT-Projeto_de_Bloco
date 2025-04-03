class Estudante:
    def __init__(self, nome, nota):
        self.nome = nome
        self.nota = nota

    def __repr__(self):
        return f"{self.nome}: {self.nota}"

def partition(array, low, high):
    pivot = array[high].nota
    i = low - 1
    for j in range(low, high):
        if array[j].nota <= pivot:
            i = i + 1
            (array[i], array[j]) = (array[j], array[i])
    (array[i + 1], array[high]) = (array[high], array[i + 1])
    return i + 1

def quickSort(array, low, high):
    if low < high:
        pi = partition(array, low, high)
        quickSort(array, low, pi - 1)
        quickSort(array, pi + 1, high)

estudantes = [
    Estudante("Ana", 9.7),
    Estudante("Marcos", 7.3),
    Estudante("Mariana", 5.5),
    Estudante("Luis", 6.0),
    Estudante("Lucas", 10.0),
    Estudante("Lucas", 10.0)
]

print("Antes da ordenação:")
print(estudantes)

quickSort(estudantes, 0, len(estudantes) - 1)

print("\nDepois da ordenação:")
print(estudantes)