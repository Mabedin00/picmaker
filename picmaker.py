def inside_face(i, j):
    if (i <= 400 and i >= 130 and j <= 400 and j >= 100 ):
        if (i >= 125 and i <= 150 and (j >= 125 and j <= 150 or j >= 350 and j <= 375) ):
            return False
        return True
    return False

def inside_eyes(i, j):
    if (i >= 100 and i <= 175 and j >= 100 and j <= 175):
        if (i >= 125 and i <= 150 and j >= 125 and j <= 150 ):
            return False
        return True
    elif (i >= 100 and i <= 175 and j >= 325 and j <= 400):
        if (i >= 125 and i <= 150 and j >= 350 and j <= 375 ):
            return False
        return True
    return False

def inside_mouth(i,j):
    if (i >= 250 and j >= 150 and i <= 350 and (1.25*(i - 150) + 100) >= j):
        return True
    else:
        return False

def picmaker():
    f = open("pic.ppm", "w")
    length = 500
    width = 500
    f.write("P3 \n{} {} \n255 \n".format(length, width))
    f.close
    f = open("pic.ppm", "a")
    i = 0
    j = 0
    while (i < length):
        while(j < width):
            if (inside_face(i,j) or inside_eyes(i, j) or inside_mouth(i,j)):
                if (inside_eyes(i, j)):
                    string = "{} {} {} ".format(255,255,255)
                    f.write(string)
                elif (inside_mouth(i,j)):
                    string = "{} {} {} ".format(255,0,0)
                    f.write(string)
                elif (inside_face(i,j)):
                    string = "{} {} {} ".format(0,255,0)
                    f.write(string)
            else:
                string = "{} {} {} ".format(0,0,0)
                f.write(string)
            j += 1
        f.write("\n")
        j = 0
        i += 1

picmaker()
