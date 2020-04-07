path = "./frankenstein.txt"
shifter = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?."
key = 10

def fopen_caesar():
    global path
    global key
    global shifter
    x = open(path).readlines()
    y = open("frankenstein.encrypted.txt").readlines()
    z = open("./encrypted_result.txt","w")
    idx = 0
    result = ""
    for i in x:
        for j in i:
            try:
                index = int(shifter.index(j))
                index += 10
                index %= len(shifter)
                result += shifter[index]
            except ValueError:
                result += j
                continue
        if result != y[idx]:
            print("error in encrypting")
        else:
            z.write("%s\n"%result.strip())
        idx += 1
        result = ""
    

def main():
    fopen_caesar()

main()