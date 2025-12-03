def read_file(filepath: str) -> str:
    with open(filepath, 'r') as file:
        out = file.read()
        file.close()
        return out