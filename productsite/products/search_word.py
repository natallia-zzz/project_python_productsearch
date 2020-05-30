def is_part_in_list(str_, words):
    for word in words:
        for elem in word:
            if str_.lower() in elem.lower():
                return elem
    return "Nothing is found"


def main():
    str_ = 0
    while str_ != 'exit':
        words = [["bags chanel", "shoes gucci", "coats versace"], ["hat zara", "dress LoveRepublic"]]
        str_ = input("Введите слово для проверки или exit, чтобы выйти\n")
        if str_ == 'exit':
            break
        else:
            print(is_part_in_list(str_, words))


if __name__ == "__main__":
    main()
