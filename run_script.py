def cumsum(numbers):
    for i in range(1, len(numbers)):
        numbers[i] += sum(numbers[i-1:i])
    return numbers
print(cumsum([1,2,3,4]))