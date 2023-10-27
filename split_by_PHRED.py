import numpy as np
import linecache

fastq = "C:\d_fragilis_transcriptome_proj\dfrag_combined_samp.fastq"
# Create two new fastq files, one for each PHRED encoding
phred_33 = open("phred_33.fastq", "w")
phred_64 = open("phred_64.fastq", "w")

phred_33_symbols = [chr(i) for i in range(33, 75)]
phred_64_symbols = [chr(i) for i in range(64, 106)]

with open(fastq, "r") as f:
    num_lines = sum(1 for line in f) 
    # Assuming num_lines is already defined
    arr = np.arange(1, num_lines+1, 4)
    # Loop through each number in arr
    for i in arr:
        # Fetch everything on line i+3
        q_scores = linecache.getline(fastq, i+3)
        q_scores = q_scores.split("\n")[0]
        print(q_scores)
        # If all of the characters in q_scores are in phred_33_symbols, then
        # the file is encoded with PHRED+33
        if all(char in phred_33_symbols for char in q_scores):
            # The file is encoded with PHRED+33
            for j in range(0, 4):
                phred_33.write(linecache.getline(fastq, i+j))
            print("PHRED+33")
        # If any of the characters in q_scores are in phred_64_symbols, then
        # the file is encoded with PHRED+64
        elif all(char in phred_64_symbols for char in q_scores):
            # Add the four lines to the PHRED+64 file
            for j in range(0, 4):
                phred_64.write(linecache.getline(fastq, i+j))
            print("PHRED+64")
        else:
            print("Unknown encoding")

phred_33.close()
phred_64.close()


