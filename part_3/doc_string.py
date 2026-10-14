
show_expected_result = True
show_hits            = True

numbers = input("")
def find_largest(numbers):

    return max(numbers)

def main():
    numbers = list(map(int, input().split()))
    print(find_largest(numbers))


if __name__ =="__main__":
    main()