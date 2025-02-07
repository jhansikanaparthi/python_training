"""
Get data from website
then
extract log data from website
"""

print("Get data from website and print")
print("-"*20)
# -------------
import urllib.request as u

my_web_file_handle = u.urlopen("https://www.jafsoft.com/searchengines/log_sample.html")
web_content = my_web_file_handle.read()
my_web_file_handle.close()

print(web_content)

print("#"*40, end="\n\n")
############################

print("Create beautifulsoup object with web_content")
print("-"*20)
# -------------

from bs4 import BeautifulSoup
soup = BeautifulSoup(web_content, 'html.parser')
print(soup)

print("#"*40, end="\n\n")
############################

print("Getting log data:")
print("-"*20)
# -------------

log_data = soup.body.pre.text
print("log_data:", log_data)

print("#"*40, end="\n\n")
############################

print("log data in raw format:")
print("-"*20)
# -------------

print("log_data in raw format:", repr(log_data))

print("#"*40, end="\n\n")
############################