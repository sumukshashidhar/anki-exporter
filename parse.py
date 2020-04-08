## we have to first read the data properly
## we can make it efficient later

def parsestring(S):
	catch = '{{c'
	retstr = ''
	for i in range(len(S)):
		if S[i:i+3] == catch and S[i+4:i+6] == '::':
			for j in range(i+6, len(S)):
				if S[j:j+2] == '}}':
					retstr = retstr + " "
					break
				else:
					retstr = retstr + (S[j])
			else:
				print("Invalid Syntax")
	return retstr



def clozenormalizer(S):
	catch = '{{c'
	retstr = ''
	for i in range(len(S)):
		if S[i:i+3] == catch and S[i+4:i+6] == '::':
			for j in range(i+6, len(S)):
				if S[j:j+2] == '}}':
					retstr = retstr + " "
					break
				else:
					retstr = retstr + (S[j])
			else:
				print("Invalid Syntax")
		else:
			retstr = retstr + S[i]
	return retstr

S = input()
print(parsestring(S))
print(clozenormalizer(S))
