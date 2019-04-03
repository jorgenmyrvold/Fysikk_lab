import numpy as np
import matplotlib.pyplot as plt
from eulers_metode import iptrack


antall_malinger = 25
x_start = -0.03
x_slutt = 1.3

tid_bane1 = np.zeros(25)
tid_bane2 = np.zeros(22)  # Fordi vi kun har 22 gyldige målinger for bane2
tid_bane3 = np.zeros(25)


for test in range(1, antall_malinger+1):
    p, t, x_malt, y_malt = iptrack('fysikk_lab/malinger_txt/bane1/Bane1-'+str(test)+'.txt')
    idx_slutt = min(min(np.where(x_malt > x_slutt)))
    idx_start = min(min(np.where(x_malt > x_start)))
    tid = t[idx_slutt] - t[idx_start]
    tid_bane1[test-1] = tid


input_index = 0
for test in range(1, antall_malinger+1):
    try:
        p, t, x_malt, y_malt = iptrack('fysikk_lab/malinger_txt/bane2/Bane2-' + str(test) + '.txt')
        idx_slutt = min(min(np.where(x_malt > x_slutt)))
        idx_start = min(min(np.where(x_malt > x_start)))
        tid = t[idx_slutt] - t[idx_start]
        tid_bane2[test - input_index - 1] = tid
    except:
        input_index += 1
        print("Mangler målinger for bane2 test", test)


for test in range(1, antall_malinger+1):
    p, t, x_malt, y_malt = iptrack('fysikk_lab/malinger_txt/bane3/Bane3-'+str(test)+'.txt')
    idx_slutt = min(min(np.where(x_malt > x_slutt)))
    idx_start = min(min(np.where(x_malt > x_start)))
    tid = t[idx_slutt] - t[idx_start]
    tid_bane3[test-1] = tid


tid_bane1_avg = np.average(tid_bane1)
tid_bane2_avg = np.average(tid_bane2)
tid_bane3_avg = np.average(tid_bane3)

tid_bane1_sd = np.std(tid_bane1)
tid_bane2_sd = np.std(tid_bane2)
tid_bane3_sd = np.std(tid_bane3)

print("\nBane 1 (Rett):    \tTid: %7.4f \tStandardavvik: %8.5f" % (tid_bane1_avg, tid_bane1_sd))
print("Bane 2 (Krum opp):\tTid: %7.4f \tStandardavvik: %8.5f" % (tid_bane2_avg, tid_bane2_sd))
print("Bane 3 (Krum ned):\tTid: %7.4f \tStandardavvik: %8.5f" % (tid_bane3_avg, tid_bane3_sd))

print(tid_bane2)
