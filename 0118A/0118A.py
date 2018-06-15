import string

vovels = {"A", "O", "Y", "E", "U", "I", "a", "o", "y", "e", "u", "i"}
consonants = (set(string.ascii_uppercase) | set(string.ascii_lowercase)) - vovels
print(''.join([ch for ch in ['.' + ch.lower() if ch in consonants else ch for ch in input()] if ch not in vovels]))
