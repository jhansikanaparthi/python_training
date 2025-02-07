"""
Write LogProcessClass with following methods:

1. add method 'get_all_ips' to get all ips
2. add method 'get_all_records' to get all records
3. add method 'write_to_txt_file' to write to text file
4. add method 'write_to_json_file' to write to json file

Expected Output:
Example:

l1 = LogProcessClass(r"web_server.log")

ips_list = l1.get_all_ips()
print("ips_list:", ips_list) # [ip1, ip2, ip3 ..]

all_records_list = l1.get_all_records()
print("all_records_list:", all_records_list)  # [(ip,dt,url),(ip,dt,url),(ip,dt,url),]

l1.write_to_txt_file('my_report.txt')

l2.write_to_json_file('my_report.json')

"""