def read_csv(csv_file: str) -> list[list[str]]:
    result = []
    with open(csv_file, 'r', encoding='utf-8') as f_in:
        for line in f_in.readlines():
            result.append(line.strip().split(';'))
    return result

7
def to_format(data: list[list[str]]) -> list[dict[str]]:
    data_lst = []
    for record in data:
        user_hash = hash(int(record[1])) + hash(record[2])
        data_lst.append(dict(user_hash=user_hash, user_id=f'{record[1]:0>10}', user_name=record[2].capitalize(),
                             access_level=record[0]))
    return data_lst


def write_json(data: list[dict[str, str]], json_file: str) -> None:
    with open(json_file, 'a', encoding='utf-8') as f_out:
        for line in data:
            f_out.write(str(line) + '\n')


def starter(file_in: str, file_out: str) -> None:
    write_json(to_format(read_csv(file_in)), file_out)


def main():
    file_in_name = 'index.csv'
    file_out_name = 'index_04.json'
    starter(file_in=file_in_name, file_out=file_out_name)


if __name__ == '__main__':
    main()
