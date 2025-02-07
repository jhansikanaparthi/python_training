"""
From given string,
Extract
DATE

Expected Output:
----------
26/Apr/2000
----------
"""
print("input Data:")
print("-"*20)
# -------------

input_data = '123.123.123.123 - - [26/Apr/2000:00:23:48 -0400] "GET /pics/wpaper.gif HTTP/1.0" 200 6248 "http://www.jafsoft.com/asctortf/" "Mozilla/4.05 (Macintosh; I; PPC)"'
print(input_data)

print("#"*40, end="\n\n")
############################

"""
From given string,
Extract
DATE

Expected Output:
----------
26/Apr/2000
----------
"""
print("input Data:")
print("-"*20)
# -------------

input_data = '123.123.123.123 - - [26/Apr/2000:00:23:48 -0400] "GET /pics/wpaper.gif HTTP/1.0" 200 6248 "http://www.jafsoft.com/asctortf/" "Mozilla/4.05 (Macintosh; I; PPC)"'
print(input_data)

print("#"*40, end="\n\n")
############################

print("Extract DATE: 1-WAY")
print("-"*20)
# -------------

input_data = '123.123.123.123 - - [26/Apr/2000:00:23:48 -0400] "GET /pics/wpaper.gif HTTP/1.0" 200 6248 "http://www.jafsoft.com/asctortf/" "Mozilla/4.05 (Macintosh; I; PPC)"'

index_of_square_bracket = input_data.find("[")
start_index = index_of_square_bracket + 1

end_index = input_data.index(":")
# index() and find() both are same, but difference is if character not found
# then index() will throw error and find() will return -1

dt = input_data[start_index : end_index]
print(dt)

print("#"*40, end="\n\n")
############################

# Example-1
# >>> # About 'split()' method
# >>> # Feature-1
# >>> s = "WEL COME"
# >>> s.split() # split based on SPACE
# ['WEL', 'COME']
# >>>
# >>> # Feature-2
# >>> s = "WEL COME"
# >>> s.split("EL") # split based on EL
# ['W', ' COME']
# >>>
#

# Example-2
# >>> # About 'find()' method
# >>> # Feature-1
# >>> s = "WEL COME"
# >>> s.find("E") # returns index of 1st 'E'
# 1
# >>>
# >>> # Feature-2
# >>> s = "WEL COME"
# >>> s.find("E", 4) # Start from index-4 onwards
# 7
# >>>
# >>> # Feature-3
# >>> s = "WEL COME"
# >>> s.find("COME") # Returns index of 'C'
# 4
# >>> # Feature-4
# >>> s = "WEL COME"
# >>> s.find("XYZ") # Returns -1 if substring not found
# -1
# >>>