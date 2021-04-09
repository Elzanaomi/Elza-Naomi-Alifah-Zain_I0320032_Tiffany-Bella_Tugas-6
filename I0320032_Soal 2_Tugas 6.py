# input jumlah data
n = int(input("\nBanyaknya Data: "))

# input data
print()  # Membuat baris baru
data = []
jum = 0

#hasil
for i in range(0, n):
    temp = int(input("Masukkan data ke-%d: " % (i + 1)))
    data.append(temp)
    jum += data[i]
    rata2 = jum / n

print("\nRata-rata  = %0.2f" % rata2)