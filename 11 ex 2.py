import statistics

stock = {"info": [600, 630, 620], "ril": [1430, 1490, 1567], "mtl": [234, 180, 160]}


def add():
    stock_add = input("Enter stock ticker:")
    stock_add = stock_add.lower()
    stock_price = float(input("Enter ticker price(s): "))
    if stock_add in stock:
        stock[stock_add].append(stock_price)
        print_all()
        return
    stock[stock_add] = [stock_price]
    print_all()


def print_all():
    for stock_add, s in stock.items():
        avg = statistics.mean(s)
        print(f"{stock_add} ==> {s}==> Avg:  ",round(avg,2))


def main():
    op = input("Enter operation (Print or Add): ")
    if op.lower() == "add":
        add()
    elif op.lower() == "print":
        print_all()
    else:
        print("Invalid operation")


if __name__ == '__main__':
    main()
