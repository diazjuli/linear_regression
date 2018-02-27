def ft_linear_regression(n, x, y):
    parameters = []
    w = covariance(n, x, y) / variance(n, x)
    b = mean(y) - w * mean(x)
    parameters.append(w)
    parameters.append(b)
    return parameters


def covariance(n, x, y):
    result = 0
    x_mean = mean(x)
    y_mean = mean(y)
    for index in range(0, n - 1):
        result += (x[index] - x_mean) * (y[index] - y_mean)
    return result


def variance(n, x):
    result = 0
    x_mean = mean(x)
    for index in range(0, n - 1):
        result += (x[index] - x_mean) * (x[index] - x_mean)
    return result


def mean(x):
    result = 0
    count = 0
    for index in x:
        count += 1
        result += index
    return result / count