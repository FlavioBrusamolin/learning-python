def concatenate_tuples(tuple1, tuple2):
    return tuple1 + tuple2


if __name__ == "__main__":
    tuple1 = (1, 2, 3, 4)
    tuple2 = (5, 6, 7, 8)
    new_tuple = concatenate_tuples(tuple1, tuple2)
    print(new_tuple)
