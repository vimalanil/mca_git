def reverse_name(full_name):
    words = full_name.split()
    reversed_words = ' '.join(words[::-1])
    return reversed_words

# Example
name = input("Enter full name: ")
print("Reversed order:", reverse_name(name))
