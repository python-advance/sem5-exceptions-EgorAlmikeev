TABS = 1
TAB_CHAR = "|___"


def print_list(col_index: int, list_data: list):
    print(TAB_CHAR * TABS * col_index, "list begins")
    for i in list_data:
        i_type = type(i)
        if i_type == dict:
            print_json(col_index + 1, i)
        elif i_type == list:
            print_list(col_index + 1, i)
        else:
            print(TAB_CHAR * TABS * col_index, i)
    print(TAB_CHAR * TABS * col_index, "list ends")


def print_json(col_index: int, json_data: dict):
    for item in json_data.items():
        key = item[0]
        value = item[1]

        v_type = type(value)

        if v_type == dict:
            print(TAB_CHAR * TABS * col_index, key, ":")
            print_json(col_index + 1, value)
        elif v_type == list:
            print(TAB_CHAR * TABS * col_index, key, ":")
            print_list(col_index + 1, value)
        else:
            print(TAB_CHAR * TABS * col_index, key, ":", value)


if __name__ == "__main__":
    from json import *
    import json

    json_data: dict

    with open("./sample_json.json", "r") as file:
        try:
            json_data = json.load(file)
        except JSONDecodeError:
            print("Not a JSON file")
            exit(-1)

    print_json(0, json_data)