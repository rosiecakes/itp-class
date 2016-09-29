def return_list(num):
    evens = []
    [evens.append(num) for num in range(1, num) if num % 2 == 0]
    return evens
