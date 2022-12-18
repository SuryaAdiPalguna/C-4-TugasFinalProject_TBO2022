# CFG
# ======================================================================================

# K → S P | S P Pel | S P O | S P Ket | S P O Pel | S P O Ket

# S -> NP 
# P -> VP | AdjP | NP
# O -> NP
# Pel -> NP | AdjP | NumP | VP | PP | NP VP
# Ket -> PP | NP

# NP → Noun | PropNoun | Pronoun | NP Noun | NP Adj | NP PropNoun | NP Pronoun | NumP NP
# VP → Verb | Adv VP
# AdjP → Adv AdjP | Adj
# PP → Prep NP
# NumP → Num | NumP Num | NumP Noun


# CNF
# ======================================================================================

# K -> S P
# K -> K Pel
# K -> K O
# K -> K Ket

# S -> Noun | PropNoun | Pronoun | NP Noun | NP Adj | NP PropNoun | NP Pronoun | NumP NP

# P -> Verb | Adv VP
# P -> Adj | Adv AdjP
# P -> Noun | PropNoun | Pronoun | NP Noun | NP Adj | NP PropNoun | NP Pronoun | NumP NP

# O -> Noun | PropNoun | Pronoun | NP Noun | NP Adj | NP PropNoun | NP Pronoun | NumP NP

# Pel -> Noun | PropNoun | Pronoun | NP Noun | NP Adj | NP PropNoun | NP Pronoun | NumP NP
# Pel -> Adj | Adv AdjP
# Pel -> Num | NumP Num | NumP Noun
# Pel -> Verb | Adv VP
# Pel -> Prep NP
# Pel -> NP VP

# Ket -> Prep NP
# Ket -> Noun | PropNoun | Pronoun | NP Noun | NP Adj | NP PropNoun | NP Pronoun | NumP NP

# NP → Noun | PropNoun | Pronoun | NP Noun | NP Adj | NP PropNoun | NP Pronoun | NumP NP
# VP → Verb | Adv VP
# AdjP → Adv AdjP | Adj
# PP → Prep NP
# NumP → Num | NumP Num | NumP Noun


import general

variable = ["K", "S", "P", "O", "Pel", "Ket", "NP", "VP", "AdjP", "PP", "NumP", "Verb", "Noun", "Adj", "Adv", "Num", "Prep", "PropNoun", "Pronoun"]
production = {
    "K" : ["SP", "KPel", "KO", "KKet"],
    "S" : general.kata_benda + general.proper_noun + general.kata_ganti + ["NPNoun", "NPAdj", "NPPropNoun", "NPPronoun", "NumPNP"],
    "P" : general.kata_kerja + ["AdvVP"] + general.kata_sifat + ["AdvAdjP"] + general.kata_benda + general.proper_noun + general.kata_ganti + ["NPNoun", "NPAdj", "NPPropNoun", "NPPronoun", "NumPNP"],
    "O" : general.kata_benda + general.proper_noun + general.kata_ganti + ["NPNoun", "NPAdj", "NPPropNoun", "NPPronoun", "NumPNP"],
    "Pel" : general.kata_benda + general.proper_noun + general.kata_ganti + ["NPNoun", "NP Adj", "NP PropNoun", "NP Pronoun", "NumP NP"] + general.kata_sifat + ["AdvAdjP"] + general.numeralia + ["NumPNum", "NumPNoun"] + general.kata_kerja + ["AdvVP"] + ["PrepNP"] + ["NPVP"],
    "Ket" : ["PrepNP"] + general.kata_benda + general.proper_noun + general.kata_ganti + ["NPNoun", "NPAdj", "NPPropNoun", "NPPronoun", "NumPNP"],
    "NP" : general.kata_benda + general.proper_noun + general.kata_ganti + ["NPNoun", "NPAdj", "NPPropNoun", "NPPronoun", "NumPNP"],
    "VP" : general.kata_kerja + ["AdvVP"],
    "AdjP" : general.kata_sifat + ["AdvAdjP"],
    "PP" : ["PrepNP"],
    "NumP" : general.numeralia + ["NumPNum", "NumPNoun"],
    "Verb" : general.kata_kerja,
    "Noun" : general.kata_benda,
    "Adj" : general.kata_sifat,
    "Adv" : general.kata_keterangan,
    "Num" : general.numeralia,
    "Prep" : general.preposisi,
    "PropNoun" : general.proper_noun,
    "Pronoun" : general.kata_ganti
}
start_symbol = ["K"]

def check_production(array):
    sum = set()
    for i in array:
        for j in variable:
            if i in production[j]:
                sum.add(j)
    return list(sum)

def check_symbol(array):
    for i in array:
        if i in start_symbol:
            return True
    return False
