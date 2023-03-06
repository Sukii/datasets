import sys
import collections

file1 = sys.argv[1]
f1 = open(file1,"r")
f1_lines = f1.readlines()
f1.close()

diff = {}
key = "start"
for f1_line in f1_lines:
    line = f1_line.rstrip()
    if line[:2] == "S ":
        key = line
        diff[key] = []
    if line[:2] == "A ":
        ls = line.split("|||")
        df = "|||".join(ls[:len(ls)-1])
        diff[key].append(df)

for key in diff:
    print(key)
    first_diff = diff[key][0]
    diff_counter = collections.Counter(diff[key])
    if first_diff.split("|||")[1] == 'noop' and diff[key][:1].count(first_diff) > 0:
           print(diff[key][0] + "|||0")
    else:
        range_ls = []
        for df in diff_counter.keys():
            count = diff_counter[df]
            dfls = df.split("|||")
            diff_range = dfls[0].split(" ")
            start = int(diff_range[1])
            end = int(diff_range[2])
            range = [start,end]
            foo = True
            if count < 5:
                foo = False
            for range_item in range_ls:
                start_item = range_item[0]
                end_item = range_item[1]
                if start >= start_item  and start <= end_item:
                    foo = False
            if start < 0:
                foo = False
            if foo:
                print(df + "|||0")
            range_ls.append(range)
    print("")
