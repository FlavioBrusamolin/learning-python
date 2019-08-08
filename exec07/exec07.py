def readAllNotes(notes_quantity):
    all_notes = []
    for iterator in range(notes_quantity):
        note = int(input(f'Entre com a nota do aluno {iterator + 1}: '))
        all_notes.append(note)
    return all_notes


def checkClassPerformance(all_notes):
    for note in all_notes:
        if note <= 70:
            print('Turma de baixa performance')
            break
    else:
        print('Turma de alta performance')


if __name__ == '__main__':
    notes_quantity = int(input('Entre com a quantidade de notas da turma: '))
    all_notes = readAllNotes(notes_quantity)
    checkClassPerformance(all_notes)
