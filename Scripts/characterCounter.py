

def characterCounter(s):
    counter = {}

    for c in s:
        if c in counter:
            counter[c] = counter[c] + 1
        else:
            counter[c] = 1

    for c in counter:
        if counter[c] > 2:
            print(c,": ",counter[c])
    return

def moveChars(s, offset, polarity):
    retString = ""
    for c in s:
        retString += chr(ord(c)+offset*polarity)

    return retString

if __name__ == "__main__":
    ciphertext = "c3ludCB2ZiA6IGEwX29icWxfczBldHJnX2RlX3BicXI="
    characterCounter(ciphertext)
    print(moveChars(ciphertext, ord('')-ord('a'), -1))
