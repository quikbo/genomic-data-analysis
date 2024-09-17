import fileinput
import sys


def N50_f():
    inputf = open(sys.argv[1], 'r')

    id = inputf.readline()
    contig_list = []
    
    while 1:
        if id == '':
            break
        
        contig_length = 0
        contig_line = inputf.readline()
        contig = ''
        
        while contig_line and contig_line[0] != '>': #first character of ID                                            
            contig += contig_line
            contig_length += len(contig_line)
            contig_line = inputf.readline()
            
        id = contig_line

        contig_list.append((contig, contig_length))
        #after while loop ends, we should have list full of tuples containing contig seq and its length
    contig_list.sort(reverse = True, key = lambda x : x[1])
    #now our list is sorted in descending order based on length, we can sum them up in order until we get 50% of total
    contig_lengths = [x[1] for x in contig_list]
    total_size = sum(contig_lengths)
    
    in_order_sum = 0
    for length in contig_lengths:
        in_order_sum += length
        if in_order_sum > total_size/2:
            print(str(length))
            outputf = open(sys.argv[2], 'w')
            outputf.write(str(length))
            outputf.close()
            return
            #print(str(length))
        
    inputf.close()

def N50():
    contig_list = []
    contig_length = 0
    contig = ''
    for line in fileinput.input():
      if line[0] == '>':
          contig_list.append((contig, contig_length))
          contig_length = 0
          contig = ''
      else:
          contig_length += len(line)
          contig += line
      counter += 1
    
    """
    while 1:
        if id == '':
            break

        contig_length = 0
        contig_line = input()
        contig = ''

        while contig_line and contig_line[0] != '>': #first character of ID                                            
            contig += contig_line
            contig_length += len(contig_line)
            contig_line = input()

        id = contig_line

        contig_list.append((contig, contig_length))
    #after while loop ends, we should have list full of tuples containing contig seq and its length                  
    """
    del contig_list[0] #removing first appending tuple which was blank
    
    contig_list.sort(reverse = True, key = lambda x : x[1])
    #now our list is sorted in descending order based on length, we can sum them up in order until we get 50% of total  
    contig_lengths = [x[1] for x in contig_list]
    total_size = sum(contig_lengths)

    in_order_sum = 0
    for length in contig_lengths:
        in_order_sum += length
        if in_order_sum >= total_size/2:
            print(str(length),end='')
            return

            
if __name__ == "__main__":
    N50()
