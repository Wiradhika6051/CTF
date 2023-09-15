import os
import base64
# Function to rename multiple files
#credit: https://www.tutorialspoint.com/rename-multiple-files-using-python
# with modification
buffer = ['' for _ in range(50)]
def main():
	path="./dump/"
	for filename in os.listdir(path):
		my_dest = base64.b64decode(filename).decode()
		if('FAKEFLAG' in my_dest):
			continue
		print(my_dest)
		with open(path + filename) as f:
			buffer[int(my_dest)] = f.read()[0]
	print(''.join(buffer))


# Driver Code
if __name__ == '__main__':
	# Calling main() function
	main()