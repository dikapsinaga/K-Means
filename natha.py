def akar_kuadrat(a,threshold):
    error = 1
    xp = a/2
    while error > threshold:
        xn = (xp + (a/xp))/2
        error = abs((xn-xp)/xn)
        xp = xn
    return xn

print(akar_kuadrat(16, 0.1))
print(akar_kuadrat(256,0.1))

import math
hasil_analitik = math.sqrt(16)
hasil_numerik = akar_kuadrat(16,0.1)
#hitung error absolut dan relatif
error_absolut = abs(hasil_analitik - hasil_numerik)
error_relatif = error_absolut/hasil_analitik * 100

print(error_absolut)
print(error_relatif)


import numpy as np
import matplotlib.pyplot as plt

x1 = np.arange(1,100,1)
y1 = [akar_kuadrat(x,100) for x in x1]


plt.plot(x1,y1,'g-',label="fungsi")
plt.xlabel('Nilai x')
plt.ylabel('Eksponensial x')
plt.title('Kurva Eksponensial')
plt.legend(bbox_to_anchor=(1.02, -0.2),loc=4)
plt.show()
