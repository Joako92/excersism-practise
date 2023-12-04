import unittest

def proteins(strand):
##    Creo una lista separando cada letra del 'VALUE'
    codon_list = list(strand)
    
##    Creo nuevos strings cada 3 valores de la lista
    codon_1 = "".join(codon_list[0:3])
    codon_2 = "".join(codon_list[3:6])
    codon_3 = "".join(codon_list[6:9])
    
##    Creo una nueva lista a partir de los 3 strings anteriores
    codons = [codon_1, codon_2, codon_3]
    
##    Lista vacia para ir guardando las proteinas que reciba del 'for loop'
    protein = []
    
##    Inicia un 'for loop' por cada valor en la lista 'codons'
    for codon in codons:     
        if codon == "AUG":
            protein.append("Methionine")
        elif codon == "UUU" or codon == "UUC":
            protein.append("Phenylalanine")
        elif codon == "UUA" or codon == "UUG":
            protein.append("Leucine")
        elif codon == "UCU" or codon == "UCC" or codon == "UCA" or codon == "UCG":
            protein.append("Serine")
        elif codon == "UAU" or codon == "UAC":
            protein.append("Tyrosine")
        elif codon == "UGU" or codon == "UGC":
            protein.append("Cysteine")
        elif codon == "UGG":
            protein.append("Tryptophan")

##            Si llega aca se devuelve la lista como esta, sin agregar mas valores
        elif codon == "UAA" or codon == "UAG" or codon == "UGA":
            return protein

##        Devuelve la lista con los valores agregados
    return protein

