import os
from tempfile import NamedTemporaryFile
import random


def generate_big_file(filename):
    with open(filename, 'w') as f:
        f.writelines('{}\n'.format(random.randint(-1000000, 1000000)) for _ in range(1000000))


def merge_files(filename1, filename2):
    f1 = open(filename1, 'r+')
    f2 = open(filename2, 'r+')
    f3, name = create_file()

    pointer1 = f1.readline()
    pointer2 = f2.readline()

    while True:

        if pointer1 == '\n':
            pointer1 = f1.readline()
        if pointer2 == '\n':
            pointer2 = f2.readline()

        if pointer1 == "" and pointer2 == "":
            break

        if pointer1 == "":
            f3.writelines(pointer2)
            pointer2 = f2.readline()
        elif pointer2 == "":
            f3.writelines(pointer1)
            pointer1 = f1.readline()
        else:
            if int(pointer1) < int(pointer2):
                f3.writelines(pointer1)
                pointer1 = f1.readline()
            else:
                f3.writelines(pointer2)
                pointer2 = f2.readline()

    f1.close()
    f2.close()
    f3.close()

    delete_file(filename1)
    delete_file(filename2)

    return name


def is_sorted(filename):
    with open(filename) as file:
        previous_line = ""

        for current_line in file:
            if previous_line != "" and int(current_line) < int(previous_line):
                return False

            previous_line = current_line

    return True


def delete_files(file_list):
    for filename in file_list:
        if os.path.exists(filename):
            os.unlink(filename)


def delete_file(filename):
    os.unlink(filename)


def create_file():
    f = NamedTemporaryFile(delete=False, mode='w+t')
    return f, f.name


def create_files(array_size, input_file_name):
    group_size = array_size
    file_list = []

    f, filename = create_file()
    file_list.append(filename)

    current_size = 0
    with open(input_file_name) as input_file:
        for current_number in input_file:
            if current_size == group_size:
                current_size = 0
                f.close()
                f, filename = create_file()
                file_list.append(filename)

            f.writelines(current_number)
            current_size += 1

    return file_list


def sort_data(filename):
    with open(filename, 'r+') as f:

        data_list = []
        for number in f:
            data_list.append(int(number))

        f.seek(0)
        f.truncate(0)
        data_list.sort()

        for number in data_list:
            f.write(str(number) + '\n')


def sort_files(file_list):
    for filename in file_list:
        sort_data(filename)


def merge_file_list(filenames):
    idx = 0
    new_files = []

    while idx < len(filenames):
        if idx == len(filenames) - 1:
            new_files.append(filenames[idx])
            idx += 1
        else:
            new_files.append(merge_files(filenames[idx], filenames[idx + 1]))
            idx += 2

    return new_files


def sort(input_data, output):
    files = create_files(300000, input_data)

    sort_files(files)
    while len(files) > 1:
        merged_files = merge_file_list(files)
        files.clear()
        for file in merged_files:
            files.append(file)

    with open(output, 'w') as f:
        with open(files[0], 'r+') as data:
            for number in data:
                f.write(number)

    if not is_sorted(output):
        raise IOError

    delete_files(files)
