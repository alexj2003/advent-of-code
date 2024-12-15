# Read input
robots = []
with open("input.txt", "r") as f:
    for line in f:
        if line.strip() == "":
            continue
        else:
            p, v = line.strip().split(" ")
            px, py = map(int, p[2:].split(","))
            vx, vy = map(int, v[2:].split(","))
            robots.append((px, py, vx, vy))

WIDTH = 101
HEIGHT = 103

# Calculate the safety factor after i seconds
def calc_safety(robots, i):
    # Quadrant totals
    a = b = c = d = 0

    for j in range(len(robots)):
        # Calculate final position
        px, py, vx, vy = robots[j]
        nx, ny = px + i * vx, py + i * vy
        nx, ny = nx % WIDTH, ny % HEIGHT

        # Update quadrant totals
        a += nx > WIDTH // 2 and ny > HEIGHT // 2
        b += nx > WIDTH // 2 and ny < HEIGHT // 2
        c += nx < WIDTH // 2 and ny > HEIGHT // 2
        d += nx < WIDTH // 2 and ny < HEIGHT // 2
    
    return a * b * c * d

# Part 1
print("Part 1:", calc_safety(robots, 100))
