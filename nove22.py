''' take the users input and replace all of the characters with the # except
for the last 4 characters


pseudo code:
use while loop:
replace word[0],[1],[3],[4] with #'''

word = (input("give me a word greater than four letters"))

wordlength = len(word)

if wordlength <=4:
            newword = "#" * wordlength

else:
            lastfour = word[wordlength -4:wordlength]
            hashtags = "#" * (wordlength -4)
            newword = hashtags + lastfour
print(newword)
# pdxclass
