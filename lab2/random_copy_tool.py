import csv
import os
from random import randint


def copy_to_new_dir_with_random_naming(path_old: str, path_new: str) -> None:
    """
    Функция копирования исходного датасета в новую директорию с присваиванием случайного номера.
    Также, чтобы не потерять метку класса, создаёт файл-аннотацию для нового датасета.
    :param path_old: путь к старому датасету
    :param path_new: путь к новому расположению датасета
    :return: None
    """
    columns = ("Path1", "Path2", "Class")
    with open("data2.csv", "w") as file:
        writer = csv.writer(file, delimiter=";")
        writer.writerow(columns)
        for directory_name in os.listdir(path_old):
            directory = os.path.join(path_old, directory_name)
            for files in os.listdir(directory):
                path = os.path.join(directory, files)
                if os.path.isfile(path) and path.endswith(".txt"):
                    new_name = "".join([str(randint(0, 9999)).zfill(4), ".txt"])
                    rev_type = path[-12: -10]
                    if rev_type == "bad":
                        full_path = os.path.join(path_new, new_name)
                        file_info = (full_path, "".join([path_new, new_name]), rev_type)
                        writer.writerow(file_info)
                    else:
                        rev_type = path[-13: -10]
                        full_path = os.path.join(path_new, new_name)
                        file_info = (full_path, "".join([path_new, new_name]), rev_type)
                        writer.writerow(file_info)
                    f = open(path, "r")
                    content = f.read()
                    f.close()
                    f = open(full_path, "w")
                    f.write(content)
                    f.close()
