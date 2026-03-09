def create_file(name):
    with open(name, "w") as f:
        pass
    print("File created successfully.")

def write_file(name, data):
    with open(name, "w") as f:
        f.write(data)
    print("Data written successfully.")

def read_file(name):
    try:
        with open(name, "r") as f:
            print("File Content:")
            print(f.read())
    except:
        print("File not found.")

def append_file(name, data):
    with open(name, "a") as f:
        f.write("\n" + data)
    print("Data appended successfully.")