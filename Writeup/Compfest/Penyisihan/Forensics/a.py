with open('cat.png','rb') as f:
   data = f.read()
   new_buffer = []
   for i in range(len(data),4):
      slices = data[i:i+4]

      # Convert the binary_value to hexadecimal string
      hex_value = ''.join(format(byte, '02x') for byte in slices)
      hex_bytes = bytes.fromhex(hex_value)
      new_buffer.append(hex_bytes)
   print(new_buffer)

#       binary_value = b'\x01\x10\x00\x10'
# hex_value = '01100010'  # Your hexadecimal value as a string

# # Convert the hexadecimal string to bytes
# hex_bytes = bytes.fromhex(hex_value)

# # Append the hex_bytes to the existing buffer
# result_buffer = binary_value + hex_bytes