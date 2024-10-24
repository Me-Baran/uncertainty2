from model import model

# Calciulate the probability for a given observation
probability = model.probability([["heavy", "no", "delayed", "attend"]])
print(probability)