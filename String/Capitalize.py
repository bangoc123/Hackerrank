str = raw_input("").strip()

if 0<len(str)<1000:
    elements = str.split(" ")

    for i in range(len(elements)):
        elements[i] = elements[i].capitalize()

    newStr = " ".join(elements)

    print newStr

