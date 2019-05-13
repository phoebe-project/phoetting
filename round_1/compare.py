import numpy as np
import matplotlib.pyplot as plt

d = np.genfromtxt('round_1.data.csv', delimiter=',')
models = ['TRUE', 'Angela_1', 'Angela_2', 'Angela_3', 'Angela_4', 'Dave', 'Joe', 'Bert']

plt.xlabel('r1+r2')
plt.ylabel('r2/r1')
for i in range(1, 9):
    plt.errorbar(d[9,i], d[11,i], xerr=d[10,i], yerr=d[12,i], fmt='o', label=models[i-1])
plt.legend(loc='lower right')
plt.savefig('radii.pdf')
plt.show()

plt.xlabel('ecosw')
plt.ylabel('esinw')
for i in range(1, 9):
    plt.errorbar(d[15,i], d[13,i], xerr=d[16,i], yerr=d[14,i], fmt='o', label=models[i-1])
plt.legend(loc='lower right')
plt.savefig('eccs.pdf')
plt.show()

plt.xlabel('T2/T1')
plt.ylabel('incl')
for i in range(1, 9):
    plt.errorbar(d[7,i], d[3,i], xerr=d[8,i], yerr=d[4,i], fmt='o', label=models[i-1])
plt.legend(loc='upper left')
plt.savefig('teffincl.pdf')
plt.show()

plt.xlabel('qphot')
plt.ylabel('l3')
for i in range(1, 9):
    plt.errorbar(d[1,i], d[19,i], xerr=d[2,i], yerr=d[20,i], fmt='o', label=models[i-1])
plt.legend(loc='upper left')
plt.savefig('ql3.pdf')
plt.show()
