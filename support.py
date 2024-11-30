import numpy as np

def read_sequence_db(db_path):
    file = open(db_path, 'r') 
    all_lines = file.readlines() 
    sequence_lines = [v for i, v in enumerate(all_lines) if all_lines[i][0] != '>']
    return sequence_lines

def read_sequences(seq_path):
    file = open(seq_path, 'r') 
    all_lines = file.readlines() 
    return all_lines

def calculate_support(db,sequences):
    
    supports = np.zeros(len(sequences), dtype='uint16')
    for i in range(len(sequences)):
        seq =  list(sequences[i])
        if seq[-1]=='\n':
            seq = seq[:len(seq)-1]
        for db_row in range(len(db)):
            current_row =  list(db[db_row])
            if current_row[-1]=='\n':
                current_row = current_row[:len(current_row)-1]
            pointer = 0
            matched = []
            for c in range(len(current_row)):
                if current_row[c] == seq[pointer]:
                    pointer = pointer + 1
                    matched.append(current_row[c])
                if matched == seq:
                    supports[i] = supports[i] + 1
                    break

    for i in range(len(sequences)):
        seq =  list(sequences[i])
        if seq[-1]=='\n':
            seq = seq[:len(seq)-1]
        seq = ''.join(map(str, seq)) 
        print('{0} - {1}'.format(seq,supports[i]))
            
            


if __name__ == '__main__':
    
    db_path = 'FILE1.txt'
    db = read_sequence_db(db_path)
    
    sequence_path = 'FILE2.txt'
    sequences = read_sequences(sequence_path)
    
    calculate_support(db,sequences)
    
    
