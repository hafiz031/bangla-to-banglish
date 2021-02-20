import re
from text_doc import text
from substitution import substitution_dict, unique_subs

bangla_text = text

banglish_text = bangla_text
# for char, sub in substitution_dict.items():
# 	banglish_text = re.sub(char, sub, banglish_text)

# following reverse order such that bigger match is taken in consideration first
for char in reversed(list(substitution_dict.keys())):
	banglish_text = re.sub(char, substitution_dict[char], banglish_text)	


'''
This code block is intended to append 'o' after each consonent sound if after that another consonent sound comes. 
In the default sound I omitted "o" after each consonent as "o" may be replaced if any vowel comes in place.
Instead I decided to append "o" later if there is no vowel after any consonent sound.
But this can create problem in some cases like "shth" and "sht" both of them are in "shashth" ("shashtho") 
and they will append "o" two times which is undesirable.
So I observed a pattern here: if current letter is a consonent and the next letter is also a consonent and if there
is unique_sub upto current letter but no unique_sub if we take the next consonent then append a 'o' after current 
consonent and start a new pattern from the next consonent.
'''
pattern_start = 0
consonent = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
for i in range(len(banglish_text) - 2):
	if banglish_text[i] in consonent and banglish_text[i + 1] == ' ' and banglish_text[i + 2] in consonent:
		banglish_text =  banglish_text[:i + 1] + 'o' + banglish_text[i + 1:]
		
banglish_text = re.sub('  ', '`', banglish_text)
banglish_text = re.sub(' ', '', banglish_text)
banglish_text = re.sub('`', ' ', banglish_text)

'''
appending "o" in the end of each word if there is a pattern in the end i[consonent]: like
'''

print(banglish_text)

# # for l in bangla_text:
# # 	print(l, end = '')

# import regex
# # print(regex.findall(r'\P{L}+', bangla_text))
# print(regex.findall(r'{L}+', bangla_text) )
# # r = re.compile(r'[^\W\d_]', re.U)
# # print(r.match(bangla_text)[0])
