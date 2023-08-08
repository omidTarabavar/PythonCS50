"""
Multi
line
comment
"""

# Ask user for their name
name = input("What's your name? ")

# Say hello to user
print("hello,")
print(name)

print("hello, "+name)
print("hello,",name) # it automatically insert space when doing this

print("hello, ", end ="")
print(name)

print("hello",name,sep = "???")
print('hello, "friend"')  # fix1 for corner case
print("hello, \"friend\"") # fix2 for corner case

print(f"hello, {name}")