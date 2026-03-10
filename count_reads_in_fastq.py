def count_reads_in_fastq(file,mode="r"):

    with open(file,mode) as fastq:

        line_number = 0                                   
        count_read = 0                                    #keeps track of the number of headers

        for every_line in fastq:                          #Iterate each line in fastq
            if line_number % 4 == 0:                      #0,4,8,12 .....n matches this condition which points to the headers of the fastq
                print(every_line)            
                count_read += 1                           #increment count_read -> 1 everytime you match a header
            line_number += 1                              #increment the line_number -> 1 to move to the next line in fastq
    return count_read                                     # return the count_read which has the total read count in a given fastq file

read_count = count_reads_in_fastq(file_name,mode)
print(read_count)
