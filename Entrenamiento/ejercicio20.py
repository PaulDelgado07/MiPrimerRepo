import matplotlib.pyplot as plt 

x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]


plt.plot(x, y, color='blue', linestyle= '--', linewidth ='2')

plt.title("Grafico de lineas")
plt.xlabel("Valores(x)")
plt.ylabel("valores(y)")
plt.grid(True)

plt.show()