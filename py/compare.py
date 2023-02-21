import sys
file1 = sys.argv[1]
file2 = sys.argv[2]
f1 = open(file1,"r")
f1_lines = f1.readlines()
f1.close()
f2 = open(file2,"r")
f2_lines = f2.readlines()
f2.close()

f1_diffs = {}
for line in f1_lines:
    if line[:2] == "S ":
        f1_line = line.rstrip()
        f1_diffs[f1_line] = []
    if line[:2] == "A ":
        ls = line.rstrip().split("|||")
        #print(ls[:len(ls)-1])
        line = "|||".join(ls[:len(ls)-1]) + "|||0"
        f1_diffs[f1_line].append(line)

f2_diffs = {}
for line in f2_lines:
    if line[:2] == "S ":
        f2_line = line.rstrip()
        f2_diffs[f2_line] = []
    if line[:2] == "A ":
        ls = line.rstrip().split("|||")
        #print(ls[:len(ls)-1])
        line = "|||".join(ls[:len(ls)-1]) + "|||0"
        f2_diffs[f2_line].append(line)

for key in f1_diffs:
    print(key)
    for diff in f1_diffs[key]:
        if not(diff in f2_diffs[key]):
            print(diff)
