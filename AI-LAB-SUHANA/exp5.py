def minimax(level, position, maximizing, values, max_level):

    if level == max_level:
        return values[position]

    left = minimax(level + 1, position * 2, not maximizing, values, max_level)
    right = minimax(level + 1, position * 2 + 1, not maximizing, values, max_level)

    if maximizing:
        return max(left, right)
    else:
        return min(left, right)


# Main program
values = list(map(int, input("Enter 8 leaf node values: ").split()))

tree_height = 3
answer = minimax(0, 0, True, values, tree_height)

print("Optimal value:", answer)