import hashlib
text = input('enter the word to find md5 : ')
result = hashlib.md5(text.encode())
print(result.hexdigest())