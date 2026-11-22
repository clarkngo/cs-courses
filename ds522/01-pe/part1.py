# 1. Create a variable name text with the given value
text = """Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated."""

# 2. Loop through the text and remove 'is', 'better', and 'than'
words_to_remove = ['is', 'better', 'than']
for word in words_to_remove:
    # Replacing the word with an empty string removes it
    text = text.replace(word, "")

# 3. Make sure all words are in lowercase
text = text.lower()

# 4. Print the final text
print(text)