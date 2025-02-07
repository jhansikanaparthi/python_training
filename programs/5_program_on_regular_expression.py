"""
Get data from web_server.log

then

extract using regular expression
IP
DATE
URL
"""

print("Get data from web_server.log")
print("-"*20)
# -------------

my_log_file_handle = open(r"C:\python_training\log\web_server.log", "r")
log_file_content = my_log_file_handle.readlines()
my_log_file_handle.close()

print(log_file_content)

print("#"*40, end="\n\n")
############################
print("Check whether it is IP address line or not: Yes/No?")
print("-"*20)
# -------------

import re
for each_line in log_file_content:
    # match_result = re.match('\d\d\d\.\d{3}\.\d{1,3}\.[0-9][0-9][0-9]', each_line)
    # OR
    match_result = re.match(r'\d\d\d\.\d{3}\.\d{1,3}\.[0-9]{3}.*', each_line)
    print("Each Line:", each_line)
    print("match_result:", match_result, end="\n\n")

# COMMENT-1
r"""
IDENTIFIERS
----------
\d -> represents any one digit b/n 0 to 9
\D -> represents any one non-digit. Except 0 to 9
. -> represents, any ONE any characters OR some character
\. -> strictly DOT
[0-9] -> represents any one digit b/n 0 to 9
----------

QUNTIFIERS
----------
\d{3} -> internally it will be \d\d\d
\d{1,3} -> iinimum 1, maximum 2 charactes
---------- 

Modifiers
----------
* -> it makes 0 or more times
+ -> it makes 1 or more times
? -> it makes 1 or zero times
---------- 
"""

print("#"*40, end="\n\n")
############################
# Example:
# ---------------
# '\d\d\d\.\d{3}\.\d{1,3}\.[0-9]{3}.*'
#   IP address followed by 'any character' 0 or more times
#
# '\d\d\d\.\d{3}\.\d{1,3}\.[0-9]{3}abc*'
#   IP address followed by 'a' then 'b' then 0 or more times 'c' will come
#
# '\d\d\d\.\d{3}\.\d{1,3}\.[0-9]{3}(abc)*'
#   IP address followed by exact 'abc' 0 or more times
#
# '\d\d\d\.\d{3}\.\d{1,3}\.[0-9]{3}(abc)'
#   IP address followed by exact 'abc' 1 time
#
# '\d\d\d\.\d{3}\.\d{1,3}\.[0-9]{3}abc'
#   IP address followed by exact 'abc' 1 time
#
# '\d\d\d\.\d{3}\.\d{1,3}\.[0-9]{3}[abc]'
#   IP address followed by either a or b or c, any character in this group will come
#
# '\d\d\d\.\d{3}\.\d{1,3}\.[0-9]{3}[abc]*'
#   IP address followed by either a or b or c, 0 or more times
#
############################

print("Extract IP")
print("-"*20)
# -------------

import re
for each_line in log_file_content:
    match_result = re.match(r'(\d\d\d\.\d{3}\.\d{1,3}\.[0-9]{3}).*', each_line)
    if match_result is not None:
        ip = match_result.group(1)
        print(ip)


# COMMENT
"""
put () to IP address pattern to capture
- This is called grouping
- each group has index number starting with 1
"""

print("#"*40, end="\n\n")
############################
print("Extract IP, DATE")
print("-"*20)
# -------------

import re
for each_line in log_file_content:
    # match_result = re.match(r'(\d\d\d\.\d{3}\.\d{1,3}\.[0-9]{3}).*- \[(\d{2}/[A-Za-z]{3}/\d{4}).*', each_line)
    # OR
    match_result = re.match(r'(\d\d\d\.\d{3}\.\d{1,3}\.[0-9]{3}).*(\d{2}/[A-Za-z]{3}/\d{4}).*', each_line)
    if match_result is not None:
        ip = match_result.group(1)
        dt = match_result.group(2)
        print(ip, dt)


# COMMENT
"""
26/Apr/2000

26
---
\d\d # Strictly 2 digits
\d{2} # Strictly 2 digits
[0-9][0-9] # Strictly 2 digits
[0-9]{2} # Strictly 2 digits
\d[0-9] # Strictly 2 digits
[0-9]\d # Strictly 2 digits

\d{1,2} # minimum 1 and maximum 2
\d?\d # minimum 1 and maximum 2
[0-9]{1,2} # minimum 1 and maximum 2
[0-9]?[0-9] # minimum 1 and maximum 2
[0-9]?\d # minimum 1 and maximum 2
\d?[0-9] # minimum 1 and maximum 2
---

Apr
---
[A-Z][a-z][a-z]
# OR
[A-Z][a-z]{2}
# OR
[A-Za-z]{3}
# OR
(Jan|Feb|Mar)
---

"""

print("#"*40, end="\n\n")
############################
print("Extract IP, DATE, URL")
print("-"*20)
# -------------

import re
for each_line in log_file_content:
    match_result = re.match(r'(\d\d\d\.\d{3}\.\d{1,3}\.[0-9]{3}).*(\d{2}/[A-Za-z]{3}/\d{4}).*(http[s]?://[a-z./A-Z_]+).*', each_line)
    if match_result is not None:
        ip = match_result.group(1)
        dt = match_result.group(2)
        url = match_result.group(3)
        print(ip, dt, url)


# COMMENT
r"""

http://search.netscape.com/Computers/Data_Formats/Document/Text/RTF

Example-1
-----
http
OR
[a-z]{4}
-----

Example-2
-----
https? -> s is optional
http[s]? -> s is optional
(https)? -> complete 'https' is optional
[https]?  -> any one character, 
            which means 
            it can be 'h'
            OR  
            it can be 't'
            OR
            it can be 'p'
            OR          
            it can be 's'
            
            THAT TOO, which is optional

[httttttttttttttttttttps] -> it can 'h' or 't' or 'p' or 's'            
(httttttttttttttttttttps) -> exact word it will match
-----

Example-3
-----
http://search.netscape.com/Computers/Data_Formats/Document/Text/RTF

Final pattern
http[s]?://[a-z./A-Z_]+

Meaning
[a-z./A-Z_] these characters, one or more time it will come
-----

"""

print("#"*40, end="\n\n")
############################