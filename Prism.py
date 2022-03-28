def surface_prism(l,h,b):
    surface = 2*((l*b) + (l*h) + (b*h))
    return surface

def volume_prism(l,b,h):
    volume=l*b*h
    return volume

def diaganol_prism(l,b,h):
    diaganal = ((l * l) + (b * b )+ (h * h))
    sqrt = diaganal ** 0.5
    return sqrt

if __name__=="__main__":
    l=int(input("Enter Length : "))
    b=int(input("Enter Breath : "))
    h=int(input("Enter Height : "))
    surface=surface_prism(l,h,b)
    print(surface)
    volume=volume_prism(l,b,h)
    print(volume)
    diagonal=diaganol_prism(l,b,h)
    print(diagonal)