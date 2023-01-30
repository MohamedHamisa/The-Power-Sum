def powerSum(X, N, a=1):
    if X < 0 or X < a**N:
        return 0
    if X == 0 or X == a**N:
        return 1
    return powerSum(X-a**N, N, a+1) + powerSum(X, N, a+1)

