# context
spam = 'Dear User,\n\nOur Administration Team needs to inform you that you are reaching the storage limit of your Mailbox account.\nYou have to verify your account within the next 24 hours.\nOtherwise, it will not be possible to use the service.\nPlease, click on the link below to verify your account and continue using our service.\n\nYour Administration Team.'


def create_word_list(spam):
    return spam.split()


# -----
# Convert the text to lower case and create a word list
words = create_word_list(spam.lower())

# Create a set storing only unique words
word_set = set(words)

# Create a dictionary that counts each word in the list
tuples = [(word, len([w for w in words if w == word])) for word in words]
# tuples = [(word, words.count(word)) for word in word_set]  # Vorschlag
word_counter = dict(tuples)
print(word_counter)

# Printing words that appear more than once
for (key, value) in word_counter.items():
    if value > 1:
        print("{}: {}".format(key, value))
