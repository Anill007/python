text = "क"
changed = text.encode('utf-8')
print(changed)

text = b'\xe0\xa4\x95'
changed = text.decode('utf-8')
print(changed)

strs = []

for i in range(5):
    temp = input("Enter string:")
    strs.append(temp)

# for i in strs:
#     print(type(i))

for i in strs:
    print(i)
