import random
import string

# Generate 3 random letters
def random_chars():
    return ''.join(random.choice(string.ascii_letters) for _ in range(3))

# Encode function
def encode(word):
    if len(word) < 3:
        return word[::-1]
    else:
        start = random_chars()
        end = random_chars()
        return start + word[1:] + word[0] + end

# Decode function
def decode(word):
    if len(word) < 3:
        return word[::-1]
    else:
        word = word[3:-3]      # remove random characters
        return word[-1] + word[:-1]

# Main Program
choice = input("Enter 'c' for coding or 'd' for decoding: ").lower()

if choice == 'c':
    text = input("Enter a word: ")
    print("Encoded:", encode(text))

elif choice == 'd':
    text = input("Enter encoded word: ")
    print("Decoded:", decode(text))

else:
    print("Invalid choice!")