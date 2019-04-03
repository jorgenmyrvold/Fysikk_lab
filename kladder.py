def avg_iptrack_course(banenr):
    avg_p = []
    poly_arr = []
    ant_malinger = 25
    poly_grad = 16  # Av grad 15, men inneholder 16 elementer pga konstantledd

    for test_nr in range(1, ant_malinger+1):
        p, data = iptrack('fysikk_lab/malinger_txt/bane' + str(banenr) + '/Bane' + str(banenr) + '-' + str(test_nr) + '.txt')
        poly_arr.append(p)

    koeff_all = []
    for i in range(ant_malinger):
        koeff_i = []
        for j in range(poly_grad):
            koeff_i.append(poly_arr[i][j])
        koeff_all.append(koeff_i)

    print('koeff_all', koeff_all)

    """
    for i in range(poly_grad):
        avg_p.append(sum(koeff_all[:, i]) / ant_malinger)
    """
    return avg_p

def avg_iptrack_poly_arr(poly_arr):
    avg_p = []
    ant_malinger = 25
    poly_grad = 16  # Av grad 15, men inneholder 16 elementer pga konstantledd

    for i in range(poly_grad-1):
        avg_p[i] = sum(poly_arr[:, i]) / ant_malinger

    return avg_p


iptrack_bane1 = np.empty([25, 16])
iptrack_bane2 = []
iptrack_bane3 = []

# iptrack for bane 1
for test_nr in range(1, 26):
    p, data = iptrack('fysikk_lab/malinger_txt/bane1/Bane1-' + str(test_nr) + '.txt')
    for i in range(16):
        iptrack_bane1[test_nr-1][i] = p[i]

# print(iptrack_bane1)
# avg_bane1 = avg_iptrack_poly_arr(iptrack_bane1)
# print("\n" + avg_bane1)

# iptrack for bane 2
for test_nr in range(1, 26):
    p, data = iptrack('fysikk_lab/malinger_txt/bane2/Bane2-' + str(test_nr) + '.txt')
    iptrack_bane2.append(p)

# iptrack for bane 3
for test_nr in range(1, 26):
    p, data = iptrack('fysikk_lab/malinger_txt/bane3/Bane3-' + str(test_nr) + '.txt')
    iptrack_bane3.append(p)



