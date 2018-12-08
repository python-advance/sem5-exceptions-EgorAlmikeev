def read_json():
    import json
    j_rules = """
    Вводите пары ключ-значение по одной за раз, разделяя ключ и значение запятой.
    Введите __STOP__ чтобы прекратить ввод.
    """
    print(j_rules)

    json_data = {}
    next_line = ""

    while next_line != "__STOP__":
        next_line = input("Следующая пара: ")
        try:
            [k, v] = next_line.split(", ")
        except ValueError:
            continue
        json_data.update({k: v})

    with open("json_output.json", "w") as file:
        file.write("\n")
        if len(json_data) != 0:
            file.write(json.dumps(json_data, indent=4))
        else:
            print("Nothing to write")


def read_csv():
    csv_rules = """
    Вводите данные построчно, разделяя столбцы запятыми.
    Введите __STOP__ чтобы прекратить ввод.
    """
    print(csv_rules)

    data = ""
    next_line = ""

    while next_line != "__STOP__":
        next_line = input("Следующая строка: ")
        data += next_line + "\n"

    with open("csv_output.csv", "w") as file:
        if len(data) != 0:
            file.write(data)
        else:
            print("Nothing to write")


if __name__ == "__main__":
    print("1. JSON\n2. CSV")
    a = int(input("set: "))

    if a == 1:
        read_json()
    elif a == 2:
        read_csv()
    else:
        print("Exit.")
