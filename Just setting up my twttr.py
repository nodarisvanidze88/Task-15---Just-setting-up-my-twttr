vowel = ["A", "E", "I", "O", "U", "a", "e", "i", "o", "u"]

user = input("Input: ").strip()
for i in user:
    if i in vowel:
        user = user.replace(i, "")

print(user)
