def file_path(path: str) -> tuple[str, str, str]:
    temp = path.split('\\')
    a, b = tuple(temp[-1].split('.'))
    result = '\\'.join(temp[:-2]), a, b
    return result


print(file_path(r"C:\Program Files\Unity\Hub\Editor\Readme.txt"))
