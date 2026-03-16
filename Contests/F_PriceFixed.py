limits = {}
for _ in range(int(input())):
    x, y = map(int,input().split())
    limits[y] = limits.get(y, 0) + x

# key => limit 7:2  pur = 7 , 2
# value => amount needed 
#{7:2,8:2,2:1,4:2,8:1}

# {2:1,4:2,7:2,8:3}
# {2:1,4:2,7:2,8:1}  => pur = 2, rub = 4
#  {4:2,7:2,8:1} => pur = 3  rub = 5
#  {4:2,7:2} => pur = 4 rub = 7
#  {7:2} => pur = 6  rub = 9
#  {7:1} => pur = 7  rub = 11
#  {} => pur = 8 rub = 12
# rub 12

    count = sorted(limits.keys())
# {2:1,4:2,7:2}
#count = [4,7,8]
    i, j = 0, len(count) - 1
# i,j = 0,3
    spent, purchased = 0, 0

    while i <= j:
        if count[i] <= purchased: # min_limit <= prev_prod_count  4<=3
            spent += limits[count[i]]
            purchased += limits[count[i]]
            i += 1
        else:
            exp = count[i]
            diff = exp - purchased # {2:1,4:2,7:2} min(2,1) = 1
            diff = min(exp-purchased, limits[count[j]])  #pur = 1, needed = 2 => req = needed - pur
            spent += 2 * diff #rub = 2diff
            purchased += diff
            limits[count[j]] -= diff
             # {2:1,4:2,7:1,8:0}
            if limits[count[j]] == 0:
                j -= 1

print(spent)