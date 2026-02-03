def is_surviving(monsters_count, bullet_count, healths, positions):
    monsters = sorted((abs(positions[i]), healths[i]) for i in range(monsters_count))
    lost_points = 0

    for distance, health in monsters:
        lost_points += health
        
        if (bullet_count * distance) < lost_points : 
            print("NO")
            return

    print("YES")