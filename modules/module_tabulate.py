from tabulate import tabulate


data = [["Name", "Age"], ["Alice", 30], ["Bob", 25]]

print(tabulate(data, headers="firstrow", tablefmt="heavy_grid"))