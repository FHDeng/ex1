hw =  'Hello World'
f = open('helloworld.txt','w')
for letter in hw:
	f.write(letter.capitalize()+ '\n'+'\t')
f.close()
#test
