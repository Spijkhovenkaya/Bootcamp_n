aantal_studenten = 21 
collegegeld_per_student = 1.377 

totaal_collegegeld = aantal_studenten * collegegeld_per_student

# btw op fruit is 9%
btw_appels = 0.09  
btw_druiven = 0.09  
btw_bananen = 0.09  


kosten_appels = 3.40
kosten_druiven = 2.45
kosten_bananen = 1.95


btw_appels_bedrag = kosten_appels * btw_appels
btw_druiven_bedrag = kosten_druiven * btw_druiven
btw_bananen_bedrag = kosten_bananen * btw_bananen


totaal_btw_fruit = btw_appels_bedrag + btw_druiven_bedrag + btw_bananen_bedrag

print(f"Totaal collegegeld betaald door alle studenten: €{totaal_collegegeld}")
print(f"Totaal BTW voor al het fruit in de fruitmand: €{totaal_btw_fruit:.2f}")
