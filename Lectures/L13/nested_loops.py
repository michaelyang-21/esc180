# nested loops

counter = 0
for i in range(5):
    for j in range(3):
        print(counter, "i = ", i, "j = ", j)
        counter += 1

# unrolling the loop
counter = 0
i = 0
for j in range(3):


