var_array = [i for i in range(101)]

jumlah_elemen = len(var_array)
jumlah_total = 0
for i in var_array:
    jumlah_total += i

result = jumlah_total / jumlah_elemen

print (result)