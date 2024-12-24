meme_dict = {
            'CRINGE': 'Garip ya da utandırıcı bir şey',
            'LOL': 'Response to something funny',
            'ROFL':  'response to a joke',
            'SHEESH': 'disapprove'
            }

word = input("Write down a word you don't understand (in all capital letters!): ")

if word in meme_dict.keys():
    print(meme_dict[word])
else:
    print('The word you entered is not found yet. Please try later.')
