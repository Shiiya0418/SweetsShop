import math

saifu = 2000
nedan = [125, 80, 50, 1000, 150, 500]
atari = [11, 8, 5, 100, 14, 33]

kitaichi = [0, 0, 0, 0, 0, 0]
for i in range(6):
    kitaichi[i] = nedan[i] * (1 / atari[i])

best_kitaichi_index = kitaichi.index(max(kitaichi))

kosu = math.floor(saifu / nedan[best_kitaichi_index])

kaukazu = [0, 0, 0, 0, 0, 0]

kaukazu[best_kitaichi_index] = kosu
print(",".join([str(k) for k in kaukazu]))
