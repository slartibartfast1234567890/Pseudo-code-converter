FILE_NAME_CODE = "code.txt"
FILE_NAME_PSEUDO = "pseudo.txt"
FILE_LINES = []
FILE_VARS = []

FILE = open(FILE_NAME_CODE, "r+")
FILE_LINES = FILE.readlines()
FILE.close()

for i in range(len(FILE_LINES)):
    FILE_LINES[i] = FILE_LINES[i].strip()
    FILE_LINES[i] = FILE_LINES[i].strip("\n")

def var_getblock():
    var_start = 0
    var_end = 0
    for i in range(len(FILE_LINES)):
        if FILE_LINES[i] == "#VAR":
            var_start = i
        elif FILE_LINES[i] == "#ENDVAR":
            var_end = i
    return var_start, var_end

VAR = var_getblock()
#print("←")
#print(var)
for j in range(VAR[0] + 1, VAR[1]):
    #print(FILE_LINES[j])
    if FILE_LINES[j][:4] == "var ":
        FILE_LINES[j] = FILE_LINES[j][4:len(FILE_LINES[j])]
        FILE_VARS.append(FILE_LINES[j])

#print(FILE_VARS)
for k in range(len(FILE_VARS)):
    var = FILE_VARS.pop(k)
    var = var.split("=")
    new_var = var[0] + "<-" + var[1] + "\n"
    FILE_VARS.insert(k, new_var)

print(FILE_VARS)

PSEUDO = open(FILE_NAME_PSEUDO, "w+")
for s in range(0, VAR[0]):
    PSEUDO.writelines(FILE_LINES[s])
PSEUDO.writelines(FILE_VARS)
for d in range(VAR[1], len(FILE_LINES)):
    PSEUDO.writelines(FILE_LINES[d] + "\n")
PSEUDO.close()