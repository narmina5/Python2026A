"""
ele bir kod yazin ki, tersine ve duzune yazilisi eynidirse true qaytarsin

meselen:
kitab -> batik ------> False
ana -> ana -----------> True
"""
soz = input("Soz daxil edin: ")
if soz == soz[::-1]:
    print("Eynidir")
else:
    print("Eyni deyil")