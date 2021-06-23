string = input("Enter words and seperate them by comma : "  )
#print(string)
word = [word for word in string.split(",")]

print(",".join(sorted(list(set(word)))))