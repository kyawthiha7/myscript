# Replace the placeholder with your actual shellcode
shellcode = [
    # your_shellcode, for example:
    
   # Add the rest of your shellcode bytes here
]

# Calculate the size of the shellcode
shellcode_size = len(shellcode)
print(f"The shellcode size is: {shellcode_size} bytes\n")

# Format and print the shellcode with 15 bytes per line
print("Formatted shellcode:")
for i in range(0, len(shellcode), 15):
    chunk = shellcode[i:i+15]
    formatted_line = ", ".join(f"0x{byte:02x}" for byte in chunk)
    if i + 15 < len(shellcode):
        print(f"{formatted_line},")
    else:
        print(formatted_line)
