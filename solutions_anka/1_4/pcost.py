def portfolio_cost(filename):
    total_cost = 0
    with open(filename, "r") as f:
        for line in f:
            share = line.split()
            try:
                total_cost += float(share[1]) * float(share[2])
            except ValueError as e:
                print(" Value can't be parsed.")
    return total_cost
            
data_file = "../../Data/portfolio3.dat"
print(f"tatal cost {portfolio_cost(data_file)}")