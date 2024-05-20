def word_frequency_counter(text):
    from collections import defaultdict
    import re

    text = text.lower()
    # Define a set of common prepositions and other words to exclude
    excluded_words = {'a', 'an', 'the', 'and', 'is', 'are', 'of', 'in', 'on', 'at', 'to', 'for', 'with', 'by',
                       'as', 'or', 'but', 'not', 'from', 'into', 'over', 'under', 'before', 'after', 'during', 
                       'through', 'above', 'below', 'between', 'among', 'out', 'off', 'about', 'against', 'along', 
                       'around', 'up', 'down', 'away', 'back', 'forward', 'it', 'its', 'has', 'been', 'still', 'have',
                         'does', 'that', 'many', 'was','use', 'some', 'all'}


    # Remove non-alphabetic characters and split into words
    word_list = re.findall(r'\b\w+\b', text)
    word_counts = defaultdict(int)
    for word in word_list:
        # Check if the word is not in the excluded words set
        if word not in excluded_words:
            word_counts[word] += 1

    # Sort by counts in descending order
    sorted_word_counts = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)
    return sorted_word_counts

with open('example.txt', 'r') as file:
    content = file.read()
word_freq = word_frequency_counter(content)
for word, freq in word_freq:
    if(freq>=4):
        print(f"{word}: {freq}")