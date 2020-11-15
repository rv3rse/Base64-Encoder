import base64

option = input("\nSelect an option: \n\n .Encode \n\n .Decode \n\nChoice: ")

if option in ('Encode' , 'encode'):
	
	message = input("\nType your message or data: ")
	message_bytes = message.encode('ascii')
	base64_bytes = base64.b64encode(message_bytes)
	base64_message = base64_bytes.decode('ascii')
	print("\nEncoded message: " + base64_message)

elif option in ('Decode' , 'decode'):
	
	encoded = input("\nEnter your encoded message or data: ")
	base64_encoded = encoded.encode('ascii')
	decoded_bytes = base64.b64decode(base64_encoded)
	standard_message = decoded_bytes.decode('ascii')
	print("\nDecoded message: " + standard_message)



else:
	print("That is not an option.")