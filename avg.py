def avg(list1):
    result = 0
    for number in list1:
        result += number
    return result / len(list1)  # Divide sum by length

print(avg([1, 2, 3, 4, 5]))  # Output: 3.0