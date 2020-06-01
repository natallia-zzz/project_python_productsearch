def is_search_in_row(search, row):
    print(row.split())
    for word in search.split():
        if word.lower() in row.lower():
            return True
    return False

def main():
    search = input("Введите слово для проверки\n")
    f = open("rows.txt", "r")
    for x in f:
        print(is_search_in_row(search, x))
    f.close()


if __name__ == "__main__":
    main()