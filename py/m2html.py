import sys
file1 = sys.argv[1]
f1 = open(file1,"r")
f1_lines = f1.readlines()
f1.close()

f1_diffs = {}
for line in f1_lines:
    if line[:2] == "S ":
        f1_line = line.rstrip()
        f1_diffs[f1_line[2:]] = []
    if line[:2] == "A ":
        f1_diffs[f1_line[2:]].append(line)

#A 37 38|||R:NOUN:NUM|||therapies|||REQUIRED|||-NONE-|||0

print("<html>\n<head><title>M2 diff file</title>\n<style>ins {background-color: lightyellow;} del {background-color: orange;} </style><body><p>")
for key in f1_diffs:
    print(key)
    ls_key = key.split()
    f1_diffs[key].reverse()
    for diff in f1_diffs[key]:
        ls = diff.rstrip().split("|||")
        ds = ls[0].split()
        dfirst = int(ds[1])
        dlast = int(ds[2])
        dlabel = ls[1]
        dtext = ls[2]
        dauthor = ls[len(ls)-1]
        if dlabel == 'noop':
            pass
        elif dfirst < dlast:
            if not(dtext == ""):
                ls_key.insert(dlast,"<ins>"+dtext+"</ins>")
            ls_key.insert(dfirst,"<del>")
            ls_key.insert(dlast+1,"</del>")
        else:
            if not(dtext == ""):
                ls_key.insert(dfirst,"<ins>"+dtext+"</ins>")
    phtml = " ".join(ls_key)
    phtml = phtml.replace("<del> ","<del>")
    phtml = phtml.replace(" </del>","</del>")
    phtml = phtml.replace("</del>","</del>&square;")
    phtml = phtml.replace("</ins>","</ins>&square;")
    print("<p>" + phtml + "</p>")

print("</body>\n</html>")

