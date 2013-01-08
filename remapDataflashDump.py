import os

target_file_path = 'c:\\Projects\\Chrysler\\Documents\\DS13\\whiteScreen2ndFromBill'
file_object = open(os.path.join(target_file_path, 'vp_data.rec'), mode='r', buffering=1)
file_object_bin = open(os.path.join(target_file_path, 'vp_data.tst'), mode='w', buffering=1)

line_num = 0
binary_lines = []
header = 'S315'
address_base = '0x02'
section = 0
section_pre = -1
Line_format = "S3"

beginning_line_num = 2
end_line_num = 4097

for line in  file_object:
    line_num = line_num + 1

    Lineheader = line[0:4]
    if Lineheader != "S315" or line == "":
        continue

    #get rid of new line char.
    line = line.rstrip('\r\n')

    #recalc address offset.
    address_offset = line[6:12]
    address_offset_dec = int(address_offset, 16)
    address_offset_dec_new = int(address_offset_dec / 2)
    address_offset_hex_new = hex(address_offset_dec_new)[2:]

    #calc and print section number.
    section = int(address_offset_dec_new / 2048)
    if section != section_pre:
        binary_lines = "\n=================Block {0}=================\n".format(section)
        file_object_bin.write(binary_lines)
        section_pre = section

    #get interested data.
    data1_str = line[12:20]
    data2_str = line[28:36]
    data1_str_byte = bytes.fromhex(data1_str)
    data2_str_byte = bytes.fromhex(data2_str)

    #convert to ascii.
    data1_str_new = ""
    i = 0
    for i in range(len(data1_str_byte)):
        if (data1_str_byte[i] >= 0x7F) or (data1_str_byte[i] <= 0x1F):
            data1_str_new = data1_str_new + "2E"
        else:
            data1_str_new = data1_str_new + data1_str[2*i] + data1_str[2*i + 1]

    data2_str_new = ""
    i = 0
    for i in range(len(data2_str_byte)):
        if (data2_str_byte[i] >= 0x7F) or (data2_str_byte[i] <= 0x1F):
            data2_str_new = data2_str_new + "2E"
        else:
            data2_str_new = data2_str_new + data2_str[2*i] + data2_str[2*i + 1]

    data1_str_byte_new = bytes.fromhex(data1_str_new)
    data2_str_byte_new = bytes.fromhex(data2_str_new)
    data1_str_ascii = str(data1_str_byte_new)[2:-1]
    data2_str_ascii = str(data2_str_byte_new)[2:-1]

    #re-arrange into new file.
    binary_lines = (address_base + str(address_offset_hex_new).zfill(6) + ': ' + data1_str +
                    ' ' + data2_str + "  |  " + data1_str_ascii + ' ' + data2_str_ascii + '\n')
    file_object_bin.write(binary_lines)

print(line_num)
file_object.close()
file_object_bin.close()