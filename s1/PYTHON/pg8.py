# Longest word from comma separated list.

words = input("Enter words seperated by comma").split(",")
longest = max(words,key=len)
print("Longest word: ",longest)