import phoebe
import numpy as np
import matplotlib.pyplot as plt
import autofig

b = phoebe.default_binary()

b.add_dataset('lc', passband='Kepler:mean', dataset='mylc')
b.add_compute(kind='phoebe', compute='mymodel')

b['requiv@primary'] = 1.234
b['requiv@secondary'] = 0.789
b['incl@binary'] = 87.3
b['period@binary'] = 3.1415926
b['q@binary'] = 0.765
b['teff@primary'] = 6322.
b['teff@secondary'] = 5486.
b['t0@system'] = 2453535.5369
b['ecc@orbit'] = 0.142
b['per0@orbit'] = 76.2

t = np.arange(2453542.353, 2453673.535, 29.44/1440)
print(len(t))

b['times@mylc@dataset'] = t
b.run_compute('mymodel')

noise = 0.0006 * np.exp( 0.4 + (t-t[0])/(t[-1]-t[0]) ) + np.random.normal(0.0, 0.0003, len(t)) - 0.002*(t-t[0])**2/(t[-1]-t[0])**2 + 0.0001*(t-t[0])/(t[-1]-t[0]) + 0.0001
noise -= np.mean(noise)

with open('lc.kepler.data', 'w') as f:
    for i in range(len(t)):
        f.write('%f  %f  %f\n' % (b['value@times@mylc@mymodel'][i], b['value@fluxes@mylc@mymodel'][i] + noise[i], 0.0003))

b.plot(x='phase', marker='o', linestyle='None', save='lc.png')
