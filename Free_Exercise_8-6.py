#%%
def devowel(word):
    List = list(word)
    Vowels = ["a", "e", "i", "o", "u"]
    for letter in List:
        if letter.lower() in Vowels:
            List.remove(letter)
    word = ''.join(List)
    return word

#%%
