# z = [1, 2, 4, 65, "aku", "kentang", True, 0.1]
# #ngakses
# print(2)

# #nambahin data dibelakang
# z.append(100)
# print(z)

# #
# z.insert(5)

# #gabungin
# x = {4,6,2}














#list comprehension

l = [
    "metal buntung",
    "kinur petot",
    "kiting ketombe",
    "baco mercon"
]

namaBelakang = [belakang.split(" ")[-1] for belakang in l]
print(namaBelakang)
