FILE_NAME_CODE = "code.py"
FILE_NAME_PSEUDO = "pseudo1.1.txt"
FILE_LINES = []
FILE_VARS = []
VAR = []
DEV = []
PE = []
P = []

FILE = open(FILE_NAME_CODE, "r+")
FILE_LINES = FILE.readlines()
FILE.close()

for i in range(len(FILE_LINES)):
    FILE_LINES[i] = FILE_LINES[i].strip("\n")

def get_all():
    global VAR, DEV, PE, P
    var_start = 0
    var_end = 0
    for i in range(len(FILE_LINES)):
        if FILE_LINES[i] == "#VAR" or FILE_LINES[i] == "#ENDVAR":
            VAR.append(i)
        elif FILE_LINES[i][:4] == "def ":
            DEV.append(i)
        elif "+=" in FILE_LINES[i]:
            PE.append(i)
        elif "print" in FILE_LINES[i]:
            P.append(i)

def var_getblock():
    var_start = 0
    var_end = 0
    for i in range(len(FILE_LINES)):
        if FILE_LINES[i] == "#VAR":
            var_start = i
        elif FILE_LINES[i] == "#ENDVAR":
            var_end = i
    return var_start, var_end

def var_convert():
    global VAR
    #VAR = var_getblock()
    #print("←")
    #print(var)
    for j in range(VAR[0] + 1, VAR[1]):
        #print(FILE_LINES[j])
        if "=" in FILE_LINES[j]:
            FILE_VARS.append(FILE_LINES[j])

    #print(FILE_VARS)
    for k in range(len(FILE_VARS)):
        var = FILE_VARS.pop(k)
        var = var.split("=")
        new_var = var[0] + "<-" + var[1] + "\n"
        FILE_VARS.insert(k, new_var)

def plus_equals():
    global PE

    for j in range(len(PE)):
        line = FILE_LINES[PE[j]]
        line = line.split("+=")
        new_line = line[0] + " = " + line[0].strip() + " + " + line[1].strip()
        FILE_LINES.pop(PE[j])
        FILE_LINES.insert(PE[j], new_line)

def procedure():
    global DEV
    
    for j in range(len(DEV)):
        line = FILE_LINES[DEV[j]]
        line = line.replace("def ", "PROCEDURE ")
        FILE_LINES.pop(DEV[j])
        FILE_LINES.insert(DEV[j], line)

def prnt():
    for i in range(len(P)):
        line = FILE_LINES[P[i]]
        line = line.split('print(')
        line[1] = line[1].split(')')
        c = line[1][0]
        FILE_LINES.pop(P[i])
        new_line = line[0] + "PRINT " + c
        FILE_LINES.insert(P[i], new_line)

get_all()
var_convert()
plus_equals()
procedure()
prnt()
#print(FILE_VARS)

PSEUDO = open(FILE_NAME_PSEUDO, "w+")
for s in range(VAR[0] + 1):
    PSEUDO.writelines(FILE_LINES[s] + "\n")
PSEUDO.writelines(FILE_VARS)
for d in range(VAR[1], len(FILE_LINES)):
    PSEUDO.writelines(FILE_LINES[d] + "\n")
PSEUDO.close()

print("Succsefully converted file to pseudo code")