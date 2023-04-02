# -- coding: utf-8 --
import csv
import os
import json
import pickle

info = {}
NAMES = ['file', 'dir', 'mount', 'link', 'something']


def get_info():
    def rec(path_folder: str):
        general_size_ = 0
        files_n_dirs = os.listdir(path_folder)
        # print(f'files_n_dirs: {files_n_dirs}')

        for file_or_dir in files_n_dirs:
            file_or_dir_ = os.path.join(path_folder, file_or_dir)
            if os.path.isdir(file_or_dir_):
                size_ = rec(file_or_dir_)
                info[file_or_dir_] = (path_folder, NAMES[1], size_)
            elif os.path.isfile(file_or_dir_):
                size_ = os.path.getsize(file_or_dir_)
                info[file_or_dir_] = (path_folder, NAMES[0], size_)
            elif os.path.ismount(file_or_dir_):
                size_ = os.path.getsize(file_or_dir_)
                info[file_or_dir_] = (path_folder, NAMES[2], size_)
            elif os.path.islink(file_or_dir_):
                size_ = os.path.getsize(file_or_dir_)
                info[file_or_dir_] = (path_folder, NAMES[3], size_)
            else:
                try:
                    size_ = os.path.getsize(file_or_dir_)
                    info[file_or_dir_] = (path_folder, NAMES[4], size_)
                except:
                    size_ = 0

            general_size_ += size_

        return general_size_
    # print(f'info: {info}')
    rec('C:\\Users\\Евгений\\Desktop\\Обучение')

    with open('info.json', 'w', encoding='utf-8') as f1, \
            open('info.csv', 'w', encoding='utf-8') as f2, \
            open('info.txt', 'wb') as f3:
        # json saving:
        json.dump(info, f1)
        # csv saving:
        writer = csv.writer(f2, dialect='excel', quotechar='|', quoting=csv.QUOTE_NONNUMERIC)
        for item in info.items():
            writer.writerow(item)

        pickle.dump(info, f3)


get_info()

