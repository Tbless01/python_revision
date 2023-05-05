# for i in range(1, 13, 1):
#     if i > 1:
#         print(f"Multiplication table {i}")
#     for j in range(13):
#         if i > 1 and j > 0:
#             print(i, "*", j, "=", i * j)


# todo same as

for i in range(2, 13, 1):
    print(f"Multiplication table {i}")
    for j in range(1, 13):
        print(f"{i} * {j} = {i * j}")

