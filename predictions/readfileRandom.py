'''
Created on 2015年12月6日

@author: leo
'''
filename = 'nonlinks'

def countfilelines(filename, eof='\n', buffsize=4096):
    with open(filename, 'rt') as handle:
        linenum = 0
        buffer = handle.read(buffsize)
        while buffer:
            linenum += buffer.count(eof)
            buffer = handle.read(buffsize)
        return linenum

def readline(filename, lineIndex, eof='\n', buffsize=4096):
    readlines = 0
    #print('the read line is: ', lineIndex)
    with open(filename, 'rt', encoding='utf-8') as handle:
        buffer = handle.read(buffsize)
        while buffer:
            #print('buffer:\n', buffer)
            #print('read lines: ', buffer.count(eof))
            thisblock = buffer.count(eof)
            if readlines < lineIndex < readlines + thisblock:
                #print(lineIndex - readlines - 1)
                return buffer.split(eof)[lineIndex - readlines - 1]
            elif lineIndex == readlines + thisblock:
                part0 = buffer.split(eof)[-1]
                buffer = handle.read(buffsize)
                part1 = buffer.split(eof)[0]
                return part0 + part1
            readlines += thisblock
            buffer = handle.read(buffsize)
        else:
            raise IndexError   
            
            
if __name__ == '__main__':
#     line = readline(filename, 1000)
#     print('the line is:\n', line)
    lines  = countfilelines(filename)
    print('file lines: ', lines)
