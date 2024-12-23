import sys
# Open the binary file
sc = sys.argv[1]

with open(sc, "rb") as f:
    binary_data = f.read()

# Convert to hex format
hex_array = ", ".join(f"0x{byte:02x}" for byte in binary_data)

# Output the C++ compatible array
cpp_array = f"unsigned char shellcode[] = {{ {hex_array} }};"

# Save to a file or print
with open("shellcode_array.bin", "w") as out_file:
    out_file.write(cpp_array)

print("Conversion complete. C++ shellcode array saved to 'shellcode_array.bin'.")
