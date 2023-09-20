from collections import defaultdict

# Create a defaultdict with default value 0
word_count = defaultdict(int)

# Process a list of words and count their frequencies
words = ["apple", "banana", "apple", "cherry", "banana", "apple"]
for word in words:
    word_count[word] += 1

# Access the count for a word
count_banana = word_count["banana"]  # If 'banana' not present, returns 0

# normal_dict = {
#     "apple":2,
#     "banana":3
# }

x=1
