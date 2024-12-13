def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")
def is_valid(s):
    if (s[0].isalpha() and s[1].isalpha()):
        if (len(s)>1 and len(s)<7):
            flag=0
            for i in range(len(s)-1):
                if s[i].isnumeric():
                    if(flag==0):
                        if(s[i]=="0"):
                            return False
                        flag=1
                    if not(s[i+1].isnumeric()):
                        return False
                if not(s[i].isalpha() or s[i].isnumeric()):
                    return False
            if not(s[len(s)-1].isalpha() or s[len(s)-1].isnumeric()):
                return False
            return True

        else:
            return False
    else:
        return False
main()
