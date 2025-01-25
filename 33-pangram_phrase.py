pangram = "the quick brown fox jumps over the lazy dog"

def program(phrase):
    letter = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'}
    phrase = set(phrase)

    if len(phrase) - 1 == len(letter):
        return True
    else:
        return False
    
print(program(pangram))