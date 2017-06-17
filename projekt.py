
#Lazariev Mykyta
#s15928

import re 

print('->hallo')

def is_end(word):   
	skrot = ['prof', 'a', 'p', 'ul', 'np', 'al', 'pl', 'dyr', 'czyt', 'dep', 'inst', 'lek', 'pp']
	for k in skrot:
		if re.match(k, word)!=None:
			return False
	return True


name = input("->put the name of file with text\n")
if(name==""):
	name='text'
file = open(name+'.txt')
result = '<?xml version="1.0" author="Mykyta Lazariev" s="15928"?>\n<text>\n'
licznik_akapit = 0


for line in file:
	tmp = line.split('\n\n')
	#print(tmp)
	for text in tmp:
		if text == '':
			continue
		if text == '\n':
			continue

		licznik_zdanie = 1
		licznik_akapit = licznik_akapit + 1
		result += "\t<p xml:id=\""+str(licznik_akapit)+"\">\n"
		pice = re.split(r' *[\.\?!][\'"\)\]]*\s', text)

		tmp = ''
		tmp2 =''
		# for text in split:
		for i in range(0, len(pice)):
			text = pice[i]

			if text == '':
				continue
			if text == '\n':
				continue
			# print(text)
			# print('word: '+text.split(' ')[-1])
			word = text.split(' ')[-1]
			first = pice[0]

			if is_end(word):
				# print('is end: ',is_end(word))
				if len(tmp) > 0:
					text = tmp + text
					tmp = ''
				result += "\t\t<s xml:id=\"" + str(licznik_akapit) + "-" + str(licznik_zdanie) + "-s\">" + text + "</s>\n"
			else:
				# print('is end: ',is_end(word))
				tmp += text+' '
				print('tmp: '+tmp)
			
			licznik_zdanie = licznik_zdanie + 1
		result += "\t</p>\n"
result += "</text>\n"


# k1=1
# for text in f:
#     if text!='\n':
#         k2=1
#         line = ""
#         prev = -2 
#         p = etree.SubElement(page, 'p', xml_id=str(k1)+"-p")
#         for i in range(len(text)-1):
#             if text[i]=='.'or text[i]=='?'or text[i]=='!':
#                 if i!=(len(text)-1) and is_end(text, prev, i): 
#                     continue
                
#                 line = text[prev+2:i+1]+'\n'
#                 prev = i
                
#                 s = etree.SubElement(p, 's', xml_id=str(k1)+"-"+str(k2)+"-s")
#                 s.text = line
#                 k2=k2+1
                
#         line = text[prev+2:]  
#         s = etree.SubElement(p, 's', xml_id=str(k1)+"-"+str(k2)+"-s")
#         s.text = line
#         k1=k1+1

file.close();
file = open('result.xml', 'w+')
file.write(result)
file.close();

print('->done!')

# print('hallo')
# name = input("put the name ofile fileile with text\n")
# file = open(name);
# outfile = open('test.xml', 'w+')
# outfileile = open('homemade.xml', 'w+')
# doc.write(outfileile)
