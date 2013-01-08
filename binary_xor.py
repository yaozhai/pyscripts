import os
import string

target_file_path = 'c:\\Projects\\Chrysler\\Documents\\DSeg\\Lockup_Bootloader'
file_object_1 = open(os.path.join(target_file_path, 'NOR_dump.tst'), mode='r', buffering=1)
file_object_2 = open(os.path.join(target_file_path, 'KL14GP.SW.IC.V51.91.03_NOR_Complete_FF.tst'), mode='r', buffering=1)
file_object_xor = open(os.path.join(target_file_path, 'XOR.tst'), mode='w', buffering=1)

XOR_Newline = []
line1_list = []
line2_list = []

counter = 0
line_count = 0

while True:
    line1_list = file_object_1.readline().split()
    line2_list = file_object_2.readline().split()
    if line1_list == [] or line2_list == []:
        break

    XOR_Newline = line1_list[0] + ' '
    result = ''

    for i in range(1, 5):
        result += bin(int(line1_list[i], 2) ^ int(line2_list[i], 2))[2:].zfill(8)
        result += ' '

    XOR_Newline = XOR_Newline + result + '\n'
    file_object_xor.write(XOR_Newline)
    counter = counter + 1

print(counter)
file_object_1.close()
file_object_2.close()
file_object_xor.close()