import spacy
import string

nlp = spacy.load("en_core_web_sm")

total = 0

fileText = open('EmailLog.txt', mode='r', encoding='utf-8')
text = ""
for lineIn in fileText:
	text += lineIn
doc = nlp(text)

# save spaCy data to a text file
f = open("demo.txt", mode="wt", encoding="utf-8")

for token in doc:
	f.write('Token: ' + token.text + " => POS: " + token.pos_ + ", TAG: " + token.tag_ + ", DEP: " + token.dep_ + ", " + '\n')


f.close()

# read spaCy data from a text file
f = open("demo.txt", mode="r", encoding="utf-8")
for line in f:
	line = line.strip("\n")
	print(line)

f.close()

sentence = ''
email = ''
number = 0
amount = ''
org = ''
total = 0
num_int = 0
#sentence += email + ': ' + str(number) + ' to ' + org + '\n'

for word in doc:
	em = email
	num = number
	#amo = '$' + num
	#amo = amount
	o = org
	tot = total
	num_int = 0
	num_int += num

	if "@" in word.text:
		em = word.text
		sentence += em + ': '

	if "0" in word.text:
		num = word.text
		sentence += '$' + num
		tot += num_int

	if (((word.tag_ == 'NNP' and word.pos_ == "PROPN" and word.dep_ == "pobj" and word.text != "Hi" and word.text != "Hey" and word.text != "Hello" and word.text != "Inc.") and (word.text != "Hi " or "Inc ")) or ((word.tag_ == "NNP" and word.dep_ == "compound" and word.text != "Hi" and word.text != "Hey" and word.text != "Hello" and word.text != "Inc"))):
		o = word.text
		sentence += ' to ' + o + ' '



	if "End" in word.text:
		sentence += '\n\n'
print('\n\n' + sentence)
print('Total Requests: $' + str(tot))
		