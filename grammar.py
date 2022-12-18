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

