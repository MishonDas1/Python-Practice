def count_even_odd(numbers):
  """Counts the number of even and odd numbers in a list.

  Args:
    numbers: A list of numbers.

  Returns:
    A tuple containing the count of even numbers and the count of odd numbers.
  """
  even_count = 0
  odd_count = 0
  for number in numbers:
    if number % 2 == 0:
      even_count += 1
    else:
      odd_count += 1
  return even_count, odd_count

def remove_duplicates(numbers):
  """Removes duplicate numbers from a list.

  Args:
    numbers: A list of numbers.

  Returns:
    A new list with duplicate numbers removed.
  """
  return list(set(numbers))

# Example usage:
my_list = [1, 2, 3, 4, 5, 5, 6, 7, 8, 8, 9, 10]

# Count even and odd numbers
even_count, odd_count = count_even_odd(my_list)
print(f"Even numbers: {even_count}")
print(f"Odd numbers: {odd_count}")

# Remove duplicates
unique_list = remove_duplicates(my_list)
print(f"List with duplicates removed: {unique_list}")
