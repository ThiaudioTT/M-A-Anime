import time

# ---------------------- Peso ------------------
hist_p = 9
persona_p = 6
animation_p = 7.5
diver_p = 10
ts_p = 8.5
ntp_p = 6.8


somatorio_p = hist_p + persona_p + animation_p + diver_p + ts_p + ntp_p

# ----------- Input dados -----------------
historia = float(input("História: "))
personagens = float(input("Personagens: "))
animacao = float(input("Animação: "))
divertimento = float(input("Divertimento: "))
trilha_sonora = float(input("Trilha sonora: "))
NotaPessoal = float(input("Nota pessoal: "))

# --------------------------- Tela -----------


Soma1 = historia * hist_p + persona_p * personagens + animacao * animation_p + divertimento * diver_p + ts_p * trilha_sonora + NotaPessoal * ntp_p


Score = Soma1 / somatorio_p


time.sleep(1)

print("\nSua nota é: {}" .format(Score))

input()
