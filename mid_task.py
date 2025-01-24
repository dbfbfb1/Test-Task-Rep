def count_duplicates(numbers):
    count_dict = {}

    for number in numbers:
        if number in count_dict:
            count_dict[number] += 1
        else:
            count_dict[number] = 1

    return count_dict

numbers = [1, 2, 2, 3, 3, 3, 4, 5, 5, 5, 5]
result = count_duplicates(numbers)

for number, count in result.items():
    print(f"{number} встречается {count} раз." if count == 1 else f"{number} встречается {count} раза.")