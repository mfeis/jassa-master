import re
KT209580 = 'AACCTTGTATTTTATACTTGGGCTATGATCAAGCCTAATCGGCACTTCTTTAAGAATAATTATCCGAACAGAACTTATAGCTCCTAGTAATATTATTGGGGACGACCAAATCTATAATGTTGTAGTCACAGCTCACGCCTTCATTATAATTTTCTTTATAGTTATACCCGTGATAATCGGTGGGTTTGGGAATTGACTTATCCCTTTAATACTCGGTAGCCCAGATATGGCGTTCCCCCGGATAAATAACATAAGATTTTGATTACTACCTCCCTCCTTAACTCTTCTTTTAGTAAGAGGTTTAGTAGAAAGAGGGGTCGGCACTGGTTGAACAGTTTACCCCCCTTTAAGAAGGAGGTTAGGCCACCCAGGCGGAGCCGTCGACCTAGCAATTTTTTCACTCCATTTAGCAGGTGCCTCTTCGATTTTAGGGGCCATTAATTTTATTTCTACTATTATTAATATACGCCCGGCAGGAATAACTTTAGACCGTATACCCTTATTTGTTTGATCCGTCTTTATTACGGCAGTTCTTCTTCTCCTCTCACTCCCGGTATTGGCCGGGGCAATCACTATATTATTAACAGACCGTAACCTAAACACTTCCTTCTTTGATCCATTAGGCGGGGGGGATCCTATTCTATACCAACATTTGTTC'
var_pos = [121,136,166,169,178,181,220,232,238,241,250,262,263,271,295,343,346,356,373,376,382,386,406,421,436,472,496]
length = 658
fname = 'fill_in_haplo.fas'
handle = open(fname)
out = open('filled_in_haplo.fas','w')
name = ''
seq = ''
while True:
    line1 = handle.readline()
    if not line1: break
    vp = 0 #for looping through var_pos
    seqL = ''
    line2 = handle.readline()
    name = re.findall('(^>\S*)\n',line1)[0]
    seq = re.findall('(\S*)\n',line2)[0]
    #fill out seq to full length seqL
    for l in range(length):
        if l+1 not in var_pos:
            seqL = seqL + KT209580[l]
        else:
            seqL = seqL + seq[vp]
            vp += 1
    #change Ns at start and end of seqL
    if seqL[var_pos[0]-1] == 'N':
        end_part = re.findall('N([ATGC]*$)',seqL[0:255])[0]
        begin_len = length - len(end_part) - (length - 255)
        seqL = 'N' * begin_len + end_part + seqL[255:]
    if seqL[var_pos[-1]-1] == 'N':
        start_part = re.findall('(^[ATGC]*)N',seqL[255:])[0]
        end_len = length - len(start_part) - 255
        seqL = seqL[0:255] + start_part + ('N' * end_len)
    #write to outfile
    out.write(line1)
    out.write(seqL+'\n')
out.close()
