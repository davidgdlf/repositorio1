import pandas as pd
import matplotlib.pyplot as plt

z1 = ['leganes', 400]
z2 = ['atleti', 520]
z3 = [',madrid', 320]
z4 = ['barsa', 120]
z5 = ['rayo vallecano', 200]

listaequipos = [z1, z2, z3, z4, z5]

equipos = pd.DataFrame(listaequipos, columns=['titulos', 'años'])

print(equipos)

plt.plot(equipos['titulos'], equipos['años'])
plt.show()

plt.scatter(equipos['titulos'], equipos['años'])
plt.show()

plt.barh(equipos['titulos'], equipos['años'])
plt.show()

plt.bar(equipos['titulos'], equipos['años'])
plt.show()

plt.pie(equipos['titulos'], equipos['años'])
plt.show()