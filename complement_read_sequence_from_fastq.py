def complement_seq_reads(fastq,mode):

    complement_dict = {"A":"T","T":"A","G":"C","C":"G","N":"N"}

    line_number = 0
    with open(fastq,mode) as fastq:
        for every_line in fastq:
            complement_seq = ""
            if line_number % 4 == 1:

                for every_char in every_line.rstrip():
                    complement_seq += complement_dict[every_char]

                print(f"Original_sequence is:",every_line)
                print(f"Complement_sequence is:",complement_seq)

            line_number += 1

complement_seq_reads("C:/Users/sabar/Downloads/sample.fastq","r")
