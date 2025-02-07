"""
Get data from web_server.log file

then

Extract
IP
DATE
URL

then

write extracted data to log_report_3.txt

Expected content in log_report_3.txt:
----------
    IP                  DATE            URL
123.123.123.123     26/Apr/2000     http://www.jafsoft.com/asctortf/
123.123.123.123     26/Apr/2000     http://www.jafsoft.com/asctortf/
123.123.123.123     26/Apr/2000     http://www.jafsoft.com/asctortf/
123.123.123.123     26/Apr/2000     http://www.jafsoft.com/asctortf/
123.123.123.123     26/Apr/2000     http://www.jafsoft.com/asctortf/
123.123.123.123     26/Apr/2000     http://www.jafsoft.com/asctortf/
----------
"""
print("Get data from web_server.log file")
print("-"*20)
# -------------

# We can provide absolute path
# my_log_file_handle = open(r"C:\python_training\log\web_server.log", "r")
# OR
# We can provide relative path
my_log_file_handle = open(r"C:\python_training\log\web_server.log", "r")
log_file_content = my_log_file_handle.readlines()
my_log_file_handle.close()

print(log_file_content)

print("#"*40, end="\n\n")
############################

print("print each value in log_file_content")
print("-"*20)
# -------------

for i in log_file_content:
    print("Each Value:", i)

print("#"*40, end="\n\n")
############################

print("print only IP address lines")
print("-"*20)
# -------------

for i in log_file_content:
    if i.startswith("123"):
        print("Each Line:", i)

print("#"*40, end="\n\n")
############################

print("print only IP address lines")
print("-"*20)
# -------------

for i in log_file_content:
    if i.startswith("123"):
        sp = i.split()
        # print("sp:", sp)
        ip =sp[0]

        raw_date = sp[3] # '[26/Apr/2000:00:23:48'
        dt = raw_date[1:raw_date.index(":")]

        raw_url = sp[10] # '"http://www.jafsoft.com/asctortf/"'
        url = raw_url[1:-1]

        print(ip, dt, url)


print("#"*40, end="\n\n")
############################
print("Write to log_report_3.txt")
print("-"*20)
# -------------

my_out_file_handle = open("log_report_3.txt", "w")
print("IP", "DATE", "URL", sep="\t", file=my_out_file_handle)

for i in log_file_content:
    if i.startswith("123"):
        sp = i.split()
        # print("sp:", sp)
        ip =sp[0]

        raw_date = sp[3] # '[26/Apr/2000:00:23:48'
        dt = raw_date[1:raw_date.index(":")]

        raw_url = sp[10] # '"http://www.jafsoft.com/asctortf/"'
        url = raw_url[1:-1]

        print(ip, dt, url, sep="\t", file=my_out_file_handle)

my_out_file_handle.close()

print("""
Created 'log_report_3.txt', please check
""")

print("#"*40, end="\n\n")
############################
print("Write to log_report_3.txt")
print("-"*20)
# -------------

my_out_file_handle = open("log_report_3.txt", "w")
print("IP", "DATE", "URL", sep="\t", file=my_out_file_handle)

for i in log_file_content:
    if i.startswith("123"):
        sp = i.split()
        # print("sp:", sp)
        ip =sp[0]

        raw_date = sp[3] # '[26/Apr/2000:00:23:48'
        dt = raw_date[1:raw_date.index(":")]

        raw_url = sp[10] # '"http://www.jafsoft.com/asctortf/"'
        url = raw_url[1:-1]

        print(ip, dt, url, sep="\t", file=my_out_file_handle)

my_out_file_handle.close()

print("""
Created 'log_report_3.txt', please check
""")

print("#"*40, end="\n\n")
############################