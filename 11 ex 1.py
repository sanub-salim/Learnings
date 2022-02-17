d = {"china": 143, "india": 136, "usa": 32, "pakistan": 21}


def add():
    country = input("Enter country name to add: ")
    country = country.lower()
    if country in d:
        print(country, "already exists in the dataset")
        return
    population = input(f"Enter population for {country}: ")
    population = float(population)
    d[country] = population
    print_all()


def remove():
    country = input("Enter country name to remove: ")
    country = country.lower()
    if country not in d:
        print(f"{country} doesn't exist in the dataset")
        return
    del d[country]
    print_all()


def query():
    country = input("Enter country name to query: ")
    if country in d:
        print(f"population of {country} is {d[country]} crore")
        return
    print(f"{country} doesn't exist in our dataset")


def print_all():
    for country, p in d.items():
        print(f"{country} ==> {p}")


def main():
    op = input("Enter operation (add, remove, query or print): ")
    if op.lower() == "add":
        add()
    elif op.lower() == "remove":
        remove()
    elif op.lower() == "query":
        query()
    elif op.lower() == "print":
        print_all()


if __name__ == '__main__':
    main()
