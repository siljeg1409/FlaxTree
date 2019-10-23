import os

def PrintTree(p, l):
    if(not os.path.exists(p)): return
    s = "|"
    k = l
    while(k > 0):
        s += " " * 4 + ("|" if k > 0 else "")
        k -= 1
    for t in os.listdir(p):
        pth = p + "\\" + t
        if(os.path.isdir(pth)):
            print( s[:-1] + "[" + t + "]" )
        else:
            print(s + ">" +  t)

        if(os.path.isdir(pth) and not os.path.isfile(pth)):
            PrintTree(pth, l + 1)

if __name__ == "__main__":
    
    path = ""
    while(os.path.exists(path) == False):
        path = input("Please enter folder path: ")

    PrintTree(path, 0)



