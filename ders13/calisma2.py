# =============================================================================
# TAPŞIRIQ 2 — Dərs 4–5: müqayisə, məntiq, if/elif/else, siyahı
# =============================================================================
"""
"İmtahan balı" sistemi.

1) Boş bir siyahı yaradın (ballar).

2) İstifadəçidən döngü ilə (məsələn, 5 dəfə və ya "stop" yazana qədər) bal
   daxil etdirin; hər balı int-ə çevirib siyahıya əlavə edin.

3) Əgər siyahı boşdursa, "Hech bir bal daxil edilmeyib" deyin və davam etməyin.

4) Orta balı tapın: sum(ballar) / len(ballar). Ortaya görə qiymət verin:
   orta >= 90 → "A", >= 80 → "B", >= 70 → "C", >= 60 → "D", əks halda "F".
   Bunu if / elif / else ilə yazın.

5) Ən yüksək və ən aşağı balı max() və min() ilə çap edin.
"""

ballar = []
for i in range(5):
    bal = input("Bal daxil edin: ")
    if bal == "stop":
        break
    ballar.append(int(bal))


if not ballar:
    print("Hec bir bal daxil edilmeyib.")
else:
    orta_bal = sum(ballar) / (len(ballar))
    if orta_bal >= 90:
        qiymet = "A"
    elif orta_bal >= 80:
        qiymet = "B"
    elif orta_bal >= 70:
        qiymet = "C"
    elif orta_bal >= 60:
        qiymet = "D"
    else:
        qiymet = "F"
    print(f'Qiymet: {qiymet}, max: {max(ballar)}, min: {min(ballar)}, orta bal: {orta_bal}')