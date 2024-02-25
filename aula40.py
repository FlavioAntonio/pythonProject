def generator(n=0, maximum=10):
    while True:
        yield n
        n += 1

        if n >= maximum:
            return
gen = generator(maximum=40)
for n in gen:
    print(n)