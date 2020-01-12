for i in range(1,12):
    with open ('C:\\temp\\dataset_3380_5 (2).txt') as f:
        cnt = 0
        h = float(0)
        for line in f:
             line = line.strip().split()
             if int(i) == int(line[0]):
                 cnt += 1
                 h += float(line[2])
                 #print(line[0],line[1],line[2])
            # print(line)
        if cnt ==0:
            print(i, '-')
        else:
            print(i, h/cnt)
    #break
#     print(i)