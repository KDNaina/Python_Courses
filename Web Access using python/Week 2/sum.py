import re

if __name__ == '__main__':
    file = open('regex_sum_694308.txt') #replace file name with your filename
    sm = 0
    wd = 0
    for line in file:
        temp = line.rstrip()
        temp = re.findall('[0-9]+', temp)
        #print(temp)
        #print('\n')
        if len(temp) > 0:
            for w in temp:
                wd += 1
                sm += int(w)

    print('The sum for the sample text above is %d\n' % sm)
