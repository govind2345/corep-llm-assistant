def retrieve_rules():
    with open("data/pra_rules.txt", "r") as f:
        return f.read()
