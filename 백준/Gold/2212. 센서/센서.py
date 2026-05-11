N = int(input())
K = int(input())
coords = list(map(int, input().split()))

coords = list(set(coords))
coords.sort()
gap = []
for i, c in enumerate(coords):
    if i == len(coords) - 1:
        break

    gap.append(coords[i + 1] - coords[i])
gap.sort(reverse=True)
road_length = coords[-1] - coords[0]
min_length = road_length - sum(gap[:K -1])

print(min_length)


