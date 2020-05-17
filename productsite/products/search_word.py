def is_part_in_list(str_, words):
    for word in words:
        if str_.lower() in word.lower():
            return word
    return "Nothing is found"


def main():
    str_ = 0
    while str_ != 'exit':
        words = ["bags chanel", "shoes gucci", "coats versace"]
        str_ = input("Введите слово для проверки или exit, чтобы выйти\n")
        if str_ == 'exit':
            break
        else:
            print(is_part_in_list(str_, words))


if __name__ == "__main__":
    main()
