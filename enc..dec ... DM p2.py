message = "STOP GLOBAL WARMING"
#message = "HELLO WORLD"
#message = "DON'T FINISH THE WORK"

key = "secret_key"

# Convert message&key to bytes
message_bytes = message.encode('utf-8')
key_bytes = key.encode('utf-8')

print(message_bytes)
print(key_bytes)

# Encrypt the message
print("Encryption:")

encrypted_message = bytearray()
for i in range(len(message_bytes)):
    encrypted_message.append(message_bytes[i] ^ key_bytes[i % len(key_bytes)])

# Print the encrypted message
print(encrypted_message)

#print("#"*20)
#encrypted_string = encrypted_message.decode('utf-8')
#print(encrypted_string)

###########################
print("-"*20)
print("Decryption:")
# Decrypt the message
decrypted_message = ""
for i in range(len(encrypted_message)):
    decrypted_message += chr(encrypted_message[i] ^ key_bytes[i % len(key_bytes)])

# Print the decrypted message
print(decrypted_message)
