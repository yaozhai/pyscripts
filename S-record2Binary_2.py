import os
import string
import sys

#----------------------------------------------------------------------
def main():
    """"""
    # This part will be changed to command parameters.
    target_file_path = os.getcwd()
    file_name_scr = str(sys.argv[1])
    file_name_dest = str(sys.argv[2])
    file_object = open(os.path.join(target_file_path, file_name_scr), mode='r', buffering=1)
    file_object_bin = open(os.path.join(target_file_path, file_name_dest), mode='w', buffering=1)
    
    count = 0
    binary_lines = ''
    base_address = "F0000000"
    address_length = 8
    header_length = 4
    
    #8 half-byte
    BytePerLine = 4
    ByteCounter = 0
    
    for line in file_object:
        if count >= 10000:
            break
    
        line = line.rstrip('\r\n')
        Lineheader = line[0:4]
        LineFormat = line[0:2]
        if LineFormat != "S3" or line == "":
            continue
    
        length = len(line)
        data_length = length - 12 - 2
        #line_byte_cnt = int(data_length/2)
        #for i in range(data_length):
        i = 0
        while i < data_length:
            if ByteCounter < (BytePerLine*2):
                if ByteCounter % 2 == 0:
                    binary_lines += ' '
                binary_lines = binary_lines + bin(int(line[12+i],16))[2:].zfill(4)
    
                i = i+1
                ByteCounter = ByteCounter + 1
            else:
                address_prefix = base_address.upper() + ': '
                newline = address_prefix + binary_lines + '\n'
                file_object_bin.write(newline)
                count = count + 1
                ByteCounter = 0
                binary_lines = ''
                base_address = hex(int(base_address, 16) + BytePerLine)[2:]
                if count >= 10000:
                    break
                if count % 1000 == 0:
                    print("*")                
    
    print(count)
    file_object.close()
    file_object_bin.close()    
    
main()