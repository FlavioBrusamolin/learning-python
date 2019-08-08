def verify_string(tuple_example):
    for iterator in tuple_example:
        if type(iterator) == str:
            print('String encontrada: ', iterator)


def create_composite_tuple():
    composite_tuple = ((1, 2, 3, 4, 5, 'a', 'b', 3.2, 2), ('asde', 4.2, 'v', 5, 6, ['a', 3]), (3, 1, 0, 'asde', 'a', (3, 4, 'f')))
    return composite_tuple


if __name__ == "__main__":
    composite_tuple = create_composite_tuple()
    for tuple_example in composite_tuple:
        verify_string(tuple_example)
