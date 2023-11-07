import sys


def txt_importer(path_file):
    if not path_file.endswith('txt'):
        return sys.stderr.write('Formato inválido')
    try:
        with open(path_file, mode="r") as file:
            data_file = file.read().splitlines()
            return data_file
    except FileNotFoundError:
        return sys.stderr.write(f'Arquivo {path_file} não encontrado\n')
