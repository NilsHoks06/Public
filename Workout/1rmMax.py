def beregn_styrke(vekt, reps):
    styrkeøkning = vekt * (1 + (reps * 0.03333333333333333))
    return styrkeøkning

# Eksempel: 6 reps med 100 kg på benk
vekt = int(input("Hvor mye vekt tok du?"))
reps = int(input("Hvor mange reps tok du?"))
resultat = beregn_styrke(vekt, reps)
print(f"Styrken etter {reps} repetisjoner med {vekt} kg er: {resultat} kg")