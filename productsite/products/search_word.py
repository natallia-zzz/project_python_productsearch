def is_part_in_list(str_, words):
    for word in words:
        if str_.lower() in word.lower():
            return word


def main():
    words = ["bags", "shoes", "coats"]
    str_ = input("Введите слово для проверки\n")
    print(is_part_in_list(str_, words))


if __name__ == "__main__":
    main()
