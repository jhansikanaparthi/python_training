"""
Read/Write from text file with any extensions like .txt, .log etc
"""

"""
We need to follow 3 steps
Step-1: Connect to file
Step-2: Read/Write
Step-3: Disconnect
"""

"""
We have functions for all 3 steps
Step-1: Connect to file
    - open() function
Step-2: Read/Write
    - FOR WRITING: 1) write 2) writelines 3) print-function
    - FOR READING: 1) read 2) readlines 3) readline
Step-3: Disconnect
"""
print("All writing operations")
print("-"*20)
# -------------

# Step-1: Connect to file
# -------------
# my_out_file_handle = open("provide file name or file path here", "provide mode")
my_out_file_handle = open("my_out_file.txt", "w")
# mode 'w': Write only, It will create new file, IMPORTANT - existing file content will be erased
# mode 'r': Read only, It will not create new file
# mode 'a': Append only, It will create new file if file not present

# Step-2: Write
# -------------

# Our Data
x = 10
y = "python"

# 1) write(): We can pass one string to this method
my_out_file_handle.write(str(x)+"\n")
my_out_file_handle.write(y+"\n")

# 2) writelines: We can pass collection of values like list/tuple etc
our_data_in_list = [str(x)+"\n", y+"\n"]
my_out_file_handle.writelines(our_data_in_list)

# 3) print-function
print(x, y, 20, "Java", sep="\n" ,file=my_out_file_handle)
# No need to convert 20 to string

# Step-3: Disconnect
# -------------
my_out_file_handle.close()

print("""
Created my_out_file.txt, please check
""")

print("#"*40, end="\n\n")
############################

print("Reading from file using 1) read()")
print("-"*20)
# -------------

# Step-1: Connect to file
# -------------
my_out_file_handle = open("my_out_file.txt", "r")

# Step-2: Read
# -------------
file_content = my_out_file_handle.read()
# Returns entire file content in ONE string
print("file_content:", file_content, end="\n\n")
print("file_content in RAW FORMAT:", repr(file_content), end="\n\n")


# Step-3: Disconnect
# -------------
my_out_file_handle.close()

print("#"*40, end="\n\n")
############################


print("Reading from file using 2) readlines()")
print("-"*20)
# -------------

# Step-1: Connect to file
# -------------
my_out_file_handle = open("my_out_file.txt", "r")

# Step-2: Read
# -------------
file_content = my_out_file_handle.readlines()
# Returns entire file content in LIST
print("file_content:", file_content, end="\n\n")

# Step-3: Disconnect
# -------------
my_out_file_handle.close()

print("#"*40, end="\n\n")
############################


print("Reading from file using 3) readline()")
print("-"*20)
# -------------

# Step-1: Connect to file
# -------------
my_out_file_handle = open("my_out_file.txt", "r")

# Step-2: Read
# -------------
file_content = my_out_file_handle.readline()
# Read one line
print("file_content:", file_content, end="\n\n")

# Step-3: Disconnect
# -------------
my_out_file_handle.close()

print("#"*40, end="\n\n")
############################

print("Reading from file using 4) read line by line using for-loop")
print("-"*20)
# -------------

# Step-1: Connect to file
# -------------
my_out_file_handle = open("my_out_file.txt", "r")

# Step-2: Read
# -------------
for i in my_out_file_handle:
    print("Each Line:", i)

# Step-3: Disconnect
# -------------
my_out_file_handle.close()

print("#"*40, end="\n\n")
############################