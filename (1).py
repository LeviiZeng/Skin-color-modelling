import pandas as pd
from matplotlib import pyplot as plt

df1 = pd.read_excel(r"skinRGB.xlsx")
df2 = pd.read_excel(r"backgroundRGB.xlsx")

SR = df1["R"]
SG = df1["G"]
SB = df1["B"]

BR = df2["R"]
BG = df2["G"]
BB = df2["B"]

for i in range(0,1790):

    Scb = -0.148*SR[i]-0.291*SG[i]+0.439*SB[i]+128
    Scr = 0.439*SR[i]-0.368*SG[i]-0.071*SB[i]+128

    plt.scatter(Scb,Scr, c="blue",s=5,marker="o")

for j in range(0,970):
    Bcb = -0.148 * BR[j] - 0.291 * BG[j] + 0.439 * BB[j] + 128
    Bcr = 0.439 * BR[j] - 0.368 * BG[j] - 0.071 * BB[j] + 128

    plt.scatter(Bcb, Bcr, c="red", s=5, marker="d")
plt.show()
