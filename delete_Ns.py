fname = 'filled_in_haplo.fas'
handle = open(fname)
out = open('jassa_cropped.fas','w')
while True:
    line1 = handle.readline()
    if not line1: break
    line2 = handle.readline()
    if 'N' not in line2:
        out.write(line1)
        out.write(line2)
out.close()