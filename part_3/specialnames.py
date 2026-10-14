import collections

# __name__
print("Module name:", __name__)

#__file__
print("File path: ", __file__)

#__package__

print("Package: ",__package__)
print(collections.__package__)

if __name__== "__main__":
    print("This code is being run directly")
