n = int(input())

if n == 0:
    print(0)
    exit()

if n == 1:
    print(3)
    exit()

if n == 2:
    print(6)
    exit()

letters = ['A', 'S', 'V']

pairs = {('A', 'S') : 1, ('A', 'V') : 1, ('S', 'A') : 1,
         ('S', 'V') : 1, ('V', 'A') : 1, ('V', 'S') : 1,
        }

for _ in range(3, n + 1):
    newpairs = {}

    for(fir,sec), count in pairs.items():
        for c in letters:
            if c == sec:
                continue
            
            if fir == 'S' and sec == 'V' and c == 'A':
                continue
            
            news = (sec, c)
            newpairs[news] = newpairs.get(news, 0) + count
    pairs = newpairs

result = sum(pairs.values())
print(result)


