# My Attempt-----------------------------------------------------
class Television:
    def __init__(self, pchannel, min, max):
        self.channel = pchannel
        self.cmin = min
        self.cmax = max

    def chage_channel_to_low(self):
        if self.channel <= self.cmin:
            self.channel = self.cmax
        else:
            self.channel -= 1

    def chage_channel_to_up(self):
        if self.channel >= self.cmax:
            self.channel = self.cmin
        else:
            self.channel += 1

tev1 = Television(50, 20, 100)
print(f"Synced Channel: {tev1.channel}")

print(f"Changing Channel to Up")
for x in range(1, 20):
    tev1.chage_channel_to_up()
    print(f"Synced Channel: {tev1.channel}")

tev2 = Television(10, 2, 10)
print("\n")
print(f"Synced Channel: {tev2.channel}")
print(f"Changing Channel to Low")
for x in range(1, 20):
    tev2.chage_channel_to_low()
    print(f"Synced Channel: {tev2.channel}")


class Televisão:
    def __init__(self, pcanal, min, max):
        self.canal = pcanal
        self.cmin = min
        self.cmax = max

    def muda_canal_para_baixo(self):
        if self.canal - 1 >= self.cmin:
            self.canal -= 1
        else:
            self.canal = self.cmax

    def muda_canal_para_cima(self):
        if self.canal + 1 <= self.cmax:
            self.canal += 1
        else:
            self.canal = self.cmin

tv1 = Televisão(9 , 2,  10 )
print(tv1.canal)
tv1.muda_canal_para_cima()
print(tv1.canal)
tv1.muda_canal_para_cima()
print(tv1.canal)

tv2 = Televisão(3 , 2,  10 )
print(tv2.canal)
tv2.muda_canal_para_baixo()
print(tv2.canal)
tv2.muda_canal_para_baixo()
print(tv2.canal)

# Alternative Way------------------------------------------------------------------
class Television:
    def __init__(self, current_channel, min_channel, max_channel):
        self.channel = current_channel
        self.min = min_channel
        self.max = max_channel

    def change_channel_down(self):
        if self.channel - 1 >= self.min:
            self.channel -= 1
        else:
            self.channel = self.max

    def change_channel_up(self):
        if self.channel + 1 <= self.max:
            self.channel += 1
        else:
            self.channel = self.min

tv1 = Television(9, 2, 10)
print(tv1.channel)

tv1.change_channel_up()
print(tv1.channel)

tv1.change_channel_up()
print(tv1.channel)

tv2 = Television(3, 2, 10)
print(tv2.channel)

tv2.change_channel_down()
print(tv2.channel)

tv2.change_channel_down()
print(tv2.channel)