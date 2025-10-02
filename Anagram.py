# Anagram set: these words are all anagrams of each other 
anagrams = ['post', 'pots', 'spot', 'stop', 'tops', 'opts']

"""
signature: letters in a word sorted alphabetically
example: signature('python') = 'hnopty'
Two words can be anagrams if they share the same signature.
Example: 'python' and 'phyton' both become 'hnopty'.
"""

# Dictionary showing words grouped by their signature
# Here 'post' is the key, and the value is a set of all its anagrams
anagramsBySignature = {
	'post':{'post', 'pots', 'spot', 'stop', 'tops', 'opts'}
}
# -------------------------------
# Step 1: Read file and store words (with newline characters)
# -------------------------------
words = []
for line in open('words.txt'): # open file line by line
    words.append(line) # append raw lines (includes "\n")
print(len(words))  # prints total number of lines/words
print(words[:10])  # shows first 10 entries

# Example of strip(): removes whitespace/newlines
print('Aaron\n'.strip()) # returns "Aaron"

# -------------------------------
# Step 2: Clean words using strip() and lower()
# -------------------------------
words = []
for line in open('words.txt'):
    words.append(line.strip().lower())  # strip removes "\n", lower makes uniform
print(words[:10])   # shows cleaned words

# -------------------------------
# Step 3: Use a set to store unique words only (remove duplicates)
# -------------------------------
words = set()
for line in open('words.txt'):
    words.add(line.strip().lower())

# -------------------------------
# Step 4: Use set comprehension (shorter way of writing Step 3)
# -------------------------------
words = {line.strip().lower() for line in open('words.txt')}
print(words) # prints all unique words (unordered)

# -------------------------------
# Step 5: Convert the set into a sorted list
# -------------------------------
words = sorted({line.strip().lower() for line in open('words.txt')})
print(words)  # prints sorted words

# -------------------------------
# Step 6: Load and preprocess words 
# -------------------------------
# Create a sorted list of unique words from words.txt (converted to lowercase, stripped of spaces/newlines)
words = sorted({line.strip().lower() for line in open('words.txt', 'r')}) 
# Demo: how sorting letters in a word shows its "signature"
print("Brownie:",sorted("brownie"))
print("Is 'star' an anagram of 'arts'? ->",sorted("star") == sorted("arts"))
print("Is 'stars' an anagram of 'arts'? ->",sorted("stars") == sorted("arts"))
# Using join to show the sorted letters of 'football'
print("Football:","-".join(sorted("football")))
print("Football:",''.join(sorted("football")))

# -------------------------------
# Step 7: Build signature → word mapping
# -------------------------------
def signature(word): #A "signature" is simply the word’s letters sorted alphabetically.
    return ''.join(sorted(word))
words_by_signature = {} # Dictionary where key = signature, value = set of words with that signature

for word in words:
    if signature(word) not in words_by_signature: # If signature not yet in dictionary, add a new set with the current word
        words_by_signature[signature(word)] = {word} 
    else: # If signature already exists, add the word to the set
        words_by_signature[signature(word)].add(word)

print("Words grouped by signature (dict):", words_by_signature)

# Alternative: Using defaultdict for cleaner code
import collections
words_by_signature = collections.defaultdict(set)

for word in words:
    words_by_signature[signature(word)].add(word)
print("Words grouped by signature (defaultdict):",words_by_signature)

# -------------------------------
# Step 8: Filter only *true anagram groups* (sets with >1 word)
# -------------------------------
anagrams_by_signature = {
    sig: wordset for sig, wordset in words_by_signature.items() if len(wordset) > 1
}
# Test signature
print("Signature of 'python':",signature('python'))
print("Anagrams of 'python':",anagrams_by_signature[signature('python')])

# -------------------------------
# Step 9: Define function to find anagrams safely
# -------------------------------
def find_anagram(word):    
    return anagrams_by_signature.get(signature(word.lower()), set()) #Return all anagrams of 'word' from the dictionary, or an empty set if none found
print("Anagrams of 'tops':",find_anagram('tops'))
print("Anagrams of 'michele':",find_anagram('michele'))

# -------------------------------
# Step 10: Explore the anagram groups
# -------------------------------
def find_anagram(myword):
    try:
        return anagrams_by_signature[signature(word)]
    except KeyError:
        return set()
print("Signatures sorted by length:", sorted(anagrams_by_signature.keys(), key=len, reverse=True)) # Sort signatures by length (longest first)
print("Anagram groups sorted by size:", sorted(anagrams_by_signature.values(), key=len, reverse=True)) # Sort anagram groups by group size (largest first)

# -------------------------------
# Step 11: Palindromes
# -------------------------------
""" Find all palindrome pairs (words that are reverses of each other) with length >= 7 from the anagram dictionary.
    Parameters: anagrams_by_signature (dict): dictionary mapping word signatures to sets of anagrams.
    Returns: list[set]: list of sets, where each set contains a palindrome pair.
"""
def palindromes(anagrams_by_signature):
    palindrome_pairs = []
    for wordset in anagrams_by_signature.values(): # Loop through each anagram set in the dictionary
        for word in wordset:
            if len(word) >= 7:  # Only check words of length >= 7
                reversed_word = word[::-1]  # reverse the word
                if reversed_word in wordset and word != reversed_word:
                    pair = {word, reversed_word} # Create a set (ensures uniqueness of order)                
                    if pair not in palindrome_pairs: # Avoid adding duplicates
                        palindrome_pairs.append(pair)

    return palindrome_pairs
result = palindromes(anagrams_by_signature)
print(result)