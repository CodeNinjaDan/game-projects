def count_characters(s):
    count = {}
    for i in s:
        if i in count:
            count[i] += 1  # Use += to increment the count for an existing character
        else:
            count[i] = 1
    return count  # Return the count dictionary

word = input("Enter your string: ")
result = count_characters(word)
print(result)