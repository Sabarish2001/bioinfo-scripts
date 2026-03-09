#Script to extract fastq headers from the fastq file and store it in the list

def extract_fastq_header(file_path,file_mode="r"):

    headers_list = []
    
    with open(file_path,file_mode) as fastq:
        count = 0                                              
        for every_line in fastq:
            if count % 4 == 0:
                headers_list.append(every_line)                # storing the header information of each and every read in list
            count += 1                
            
    return headers_list

headers = extract_fastq_headers(file_path,file_mode)
print(headers)
