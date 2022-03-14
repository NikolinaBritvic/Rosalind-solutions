# Find the Reverse Complement of a DNA String

def ReverseComplement(a):
    complement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}
    return ''.join([complement[base] for base in a[::-1]])

a=input("Unos: ")
print(ReverseComplement(a))
