def longest_word(input:str)->int:
    words = input.split()
    max_length = max(len(word)for word in words)
    return max_length
    
input = "the quick brown fox jumps over the lazy dogs"
print(longest_word(input))


