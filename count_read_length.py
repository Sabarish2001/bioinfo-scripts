def count_length_of_reads(file,mode):

    seq_len = {}
    with open(file,mode) as fastq:
        line_number = 0
        for every_line in fastq:                                                                                           
            if line_number % 4 == 1:                                                 
                seq_len[every_line.rstrip()] = 0                                            
            line_number += 1                                     
        for every_keys in seq_len.keys():                                            
            seq_len[every_keys] += len(every_keys)              

    return seq_len
