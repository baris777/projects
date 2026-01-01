# Stock Trading Calculator 

# I created this calculator in 2024 as a personal tool to support stock 
# trading decisions. This application allows users to enter partial 
# information about a trade and automatically infers missing values using 
# basic financial relationships.

# buying price = x
# selling price = y
# total buy cost = z
# quantity = a
# growth rate (%) = b
# sell revenue = c
# profit = d

def main():
    print("WELCOME TO THE STOCK TRADING CALCULATOR\n", ("-" * 20), sep="")
    print("You can leave some fields empty. \nThe calculator will try to infer missing values.")
    
    while True:
        x = get_n("\nBuying Price: ", positive=True)
        y = get_n("Selling price: ", positive=True)
        z = get_n("Total buy cost: ")
        a = get_n("Quantity: ", positive=True)
        b = get_n("Growth rate %: ")

        result = calculator(x=x, y=y, z=z, a=a, b=b)

        print("\nResults\n", ("-" * 20), sep="")
        print(f"Buying Price: ${result['x']:,.2f}" if result['x'] is not None else "Buying Price: —")
        print(f"Selling Price: ${result['y']:,.2f}" if result['y'] is not None else "Selling Price: —")
        print(f"Total Buy Cost: ${result['z']:,.2f}" if result['z'] is not None else "Total Buy Cost: —")
        print(f"Quantity: {result['a']:,.2f}" if result['a'] is not None else "Quantity: —")
        print(f"Growth Rate %: {result['b']:,.2f}%" if result['b'] is not None else "Growth Rate %: —")
        print(f"Sell Revenue: ${result['c']:,.2f}" if result['c'] is not None else "Sell Revenue: —")
        print(f"Profit: ${result['d']:,.2f}" if result['d'] is not None else "Profit: —")

        while True:
            choice = input("\nPlease press q to quit or press y to continue!\n").strip().lower()
            if choice == "q":
                return
            elif choice == "y":
                break
            else:
                print("Please use the right key.")
                continue

def calculator(x=None, y=None, z=None, a=None, b=None):
    if a is None and x is not None and z is not None and x != 0:
        a = z / x
    if z is None and x is not None and a is not None:
        z = x * a
    if x is None and z is not None and a is not None and a != 0:
        x = z / a
    if y is None and b is not None and x is not None:
        y = x * (1 + b / 100)
    if b is None and x is not None and y is not None and x != 0:
        b = ((y - x) / x) * 100
    if y is not None and a is not None:
        c = y * a
    else:
        c = None
    if c is not None and z is not None:
        d = c - z
    else:
        d = None

    return {"x":x , "y":y, "z":z, "a":a, "b":b, "c":c, "d":d}

def get_n(prompt, positive=False):
    while True:
        value = input(prompt).strip()

        if value == "":
            return None

        try:
            num = float(value)

            if positive and num <= 0:
                print("Value must be positive.")
                continue

            return num

        except ValueError:
            print("Please enter a valid number!")

if __name__ == "__main__":
    main()