import numpy as np
import pandas as pd

df1 = pd.read_excel(r"C:\Users\admin\Desktop\W05\data\skinRGB.xlsx")

SR = df1["R"]
SG = df1["G"]
SB = df1["B"]


data_cb = -0.148*SR-0.291*SG+0.439*SB+128
mean_cb=np.mean(data_cb)
print("The mean for Cb:", mean_cb)

data_cr = -0.439*SR-0.368*SG+0.071*SB+128
mean_cr = np.mean(data_cr)
print("The mean for Cr:", mean_cr)

cov_matrix=np.cov(data_cb,data_cr)
print("The covariance matrix:", cov_matrix)
