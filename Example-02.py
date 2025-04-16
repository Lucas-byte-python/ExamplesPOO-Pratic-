#Object Television Test-----------------------------------------
class Television:
    def __init__(self, pchannel, min, max):
        self.channel = pchannel
        self.cmin = min
        self.cmax = max

    def change_channel_to_low(self):
        self.channel -= 1

    def change_channel_to_up(self):
        self.channel += 1

tv1 = Television(2, 2, 10)
print(tv1.channel)
for x in range(1, 20):
    tv1.change_channel_to_up()
    print(tv1.channel)
print()
print()

tv2 = Television(10, 2, 10)
print(tv2.channel)
for x in range(1, 20):
    tv2.change_channel_to_low()
    print(tv2.channel)
print()
print()

#Format Correct------------------------------------------------
class Television:
    def __init__(self, pchannel, min, max):
        self.channel = pchannel
        self.cmin = min
        self.cmax = max

    def change_channel_to_low(self):
        if self.channel - 1 >= self.cmin:
            self.channel -= 1
        else:
            self.channel = self.cmax

    def change_channel_to_up(self):
        if self.channel + 1  <= self.cmax:
            self.channel += 1
        else:
            self.channel = self.cmin

tv1 = Television(9, 2, 10)
print(tv1.channel)

tv1.change_channel_to_up()
print(tv1.channel)

tv1.change_channel_to_up()
print(tv1.channel)

tv1.change_channel_to_up()
print(tv1.channel)

print()
print()

tv2 = Television(3, 2, 10)
print(tv2.channel)

tv2.change_channel_to_low()
print(tv2.channel)

tv2.change_channel_to_low()
print(tv2.channel)

tv2.change_channel_to_low()
print(tv2.channel)

print()
print()
# Three Example-----------------------------------------------
class Television:
    def __init__(self, pchannel, min, max):
        self.channel = pchannel
        self.cmin = min
        self.cmax = max

    def chage_channel_to_low(self):
            self.channel -= 1

    def chage_channel_to_up(self):
            self.channel += 1

tev1 = Television(50 , 20,  100 )
print(f"Synced Channel: ",tev1.channel)

print(f"Changing Channel to Up")
for x in  range (1, 20):
    tev1.chage_channel_to_up()
    print(f"Synced Channel: ",tev1.channel)

tev2 = Television(10, 2, 10)
print()
print()

print(f"Synced Channel: ",tev2.channel)
print(f"Changing Channel to Low")
for x in  range (1, 20):
    tev2.chage_channel_to_low()
    print(f"Synced Channel: ",tev2.channel)

