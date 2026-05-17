"""
İstifadəçidən müddəti gün, saat, dəqiqə və saniyə kimi oxuyan skript yazın.
Bu müddətlə bərabər olan ümumi saniyə sayını hesablayın və terminalda göstərin.
"""

"""
Məs.:
Gün daxil edin: 2
Saat daxil edin: 12
Dəqiqə daxil edin: 5
Saniyə daxil edin: 30

Cəmi saniyə: 216330
"""

g = int(input("gun: "))
s = int(input("saat: "))
d = int(input("deqiqe: "))
sn = int(input("saniye: "))

print(86400*g+3600*s+60*d+sn)