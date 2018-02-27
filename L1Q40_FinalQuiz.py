# Write Python code that assigns to the
# variable url a string that is the value
# of the first URL that appears in a link
# tag in the string page.
# Your code should print http://udacity.com
# Make sure that if page were changed to

# page = '<a href="http://udacity.com">Hello world</a>'

# that your code still assigns the same value to the variable 'url',
# and therefore still prints the same thing.

# page = contents of a web page
page =('<div id="top_bin"><div id="top_content" class="width960">'
'<div class="udacity float-left"><a href="http://udacity.com">')
start_link = page.find('<a href=')
begin_link = page.find('"',start_link)
end_link = page.find('"',begin_link+1)

url = page[begin_link+1:end_link]
print url

'''
print start_link
print begin_link
print end_link
print page[start_link:]
print page[begin_link+1:end_link]
#print page[end_link]
#print page[begin_link+1:end_link-1]
'''
