from curses import pair_content
eng_freq = {
	'A':(8.2, 7.8),
	'B':(1.5, 2),
	'C':(2.8, 4),
	'D':(4.3, 3.8),
	'E':(13.0, 11),
	'F':(2.2, 1.4),
	'G':(2.0, 3),
	'H':(6.1, 2.3),
	'I':(7.0, 8.6),
	'J':(0.15, 0.21),
	'K':(0.77, 0.97),
	'L':(4.0, 5.3),
	'M':(2.4, 2.7),
	'N':(6.7, 7.2),
	'O':(7.5, 6.1),
	'P':(1.9, 2.8),
	'Q':(0.095, 0.19),
	'R':(6.0, 7.3),
	'S':(6.3, 8.7),
	'T':(9.1, 6.7),
	'U':(2.8, 3.3),
	'V':(0.98, 1),
	'W':(2.4, 0.91),
	'X':(0.15, 0.27),
	'Y':(2.0, 1.6),
	'Z':(0.074, 0.44)
}
cypher = "$%!2-20/44%27%!2%0,%!3%$4/).&/2-9/54(!49/5(!6%\"%%.!##%04%$!4(/'7!2433#(//,/&7)4#(#2!&4!.$7):!2$290,%!3%&).$%.#,/3%$!,)34/&!,,.%#%33!29\"//+3!.$%15)0-%.44%2-\"%').3/.3%04%-\"%2&)2347%!7!)49/52/7,\"9./,!4%24(!.*5,94()249&)2349/5233).#%2%,9-).%26!-#'/.!'!,,"
ALPHABET_LEN = 26

printlen = 200
eng_dict_idx = 0
K = 2
guesses = {
	'$':'D',
	'!':'A',
	'2':'R'
}

def printlim(s):
	print(s[:printlen])

def main():
	printlim(cypher)

	cypher_freq = makeSortedFreqList(cypher)
	
	ref_freq = [(eng_freq[k][eng_dict_idx]/100,k) for k in eng_freq]
	ref_freq.sort(key=lambda t: t[0])

	printFreqComparison(cypher_freq, ref_freq)
	basic_freq_mapping = makeFrequencyMapping(cypher_freq, ref_freq)
	text = decipherWithMapping(cypher, basic_freq_mapping)
	printlim(text)

	topk = [ref_freq[-i][1] for i in range(K)]+[' ']
	partial_text = ""
	for c in text:
		if c not in topk:
			partial_text += "*"
		else:
			partial_text += c
	printlim(partial_text)

	guess_text = ""
	for idx, c in enumerate(cypher):
		if c in guesses:
			guess_text += guesses[c]
		else:
			guess_text += partial_text[idx]
	printlim(guess_text)	

def decipherWithMapping(cypher: str, mapping: dict)->str:
	text = ""
	for c in cypher:
		text += mapping[c]
	return text

def makeFrequencyMapping(source_freq: list, dest_freq: list)->dict:
	return {source_freq[i][1]:dest_freq[i][1] for i in range(ALPHABET_LEN)}

def printFreqComparison(freq1: list, freq2: list):
	diffs = [abs(freq1[i][0]-freq2[i][0]) for i in range(ALPHABET_LEN)]
	for i in range(ALPHABET_LEN):
		print(f"{diffs[i]}, {freq1[i]}, {freq2[i]}")
	print()

def makeSortedFreqList(text: str)->list:
	m = {c:0 for c in text}
	for c in text:
		m[c] += 1
	char_counts = [(m[c], c) for c in m.keys()]
	char_counts.append((0, '^')) #this is because there are only 25 different chars in cypher and we want 26.
	#cypher_tot = sum([t[0] for t in char_counts])
	text_len = len(text)
	freq = [(count/text_len, char) for count, char in char_counts]
	freq.sort(key=lambda t: t[0])
	return freq

def removeChar(s: str, char_to_remove: str)->str:
	res = ""
	for c in s:
		if c != char_to_remove:
			res += c
	return res

if __name__ == "__main__":
	main()
