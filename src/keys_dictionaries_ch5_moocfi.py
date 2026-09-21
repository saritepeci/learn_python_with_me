# Mooc.fi CH5 dictionary
results = {"John":63, "Anne":34}
results["Peter"] = 50
results["Nia"] = 80

results["Peter"] = 70 # not new item, uptadet value

print(results)
print(results["Nia"])
#print(results["Bob"]) #KeyError: 'Bob'

############# Tuple
# 
# Tuple is immutable. unchangeable
coordinates = (230, 452)
