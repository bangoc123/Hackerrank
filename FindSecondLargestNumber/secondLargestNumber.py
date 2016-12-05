n = int(raw_input(""))

x = raw_input("")

y = [int(x) for x in x.split(" ")]

if len(y) == n and 2 <= len(y) <= 10:

    first = None

    second = None

    for number in y:

        if number > first:
            second = first
            first = number
        if second < number < first:
            second = number
    print second



