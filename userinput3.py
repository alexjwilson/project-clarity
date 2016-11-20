import re
import string
import sys

exclude = list(string.punctuation)

f = open('message.txt')
file = f.read()

print(file)
# print(len(file))

sentences = re.split(r' *[\.\?!][\'"\)\]]* *', file)
# sentences = file.split('\n')

# print(sentences)

newList = []

for i in sentences:
    newList.append(i.split(" "))

longest_sen = max(newList, key = len)

longest_sen_len = len(longest_sen)

# print(longest_sen)
# print(longest_sen_len)

text = re.sub('[^A-Z,a-z\ \']+'," ", file)
words = list(text.split())
# print(words)

sortedwords = sorted(words, key=len)

sortedsentences = sorted(sentences, key= len)

def __init__(self):
    return None

def syllable_count(text):
        """
        Function to calculate syllable words in a text.
        I/P - a text
        O/P - number of syllable words
        """
        count = 0
        vowels = 'aeiouy'
        text = text.lower()
        text = "".join(x for x in text if x not in exclude)

        if text is None:
            return 0
        elif len(text) == 0:
            return 0
        else:
            if text[0] in vowels:
                count += 1
            for index in range(1, len(text)):
                if text[index] in vowels and text[index-1] not in vowels:
                    count += 1
            if text.endswith('e'):
                count -= 1
            if text.endswith('le'):
                count += 1
            if count == 0:
                count += 1
            count = count - (0.1*count)
            return count

def flesh(file):
    float(len(words)/(file.count('.') + file.count('?') + file.count('!')))

const = r"bcdfghjklmnpqrstvwxyz"
vow = r'aeiou'
def syl_count(s):
	syl_count = 0
	qu = re.compile(r'qu')
	s = qu.sub('qw',s)



	ends = re.compile(r'(es$)|(que$)|(gue$)')
	s = ends.sub('',s)

	s = re.sub(r'^re',r'ren',s)
	s = re.sub(r'^gua',r'ga',s)
	s = re.sub(r'([aeiou])(l+e$)',r'\g<1>',s)
	(s,nsyl_count) = re.subn(r'([bcdfghjklmnpqrstvwxyz])(l+e$)',r'\g<1>',s)
	syl_count += nsyl_count


	s = re.sub(r'([aeiou])(ed$)',r'\g<1>',s)
	(s,nsyl_count) = re.subn(r'([bcdfghjklmnpqrstvwxyz])(ed$)',r'\g<1>',s)
	syl_count += nsyl_count

	endsp = re.compile(r'(ly$)|(ful$)|(ness$)|(ing$)|(est$)|(er$)|(ent$)|(ence$)')
	(s,nsyl_count) = endsp.subn(r'',s)
	syl_count += nsyl_count
	(s,nsyl_count) = endsp.subn(r'',s)
	syl_count += nsyl_count

	s = re.sub(r'(^y)([aeiou][aeiou]*)',r'\g<2>',s)
	s = re.sub(r'([aeiou])(y)',r'\g<1>t',s)
	(s,nsyl_count) = re.subn(r'(^y)([bcdfghjklmnpqrstvwxyz])',r'\g<2>',s)
	syl_count += nsyl_count
	syl_count += nsyl_count


	s = re.sub(r'aa+',r'a',s)
	s = re.sub(r'ee+',r'e',s)
	s = re.sub(r'ii+',r'i',s)
	s = re.sub(r'oo+',r'o',s)
	s = re.sub(r'uu+',r'u',s)

	dipthongs = re.compile(r'(ai)|(au)|(ea)|(ei)|(eu)|(ie)|(io)|(oa)|(oe)|(oi)|(ou)|(ue)|(ui)')
	s,nsyl_count = dipthongs.subn('',s)
	syl_count += nsyl_count

	if(len(s)>3):
			s = re.sub(r'([bcdfghjklmnpqrstvwxyz])(e$)',r'\g<1>',s)

	s,nsyl_count = re.subn(r'[aeiouy]','',s)
	syl_count += nsyl_count
	return syl_count

syllableCount = 0

for word in sortedwords:
    #print(syl_count(word))
    syllableCount += syl_count(word)

# print(syllableCount)

print("The number of sentences is: %s." % (file.count('.') + file.count('?') + file.count('!')))

print("The number of words is: %s." % len(words))

print("The number of words in the longest sentence is: %s." % longest_sen_len)

print("The longest word is: %s." % sortedwords[-1])

print("The count of syllables is: %s." % syllableCount)

print("The Flesh reading ease of your message is: %s." % (206.835 - 1.015*(len(words)/(file.count('.') + file.count('?') + file.count('!'))) - 84.6*(syllableCount/len(words))))
