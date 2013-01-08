import os
import Image

picture_path = "c:\\Documents and Settings\\uidu6087\\My Documents\\My Pictures"
picture_name = "2011-Ram-Logo-29_crop"
os.chdir(picture_path)

im = Image.open( picture_name + '.bmp' )
file_output = open(os.path.join(picture_path, picture_name + '.c'), mode='w', buffering=1)

xsize, ysize = im.size
RGBData = []
output_line = ''
pix_per_line = 4
dot_count = 0
pix_count_total = 0

r = 0
g = 1
b = 2
alpha = 3

file_output.write("const uint32 pgluBitmap[ {0} ] = \n".format(xsize * ysize))
file_output.write("{\n")
# read picture into a dict.
for y in range(ysize):
    for x in range(xsize):
        dot_count = dot_count + 1
        dot = (x, y)
        pix_count_total = pix_count_total + 1
        output_line = output_line + '0x' + 'FF' + hex(im.getpixel(dot)[r])[2:].zfill(2) + hex(im.getpixel(dot)[g])[2:].zfill(2) + hex(im.getpixel(dot)[b])[2:].zfill(2) + 'ul' + ', '

        if dot_count >= 4:
            if y == ysize - 1 and x == xsize - 1:
                output_line = output_line[:-2]

            output_line = output_line + '\n'
            file_output.write(output_line)
            output_line = ''
            dot_count = 0

if y == ysize - 1 and dot_count != 0:
    output_line = output_line[:-2] + '\n'
    file_output.write(output_line)
    output_line = ''

file_output.write("};\n")

print(pix_count_total)