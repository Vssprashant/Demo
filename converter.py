inFile = input("Enter the input file path+name: ")
outFile = inFile + '.csv'
scoap = []


def subString(string, startChar, endChar):
    return string[string.find(startChar)+1:string.find(endChar)]


with open(inFile, 'r') as f:
    scoap = f.readlines()

i = 0
while i < len(scoap):
    scoap[i] = scoap[i].replace(' ', '')
    if '∞' in scoap[i]:
        scoap[i] = scoap[i].replace('∞', '10000')
    i = i + 1

with open(outFile, 'w') as f:
    i = 0
    f.write('Net_Name\tCC0\tCC1\tCO\tSC0\tSC1\tSO\tis_trojan\n')
    while i < len(scoap):
        if ':' in scoap[i]:
            f.write(scoap[i][:-2] + '\t')
            i = i + 1
            for item in subString(scoap[i], '(', ')').split(','):   # cc0, cc1
                f.write(item + '\t')
            f.write(scoap[i][scoap[i].find(')')+1:-1] + '\t')   # co
            i = i + 1
            for item in subString(scoap[i], '[', ']').split(','):   # sc0, sc1
                f.write(item + '\t')
            f.write(scoap[i][scoap[i].find(']') + 1:-1])
            f.write('\t0\n')
            i = i + 1
#            pass
#        i = i + 1
