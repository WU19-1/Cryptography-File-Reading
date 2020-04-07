path = "./frankenstein.encrypted.txt"
shifter = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?."
key = 10

def fopen_decrypt_caesar():
    global path
    global shifter
    global key
    x = open("./decrypted_result.txt","w")
    y = open(path,'r').readlines()
    for i in y:
        result = ""
        for j in i:
            try:
                index = shifter.index(j)
                if (index - key < 0):
                    index += len(shifter)
                index -= 10
                result += shifter[index]
            except ValueError:
                result += j
                continue
        x.write("%s\n" % result.rstrip())
    x.close()

def main():
    fopen_decrypt_caesar()

main()