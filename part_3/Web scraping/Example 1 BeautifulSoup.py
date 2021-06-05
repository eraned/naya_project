from bs4 import BeautifulSoup as bs
import re

with open('html_example.html') as f:
    html_page = f.read()

soup = bs(html_page, 'html.parser')
# Print html text prettify
print(soup.prettify()[:200])

# Print soup with li class
print(soup.li)

# Print soup with a class
print(soup.a)

# Print on attr
link = soup.a
print(link.attrs)

# Print the 'href'
print(link['href'])

# find all 'a' class
links = soup.find_all('a')
print(links)

# Filter by attribute value:
links = soup.find_all('a', class_="news")
for link in links:
    print(f"{link['id']}: {link.string} - {link.get('href')} ")


# This code finds all the tags whose names start with the letter “b” but not followed by the letter "r"
for tag in soup.find_all(re.compile("^b[^r]+")):
    print(tag.name)

# Find by string
print(soup.find_all(string='item 4'))

# As with tag names, we can pass a regular expression object:
print(soup.find_all(string=re.compile(".* goal .*")))

# limit 5
print(soup.find_all('a', limit=5))

# if you need only single (the first) result or you know there is only signle item of what you are looking for,
# you can use find() (instead of passing limit=1 to find_all)

print(soup.find('a', class_='sport'))

# do we want Beautiful Soup to search the all tree (children, its children’s children, and so on) , or just for direct children?
print(soup.body.find_all(class_='list', recursive=False))