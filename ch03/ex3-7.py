names = ["eric", "tom", "jim", "xiaoming"]

print("I will invite " + names[0] + " to dinner with me.")
print("I will invite " + names[1] + " to dinner with me.")
print("I will invite " + names[2] + " to dinner with me.")
print("I will invite " + names[3] + " to dinner with me.")

print("\n" + names[3] + " have no time to dinner with me.\n")

names[3] = "tony"
print("I will invite " + names[0] + " to dinner with me.")
print("I will invite " + names[1] + " to dinner with me.")
print("I will invite " + names[2] + " to dinner with me.")
print("I will invite " + names[3] + " to dinner with me.")

print("\nI find a more bigger dinner table, so I will invite more guest.\n")

names.insert(0, "steven")
names.insert(2, "nicoal")
names.append("jery")
print("I will invite " + names[0] + " to dinner with me.")
print("I will invite " + names[1] + " to dinner with me.")
print("I will invite " + names[2] + " to dinner with me.")
print("I will invite " + names[3] + " to dinner with me.")
print("I will invite " + names[4] + " to dinner with me.")
print("I will invite " + names[5] + " to dinner with me.")
print("I will invite " + names[6] + " to dinner with me.")

print("\nI will only invite two guests to dinner with me.\n")

name = names.pop()
print(name + ", I'm so sorry, I can't invite you to dinner with me.")

name = names.pop()
print(name + ", I'm so sorry, I can't invite you to dinner with me.")

name = names.pop()
print(name + ", I'm so sorry, I can't invite you to dinner with me.")

name = names.pop()
print(name + ", I'm so sorry, I can't invite you to dinner with me.")

name = names.pop()
print(name + ", I'm so sorry, I can't invite you to dinner with me.")

print(names[0] + ", I invite you to dinner with me yet.")
print(names[1] + ", I invite you to dinner with me yet.")

del names[1]
del names[0]
print("guest list: ", names)
