def find_anagrams(word, candidates):
    expected = []
    
    for b in candidates:
        ##Checks for length, anagram and not being same word:
        if len(word) == len(b) and sorted(word.lower()) == sorted(b.lower()) and word.lower() != b.lower():
            expected.append(b)
            
   
    return expected


