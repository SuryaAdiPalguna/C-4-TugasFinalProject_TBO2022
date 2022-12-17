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
production = [
    ["S P", "K Pel", "K O", "K Ket"],
    general.kata_benda + general.proper_noun + general.kata_ganti + ["NP Noun", "NP Adj", "NP PropNoun", "NP Pronoun", "NumP NP"],
    general.kata_kerja + ["Adv VP"] + general.kata_sifat + ["Adv AdjP"] + general.kata_benda + general.proper_noun + general.kata_ganti + ["NP Noun", "NP Adj", "NP PropNoun", "NP Pronoun", "NumP NP"],
    general.kata_benda + general.proper_noun + general.kata_ganti + ["NP Noun", "NP Adj", "NP PropNoun", "NP Pronoun", "NumP NP"],
    general.kata_benda + general.proper_noun + general.kata_ganti + ["NP Noun", "NP Adj", "NP PropNoun", "NP Pronoun", "NumP NP"] + general.kata_sifat + ["Adv AdjP"] + general.numeralia + ["NumP Num", "NumP Noun"] + general.kata_kerja + ["Adv VP"] + ["Prep NP"] + ["NP VP"],
    ["Prep NP"] + general.kata_benda + general.proper_noun + general.kata_ganti + ["NP Noun", "NP Adj", "NP PropNoun", "NP Pronoun", "NumP NP"],
    general.kata_benda + general.proper_noun + general.kata_ganti + ["NP Noun", "NP Adj", "NP PropNoun", "NP Pronoun", "NumP NP"],
    general.kata_kerja + ["Adv VP"],
    general.kata_sifat + ["Adv AdjP"],
    ["Prep NP"],
    general.numeralia + ["NumP Num", "NumP Noun"],
    general.kata_kerja,
    general.kata_benda,
    general.kata_sifat,
    general.kata_keterangan,
    general.numeralia,
    general.preposisi,
    general.proper_noun,
    general.kata_ganti
]
start_symbol = ["K"]

def check_production(array):
    sum = set()
    for i in array:
        for n, value in enumerate(production):
            if i in value:
                sum.add(variable[n])
    return list(sum)

def check_symbol(array):
    for i in array:
        if i in start_symbol:
            return True
    return False