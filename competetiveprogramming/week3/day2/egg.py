# We'll use the first egg to get a range of possible floors that contain the highest floor an egg can be dropped from without breaking. To do this, we'll drop it from increasingly higher floors until it breaks, skipping some number of floors each time.

# When the first egg breaks, we'll use the second egg to find the exact highest floor an egg can be dropped from. We only have to drop the second egg starting from the last floor where the first egg didn't break, up to the floor where the first egg did break. But we have to drop the second egg one floor at a time.

# With the first egg, if we skip the same number of floors every time, the worst case number of drops will increase by one every time the first egg doesn't break. To counter this and keep our worst case drops constant, we decrease the number of floors we skip by one each time we drop the first egg.
#   Highest floor an egg won't break from
# 13

# Floors we drop first egg from
# 14

# Floors we drop second egg from
# 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13

# Total number of drops
# 14
#   Highest floor an egg won't break from
# 98

# Floors we drop first egg from
# 14, 27, 39, 50, 60, 69, 77, 84, 90, 95, 99

# Floors we drop second egg from
# 96, 97, 98

# Total number of drops
# 14
