def load_env():
    d = {}

    with open(".env", 'r') as file:
        contents = file.read().split("\n")

    for line in contents:
        k, v = line.split("=")
        try:
            d[k] = v
        except Exception:
            print("Invalid key!")

    return d


if __name__ == "__main__":
    load_env()