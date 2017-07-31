def next_haplo_name(hh):
    if hh < 10:
        name = 'J0' + str(hh)
    else: name = 'J' + str(hh)
    return name

fname = 'jassa_cropped.fas'
handle = open(fname)
haplos = {} #haplos have names A, B, C etc. as keys and sequence as value
h = 1
out1 = open('jassa_haplos.fas','w')
out2 = open('jassa_ind_haplos.csv','w')
while True:
    line1 = handle.readline() #the name, e.g. Jassa_L10A_F_18
    if not line1: break
    line2 = handle.readline() #the DNA sequence
    if line2 not in haplos.values(): #fill the haplos dictionary
        haplo_name = next_haplo_name(h)
        h += 1
        haplos[haplo_name] = line2
        line_h = '>' + haplo_name +'\n' + line2
        out1.write(line_h)
handle.close()
handle = open(fname)
while True:
    line1 = handle.readline() #the name, e.g. Jassa_L10A_F_18
    if not line1: break
    line1 = line1.strip('\n')
    line2 = handle.readline() #the DNA sequence
    for k,v in haplos.items(): #look for the haplotype code
        if v == line2:
            print(k,v)
            line1 = line1.strip('>').split('_')
            line1 = ','.join(line1)
            line_i = line1 +','+ k + '\n'
            out2.write(line_i)
out1.close()
out2.close()