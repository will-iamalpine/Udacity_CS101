# Modify the get_next_target procedure so that
# if there is a link it behaves as before, but
# if there is no link tag in the input string,
# it returns None, 0.

# Note that None is not a string and so should
# not be enclosed in quotes.

# Also note that your answer will appear in
# parentheses if you print it.

page = '''<div id="top_bin"> <div id="top_content" class="width960">
   <div class="udacity float-left"> <a href="testymctesterson">'''

def get_next_target(page):
    start_link = page.find('<a href=')
    if start_link != -1:
    #Insert your code below here
        start_quote = page.find('"', start_link)
        end_quote = page.find('"', start_quote + 1)
        url = page[start_quote + 1:end_quote]
        return url, end_quote

    else:
        return (None, 0)

print(get_next_target(page))

#provided solution
'''
def get_next_target(page):
    start_link = page.find('<a href=')

    # if the link tag sequence is not found, find returns a -1
    if start_link == -1:
        # return the error codes of None, 0 now and skip the rest!
        return None, 0

    start_quote = page.find('"', start_link)
    end_quote = page.find('"', start_quote + 1)
    url = page[start_quote + 1:end_quote]
    return url, end_quote'''
