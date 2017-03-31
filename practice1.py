clue = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
alphabet = "abcdefghijklmnopqrstuvwxyz"
transalphabet = "cdefghijklmnopqrstuvwxyzab"

def convert(clueString):
        import string
        converted = str.maketrans(alphabet, transalphabet)
        print (clueString.translate(converted))

#convert(clue)
convert("map")
