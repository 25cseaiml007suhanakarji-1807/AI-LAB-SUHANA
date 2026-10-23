def alpha_beta(level, position, maximizing, values, max_level, alpha, beta):

    if level == max_level:
        return values[position]

    if maximizing:
        best_value = float('-inf')

        for child in [0, 1]:
            value = alpha_beta(
                level + 1,
                position * 2 + child,
                False,
                values,
                max_level,
                alpha,
                beta
            )

            best_value = max(best_value, value)
            alpha = max(alpha, best_value)

            if alpha >= beta:
                break

        return best_value

    else:
        best_value = float('inf')

        for child in [0, 1]:
            value = alpha_beta(
                level + 1,
                position * 2 + child,
                True,
                values,
                max_level,
                alpha,
                beta
            )

            best_value = min(best_value, value)
            beta = min(beta, best_value)

            if alpha >= beta:
                break

        return best_value


# Main program
values = list(map(int, input("Enter 8 leaf node values: ").split()))

tree_height = 3
answer = alpha_beta(
    0, 0, True, values, tree_height,
    float('-inf'), float('inf')
)

print("Optimal value:", answer)