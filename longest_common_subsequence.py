# -*- coding: utf-8 -*-
"""
Created on Mon Feb 12 19:50:44 2024

@author: Arjunsinh Harer
"""

import random
import numpy as np

def generate_dna_fragment():
  
    
    dna_bases = ['A', 'T', 'C', 'G']

    # Generate the sequence without start and stop codons first
    fragment_length = random.randint(1000,4000)  # 200 base pairs without start and stop codons
    dna_fragment = ''.join(random.choice(dna_bases) for _ in range(fragment_length))  
  

    return dna_fragment


def longest_sub_seq(seq_1, seq_2, read_len_1, read_len_2):
    # Initialize a 2D numpy array with zeros, with dimensions based on the lengths of the two input sequences.
    # The matrix will store the length of the longest common suffix for substrings ending at positions [i][j].
    tabulation = np.zeros((read_len_1 + 1, read_len_2 + 1), dtype=int)
    
    # Variable to keep track of the length of the longest common substring found so far.
    length = 0
    
    # Variable to store the ending position of the longest common substring in seq_1.
    end_pos = 0
    
    # Loop over each character position in seq_1.
    for i in range(1, read_len_1 + 1):  # Starting from 1 since numpy arrays are directly accessible
        
        # Nested loop over each character position in seq_2.
        for j in range(1, read_len_2 + 1):  # Starting from 1 as well
            
            # If the current characters in seq_1 and seq_2 match,
            # update the current cell based on the value from the diagonally previous cell + 1.
            if seq_1[i-1] == seq_2[j-1]:
                tabulation[i, j] = tabulation[i-1, j-1] + 1
                
                # If this gives us a new maximum length, update the length and record the current position.
                if length < tabulation[i, j]:
                    length = tabulation[i, j]
                    end_pos = i
                    
    # Calculate the starting position of the longest common substring in seq_1.
    start = end_pos - length
    
    # Extract the longest common substring from seq_1 using the start and end positions.
    sub_sequence = seq_1[start:end_pos]
    
    # Return the longest common substring, its length, and the original input strings for reference.
    return (sub_sequence, length, seq_1, seq_2)



i=0
while i <10:
    
    
    seq_1 = generate_dna_fragment(); read_len_1 = len(seq_1)
    seq_2 = generate_dna_fragment(); read_len_2 = len(seq_2)
    
    output = longest_sub_seq(seq_1, seq_2, read_len_1, read_len_2)

    
    print('The longest subsequence of {} & {}, is a {} base-pair subsequence {}\n'.format(seq_1, seq_2, output[1], output[0]))

    
    i+=1
    