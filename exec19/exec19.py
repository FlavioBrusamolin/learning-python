if __name__ == "__main__":
    user = {"name": "Flavio Brito", "age": 20, "number": "(35)987137335", "address": "Rua Dr. Leopoldo de Luna"}
    for key in user:
        print(f'{key.capitalize()}: {user[key]}')