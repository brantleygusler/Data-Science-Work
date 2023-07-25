def mono(image, sepia=False):
height = len(image)
width  = len(image[0])
for row in range(height):
    for col in range(width):
        pixel = image[row][col]
        new_value = 0.3 * pixel.red + 0.6 * pixel.green + 0.1 * pixel.blue
        pixel.red = int(new_value)
        if sepia:
            pixel.green = int(new_value * 0.6)
            pixel.blue = int(new_value * 0.4)
        else:
            pixel.green = pixel.red
            pixel.blue = pixel.red
return True
