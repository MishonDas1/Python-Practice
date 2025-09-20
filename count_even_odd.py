def count_even_odd(input_list):
    even_count = sum(1 for x in input_list if x % 2 == 0)
    odd_count = sum(1 for x in input_list if x % 2 != 0)
    return even_count, odd_count

def remove_duplicates(input_list):
    return list(set(input_list))

numbers_list = [10, 20, 30, 40, 50, 60, 70, 71, 72, 73]
even, odd = count_even_odd(numbers_list)

print(f"The list is: {numbers_list}")
print(f"Number of even numbers: {even}")
print(f"Number of odd numbers: {odd}")

duplicate_list = [50, 60, 70, 80, 90, 100, 50, 60, 70]
unique_list = remove_duplicates(duplicate_list)

print(f"List with duplicates removed: {unique_list}")
