#DNA input
def length():
    if bases == 1:
        print('Length = {} base, {} codons. \n'.format(bases, codons))
    elif 3 < bases < 6:
        print('Length = {} bases, {} codon. \n'.format(bases, codons))
    else:
        print('Length = {} bases, {} codons. \n'.format(bases, codons))

seq = input('Enter DNA sequence: ').upper()
seq = ''.join(i for i in seq if i.isalpha())
bases = len(seq)
codons = len(seq)//3

print('\n' + seq)
length()

#Frame generator
def frameGen(n):
    frame = [seq[i:i+3] for i in range(n-1, bases, 3)]
    frame = [c for c in frame if len(c) == 3]
    return frame

frame1 = frameGen(1)
frame2 = frameGen(2)
frame3 = frameGen(3)

#Sense strand DNA codon translator (5'->3')
code = {'TTT': 'Phe', 'TTC': 'Phe', 'TTA': 'Leu', 'TTG': 'Leu',
        'CTT': 'Leu', 'CTC': 'Leu', 'CTA': 'Leu', 'CTG': 'Leu',
        'ATT': 'Ile', 'ATC': 'Ile', 'ATA': 'Ile', 'ATG': 'Met',
        'GTT': 'Val', 'GTC': 'Val', 'GTA': 'Val', 'GTG': 'Val',
        'TCT': 'Ser', 'TCC': 'Ser', 'TCA': 'Ser', 'TCG': 'Ser',
        'CCT': 'Pro', 'CCC': 'Pro', 'CCA': 'Pro', 'CCG': 'Pro',
        'ACT': 'Thr', 'ACC': 'Thr', 'ACA': 'Thr', 'ACG': 'Thr',
        'GCT': 'Ala', 'GCC': 'Ala', 'GCA': 'Ala', 'GCG': 'Ala',
        'TAT': 'Tyr', 'TAC': 'Tyr', 'TAA': 'Stop (Ochre)', 'TAG': 'Stop (Amber)',
        'CAT': 'His', 'CAC': 'His', 'CAA': 'Gln', 'CAG': 'Gln',
        'AAT': 'Asn', 'AAC': 'Asn', 'AAA': 'Lys', 'AAG': 'Lys',
        'GAT': 'Asp', 'GAC': 'Asp', 'GAA': 'Glu', 'GAG': 'Glu',
        'TGT': 'Cys', 'TGC': 'Cys', 'TGA': 'Stop (Opal)', 'TGG': 'Trp',
        'CGT': 'Arg', 'CGC': 'Arg', 'CGA': 'Arg', 'CGG': 'Arg',
        'AGT': 'Ser', 'AGC': 'Ser', 'AGA': 'Arg', 'AGG': 'Arg',
        'GGT': 'Gly', 'GGC': 'Gly', 'GGA': 'Gly', 'GGG': 'Gly'
        }

def translator(sequence):
    protein = [code.get(c) for c in sequence]
    print(' '.join(sequence) + '\n')
    print(' '.join(protein) + '\n')

#Protein output
print('Frame 1:')
translator(frame1)
print('Frame 2:')
translator(frame2)
print('Frame 3:')
translator(frame3)

#next - remove new lines from sequence
#next - convert to protein name
#def protein(aminoSeq):
