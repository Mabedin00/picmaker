def picmaker():
    f = open("pic1.ppm", "w")
    length = 500
    width = 500
    f.write("P3 \n{} {} \n255 \n".format(length, width))
    f.close
    f = open("pic1.ppm", "a")
    i = 0
    j = 0
    while (i < length):
        while(j < width):
            string = "{} {} {} ".format(j*i % 250 , (abs(width - j*i)) % 250, 255 )
            f.write(string)
            j += 1
        f.write("\n")
        j = 0
        i += 1


picmaker()
