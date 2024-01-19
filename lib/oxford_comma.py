def oxford_comma(elements):
    if len(elements) == 1:
        return elements[0]
    elif len(elements) == 2:
        return "{} and {}".format(elements[0], elements[1])
    else:
        comma_separated = ", ".join(elements[:-1])
        return "{}, and {}".format(comma_separated, elements[-1])
    
