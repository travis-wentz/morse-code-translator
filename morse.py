#imports

def getMorseMap():
	morseMap = {"a": ". -",
		"b": "- . . .",
		"c": "- . - .",
		"d": "- . .",
		"e": ".",
		"f": ". . - .",
		"g": "- - .",
		"h": ". . . .",
		"i": ". .",
		"j": ". - - -",
		"k": "- . -",
		"l": ". - . .",
		"m": "- -",
		"n": "- .",
		"o": "- - -",
		"p": ". - - .",
		"q": "- - . -",
		"r": ". - .",
		"s": ". . .",
		"t": "-",
		"u": ". . -",
		"v": ". . . -",
		"w": ". - -",
		"x": "- . . -",
		"y": "- . - -",
		"z": "- - . .",
		" ": " ",
		"0": "- - - - -",
		"1": ". - - - -",
		"2": ". . - - -",
		"3": ". . . - -",
		"4": ". . . . -",
		"5": ". . . . .",
		"6": "- . . . .",
		"7": "- - . . .",
		"8": "- - - . .",
		"9": "- - - - ."}
	return morseMap

def main():
	print("Enter your message > ")
	inStr = input().lower()
	morseStr = "- . - . -"
	morseMap = getMorseMap()

	for letter in inStr:
		if letter in morseMap:
			tempStr = "   " + morseMap[letter]
			morseStr += tempStr
	morseStr += "   . - . - ."
	print(morseStr)

if __name__ == "__main__":
	main()