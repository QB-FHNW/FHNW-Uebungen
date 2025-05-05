import matplotlib.pyplot as plt

plt.plot([1,2,3,4],[1,4,9,16], 'g')     # , 'bo' kann weggelassen werden - dann werden punkte angezeigt. oder mit'g' wird die anzeige grün.and
plt.axis([0,5,6,20])    # x-Achse (0 bis 5), y-Achse (6 bis 20) anzeigen
plt.xlabel('Äpfel')     # Achsenbeschriftung
plt.ylabel('Birnen')    # Achsenbeschriftung

plt.show()