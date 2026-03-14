def read_file_contents(file_path: str):
    try:
        with open(file_path, 'r') as file:
            data = file.read()
            print(data)
    except FileNotFoundError:
        print(f"File not found - {file_path}")