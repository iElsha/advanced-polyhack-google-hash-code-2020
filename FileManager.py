from random import random


def parse(path):
    with open(path) as file:
        data = []
        for row in file.read().split("\n"):
            object = []
            for col in row.strip().split(" "):
                if col.isdigit():
                    object.append(int(col))
                elif col.isdecimal():
                    object.append(float(col))
                else:
                    object.append(col)
            data.append(object)
        return data


def output(path, data):
    file_name = path[
                path.rfind('/') + 1 if path.rfind('/') >= 0 else 0:
                path.rfind('.') - 1 if path.rfind('.') >= 0 else len(path)
                ]
    with open("res_files/" + file_name + "_" + str(random()) + ".out", "w") as out:
        for row in data:
            for col in row:
                out.write(str(col))
            out.write("\n")

