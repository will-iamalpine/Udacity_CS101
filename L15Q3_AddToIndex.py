# Define a procedure, add_to_index,
# that takes 3 inputs:

# - an index: [[<keyword>,[<url>,...]],...]
# - a keyword: String
# - a url: String

# If the keyword is already
# in the index, add the url
# to the list of urls associated
# with that keyword.

# If the keyword is not in the index,
# add an entry to the index: [keyword,[url]]

index = [ ['test1',['url1','url2']], ['test2',['url3','url4']] ]

def add_to_index(index,keyword,url):
#solution provided is more elegant:
#    for entry in index:
#        if entry[0] == keyword:
#            entry[1].append(url)
#            print keyword, 'found'
#            return
#    index.append( [keyword,[url]] )

    #create sublist containing indices
    indices = [x[0] for x in index]
    #search within indices for keyword
    if keyword in indices:
        position = indices.index(keyword)
        #print 'found',keyword,'@ index',position
        #append url if it's not there already
        if url not in index[position][1]:
            index[position][-1].append(url)
    else:
        index.extend( [ [keyword,[url]] ] )




add_to_index(index,'udacity','http://udacity.com')
add_to_index(index,'udacity','http://npr.org')
add_to_index(index,'test2','url.com')
add_to_index(index,'test2','test.com')
add_to_index(index,'computing','http://acm.org')

print index

#>>> [['test1', ['url1', 'url2']], ['test2', ['url3', 'url4', 'url.com']], ['udacity', ['http://udacity.com', 'http://npr.org']], ['computing', ['http://acm.org']]]
