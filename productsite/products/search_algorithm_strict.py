def is_search_in_row_strict(search, row):
    print(row.split())
    count = 0
    for word in search.split():
        for elem in row.split():
            if word.lower() == elem.lower():
                count += 1
    if count == len(search.split()):
        return True
    else:
        return False

def main():
    search = input("Введите слово для проверки\n")
    f = open("rows.txt", "r")
    for x in f:
        print(is_search_in_row_strict(search, x))
    f.close()


if __name__ == "__main__":
    main()