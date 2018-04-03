import numpy as np
import matplotlib.pyplot as plt


#Datos de C++
cN = np.genfromtxt("times_cpp.csv", delimiter = ",", usecols = 0)
ct = np.genfromtxt("times_cpp.csv", delimiter = ",", usecols = 1) 

#Datos de python
pN = np.genfromtxt("times_python.csv", delimiter = ",", usecols = 0)
pt = np.genfromtxt("times_python.csv", delimiter = ",", usecols = 1)

plt.plot(cN,ct, label = "C++")
plt.plot(pN,pt, c = "g",label = "Python")
plt.title("Tiempo C++ y Python")
plt.xlabel("N")
plt.ylabel("Tiempo")

plt.legend(loc = 2)

plt.savefig("cpp_vs_python.png")
