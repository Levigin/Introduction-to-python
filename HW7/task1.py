import os


def group_rename(file_name: str, count_rename: int, extension_in: str = 'txt', extension_out: str = 'dll',
                 name_range: tuple = (2, 4)):
    dir_list = os.listdir()
    min_, max_ = name_range

    for i, file in enumerate(dir_list, start=1):
        name, ext = file.split('.')
        if ext == extension_in:
            print(f'ext: {ext}')
            sequence_number = '0' * (count_rename - len(str(i))) + str(i)
            os.rename(file, (name[min_: max_ + 1] if min_ <= len(
                          name) <= max_ else name) + file_name + sequence_number + f'.{extension_out}')


group_rename('task', 4)
