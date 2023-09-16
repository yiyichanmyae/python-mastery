data_directory = "../../Data/portfolio.dat"

total_cost = 0
with open(data_directory, "r") as f:
    for line in f:
        share = line.split()
        total_cost += float(share[1]) * float(share[2])
        
print(f"tatal cost {total_cost}")