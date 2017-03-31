clue = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

alphabet = "abcdefghijklmnopqrstuvwxyzab"
#ab을 추가한 이유 : yz+2를 했을 때 ab로 바꾸기 위해
#lphabet = "cdefghijklmnopqrstuvwxyzab"

def convert(s):
	result = []
	for letter in s:
		if letter in alphabet: # 공백 빼고 처리하기 위해
			_index = alphabet.index(letter)
			#result.append(alphabet[_index+2])
			result.append(alphabet[_index-24]) #배열[-1]해도 됨
		else: # 공백일 때
			result.append(letter)
	return "".join(result)

# main함수
if __name__ == '__main__':
	convert(clue)

# index함수 이용
a = "asd"
a.index("a") # 0 출력
a.index("s") # 1 출력
a.index("d") # 2 출력

# append함수 이용
a = [1, 2, 3, 4]
a.append(5) # a = [1, 2, 3, 4, 5]가 됨