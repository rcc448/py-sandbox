#software per il calcolo della radice quadrata
#con il metodo di bisezione


def bisection(x_in, initial_min, initial_max):

    x_min = initial_min
    x_max = initial_max
    guess = (x_max + x_min) /2
    while abs(guess ** 2 - x_in) > 0.001:
        if guess ** 2 > x_in:
            x_max = guess
            guess = (x_min + guess) / 2
        else:
            x_min = guess
            guess = (x_max + guess) / 2
    return guess

x = float(input("Prego inserire il valore:"))
if x < 0:
    print("La radice quadrata è definita solo per x > 0")
else:
    solution = "placeholder"
    # considerato che la radice quadrata ha per
    # definizione x > 0 bisogna distinguere due casi

    # x > 1 la radice quadrata di x è strettamente minore
    # di x
    if x > 1.0:
        solution = bisection(x, 1, x)
    elif x == 1.0:
        solution = 1.0
    else:
        # caso x < 1 allora la radice è > di x
        solution = bisection(x, 0, 1)

    print(f"la radice quadrata di {x} è {solution}")