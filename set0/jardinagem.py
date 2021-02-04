# PYTHON - MIT - UNICAMP
# =============================================================================
# Created By  : Matheus Percário Bruder
# Created Date: February 1st, 2021
# =============================================================================

comp_lateral = int(input("O comprimento lateral (em metros) de todo o jardim acabado: "))  # 30
dist_plantas = float(input("O espaçamento recomendado (em metros) entre as plantas: "))  # 0.06
prof_canteiros = int(input("A profundidade (em metros) do solo nos canteiros: "))  # 2 
prof_cascalhos = int(input("A profundidade (em metros) do cascalho: "))  # 1

print()
print("=" * 30)
print()

pi = 3.14159
area_tot = comp_lateral ** 2
d_circ_cascalho = (comp_lateral / 2)
r_circ_cascalho = (comp_lateral / 4)

area_circ_cascalho = pi * (r_circ_cascalho ** 2)
area_tot_cascalho = area_circ_cascalho * 3
area_tot_jardim = area_tot - area_tot_cascalho
area_j_pequeno = ((d_circ_cascalho ** 2) - area_circ_cascalho) / 4
area_j_grande = (area_tot - (d_circ_cascalho ** 2) - area_circ_cascalho * 2) / 4 

volume_j_pequeno = round(area_j_pequeno * prof_canteiros, 2)
volume_j_grande = round(area_j_grande * prof_canteiros, 2)
volume_tot_jardim = volume_j_pequeno * 4 + volume_j_grande * 4
volume_tot_cascalho = round(area_tot_cascalho * prof_cascalhos, 2)

num_plantas_j_pequeno = (area_j_pequeno / (dist_plantas ** 2)) // 1
num_plantas_j_grande = (area_j_grande / (dist_plantas ** 2)) // 1 
tot_plantas = num_plantas_j_pequeno * 4 + num_plantas_j_grande * 4

print(f"Quantas plantas cabem em cada canteiro pequeno? {num_plantas_j_pequeno}")
print(f"Quantas plantas cabem em cada canteiro grande? {num_plantas_j_grande}")
print(f"Quantas plantas cabem no jardim como um todo? {tot_plantas}")
print(f"Quanto solo cada canteiro pequeno precisa? (precisão .01 m³): {volume_j_pequeno}")
print(f"Quanto solo cada canteiro grande precisa? (precisão .01 m³): {volume_j_grande}")
print(f"Quanto solo é necessário no total? {volume_tot_jardim}")
print(f"Quanto cascalho é necessário no total? {volume_tot_cascalho}")