def parse_quality_values_to_scores(file,mode):
    quals_with_values = {}

    with open(file,mode) as fastq:
        line_number = 0
        for every_line in fastq:
            if line_number % 4 == 3:
                quals_with_values[every_line] = []

                for every_character in every_line:
                    quals_with_values[every_line].append(ord(every_character) - 33)
            line_number += 1

    return quals_with_values
