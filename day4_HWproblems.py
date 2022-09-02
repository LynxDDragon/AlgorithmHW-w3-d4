#EXERCISE 1

words = ['this' , 'is', 'a', 'sentence', '.']

def swap_words(sentence, word):
    for w in range(0, int(word / 2)):
        sentence[w], sentence[word - w -1 ] = sentence[word - w - 1], sentence[w]
        
print(words)
sentence = words        
word = len(words)
swap_words(sentence, word)

print(sentence)


#EXERCISE 2
a_text = 'In computing, a hash table hash map is a data structure which implements an associative array abstract data type, a structure that can map keys to values. A hash table uses a hash function to compute an index into an array of buckets or slots from which the desired value can be found'
a_text = a_text.split()

glos = {}
def wordcount(a_text):
    for word in a_text:
        glos[word] = glos.get(word,0)+ 1
    return glos

wordcount(a_text)


#Also, before getting to the actual thing, I made
#a program that counts the letters in the sentence

a_text = 'In computing, a hash table hash map is a data structure which implements an associative array abstract data type, a structure that can map keys to values. A hash table uses a hash function to compute an index into an array of buckets or slots from which the desired value can be found'
a_text = a_text.split()

glos = {}
def wordcount(a_text):
    for word in a_text:
        glos[word] = glos.get(word,0)+ 1
    return glos

wordcount(a_text)

#ExERSISE 3

list1 = [5,2,6,235,52,64,21,553]
target = 2

if target in list1:
    print('target here')
else:
    print('not here')
