# --------------------------- #
# Intro to CS Final Project   #
# Gaming Social Network       #
# --------------------------- #

# Background ==========
# You and your friend have decided to start a company that hosts a gaming
# social network site. Your friend will handle the website creation (they know
# what they are doing, having taken our web development class). However, it is
# up to you to create a data structure that manages the game-network information
# and to define several procedures that operate on the network.
#
# In a website, the data is stored in a database. In our case, however, all the
# information comes in a big string of text. Each pair of sentences in the text
# is formatted as follows:
#
# <user> is connected to <user1>, ..., <userM>.<user> likes to play <game1>, ..., <gameN>.
#
# For example:
#
# John is connected to Bryant, Debra, Walter.John likes to play The Movie: The Game, The Legend of Corgi, Dinosaur Diner.
#
# Note that each sentence will be separated from the next by only a period. There will
# not be whitespace or new lines between sentences.
#
# Your friend records the information in that string based on user activity on
# the website and gives it to you to manage. You can think of every pair of
# sentences as defining a user's profile.
#
# Consider the data structures that we have used in class - lists, dictionaries,
# and combinations of the two (e.g. lists of dictionaries). Pick one that
# will allow you to manage the data above and implement the procedures below.
#
# You may assume that <user> is a unique identifier for a user. For example, there
# can be at most one 'John' in the network. Furthermore, connections are not
# symmetric - if 'Bob' is connected to 'Alice', it does not mean that 'Alice' is
# connected to 'Bob'.
#
# Project Description ====================
# Your task is to complete the procedures according to the specifications below
# as well as to implement a Make-Your-Own procedure (MYOP). You are encouraged
# to define any additional helper procedures that can assist you in accomplishing
# a task. You are encouraged to test your code by using print statements and the
# Test Run button.
# -----------------------------------------------------------------------------

# Example string input. Use it to test your code.
example_input="John is connected to Bryant, Debra, Walter.\
John likes to play The Movie: The Game, The Legend of Corgi, Dinosaur Diner.\
Bryant is connected to Olive, Ollie, Freda, Mercedes.\
Bryant likes to play City Comptroller: The Fiscal Dilemma, Super Mushroom Man.\
Mercedes is connected to Walter, Robin, Bryant.\
Mercedes likes to play The Legend of Corgi, Pirates in Java Island, Seahorse Adventures.\
Olive is connected to John, Ollie.\
Olive likes to play The Legend of Corgi, Starfleet Commander.\
Debra is connected to Walter, Levi, Jennie, Robin.\
Debra likes to play Seven Schemers, Pirates in Java Island, Dwarves and Swords.\
Walter is connected to John, Levi, Bryant.\
Walter likes to play Seahorse Adventures, Ninja Hamsters, Super Mushroom Man.\
Levi is connected to Ollie, John, Walter.\
Levi likes to play The Legend of Corgi, Seven Schemers, City Comptroller: The Fiscal Dilemma.\
Ollie is connected to Mercedes, Freda, Bryant.\
Ollie likes to play Call of Arms, Dwarves and Swords, The Movie: The Game.\
Jennie is connected to Levi, John, Freda, Robin.\
Jennie likes to play Super Mushroom Man, Dinosaur Diner, Call of Arms.\
Robin is connected to Ollie.\
Robin likes to play Call of Arms, Dwarves and Swords.\
Freda is connected to Olive, John, Debra.\
Freda likes to play Starfleet Commander, Ninja Hamsters, Seahorse Adventures.\
"

# -----------------------------------------------------------------------------
# create_data_structure(string_input):
#   Parses a block of text (such as the one above) and stores relevant
#   information into a data structure. You are free to choose and design any
#   data structure you would like to use to manage the information.
#
# Arguments:
#   string_input: block of text containing the network information
#
#   You may assume that for all the test cases we will use, you will be given the
#   connections and games liked for all users listed on the right-hand side of an
#   'is connected to' statement. For example, we will not use the string
#   "A is connected to B.A likes to play X, Y, Z.C is connected to A.C likes to play X."
#   as a test case for create_data_structure because the string does not
#   list B's connections or liked games.
#
#   The procedure should be able to handle an empty string (the string '') as input, in
#   which case it should return a network with no users.
#
# Return:
#   The newly created network data structure

#imports:
import re
import random

#dictionary_structure = {
#    'name1': { 'connections': ['Bryant', 'Debra', 'Walter'], 'games': [' The Movie: The Game', ' The Legend of Corgi', ' Dinosaur Diner'] },
#    'name2': { 'connections': [],'games': [] }...etc },

def grab_list(string_input,key,index):
    start_quote = string_input.find(key, index)
    #print start_quote,'start_quote'
    end_quote = string_input.find('.', start_quote + len(key))
    #print end_quote,'end_quote'
    url = string_input[start_quote + len(key)+1:end_quote]
    #print url,'url'
    return url.split(', ')

def grab_name(string_input,index):
    #phrase_index = string_input.find(key)-1   #edit
    #print phrase_index,'phrase_index'
    begin_name = string_input.rfind('.', 0, index-1) #searches for last known instance
    #print begin_name,'begin_name'
    name = string_input[begin_name+1:index-1]
    return name

def create_data_structure(string_input):
    DATA = {}
    #populate dict with names & connections initially
    connections = 'is connected to'
    connectionsListIndex = [m.start() for m in re.finditer(connections, string_input)]
    for i in connectionsListIndex:
        DATA[grab_name(string_input,i)] = {'connections':grab_list(string_input,connections,i) }
    games = 'likes to play' #populates 'games' key
    gamesListIndex = [m.start() for m in re.finditer(games, string_input)]
    for i in gamesListIndex:
        DATA[grab_name(string_input,i)]['games'] = grab_list(string_input,games,i)
    return DATA

# ----------------------------------------------------------------------------- #
# Note that the first argument to all procedures below is 'network' This is the #
# data structure that you created with your create_data_structure procedure,    #
# though it may be modified as you add new users or new connections. Each       #
# procedure below will then modify or extract information from 'network'        #
# ----------------------------------------------------------------------------- #

# -----------------------------------------------------------------------------
# get_connections(network, user):
#   Returns a list of all the connections that user has
#
# Arguments:
#   network: the gamer network data structure
#   user:    a string containing the name of the user
#
# Return:
#   A list of all connections the user has.
#   - If the user has no connections, return an empty list.
#   - If the user is not in network, return None.
def get_connections(network, user):
    if user in network:
        info = network.get(user)
        #print 'INFO',info
        connections = info.get('connections')
        #print 'connections:',connections
        if connections == [' '] or connections == []:      #still need to polish this
            return []
        else:
            #print 'connections:',connections,type(connections)
            return connections

# -----------------------------------------------------------------------------
# get_games_liked(network, user):
#   Returns a list of all the games a user likes
#
# Arguments:
#   network: the gamer network data structure
#   user:    a string containing the name of the user
#
# Return:
#   A list of all games the user likes.
#   - If the user likes no games, return an empty list.
#   - If the user is not in network, return None.
def get_games_liked(network,user):
    if user in network:
        info = network.get(user)
        games = info.get('games')
        if games == [' ']:      #polish this #NOTE
            return []
        else:
            return games

# -----------------------------------------------------------------------------
# add_connection(network, user_A, user_B):
#   Adds a connection from user_A to user_B. Make sure to check that both users
#   exist in network.
#
# Arguments:
#   network: the gamer network data structure
#   user_A:  a string with the name of the user the connection is from
#   user_B:  a string with the name of the user the connection is to
#
# Return:
#   The updated network with the new connection added.
#   - If a connection already exists from user_A to user_B, return network unchanged.
#   - If user_A or user_B is not in network, return False.
def add_connection(network, user_A, user_B):
    #print 'initial network:',network
    if user_A in network and user_B in network:
        A = get_connections(network, user_A)
        #print 'A:',A
        if user_B not in A:
            network[user_A]['connections'].append(user_B)
            #print 'adding connection:',network[user_A]['connections']
            return network
        else:
            return network
    else:
        return False

# -----------------------------------------------------------------------------
# add_new_user(network, user, games):
#   Creates a new user profile and adds that user to the network, along with
#   any game preferences specified in games. Assume that the user has no
#   connections to begin with.
#
# Arguments:
#   network: the gamer network data structure
#   user:    a string containing the name of the user to be added to the network
#   games:   a list of strings containing the user's favorite games, e.g.:
#		     ['Ninja Hamsters', 'Super Mushroom Man', 'Dinosaur Diner']
#
# Return:
#   The updated network with the new user and game preferences added. The new user
#   should have no connections.
#   - If the user already exists in network, return network *UNCHANGED* (do not change
#     the user's game preferences)
def add_new_user(network, user, games):
    if user not in network:
        network[user] = {'connections':[],'games':games}
    return network

# -----------------------------------------------------------------------------
# get_secondary_connections(network, user):
#   Finds all the secondary connections (i.e. connections of connections) of a
#   given user.
#
# Arguments:
#   network: the gamer network data structure
#   user:    a string containing the name of the user
#
# Return:
#   A list containing the secondary connections (connections of connections).
#   - If the user is not in the network, return None.
#   - If a user has no primary connections to begin with, return an empty list.

# Note:
#   It is OK if a user's list of secondary connections includes the user
#   himself/herself. It is also OK if the list contains a user's primary
#   connection that is a secondary connection as well.
def get_secondary_connections(network, user):
    if user not in network:
        return None
    if network[user]['connections'] == []:
        return []
    else:
        secondary = []
        primary = network[user]['connections']
        for i in primary:
            secondary.extend(network[i]['connections'])
        return list(set(secondary))

# -----------------------------------------------------------------------------
# count_common_connections(network, user_A, user_B):
#   Finds the number of people that user_A and user_B have in common.
#
# Arguments:
#   network: the gamer network data structure
#   user_A:  a string containing the name of user_A
#   user_B:  a string containing the name of user_B
#
# Return:
#   The number of connections in common (as an integer).
#   - If user_A or user_B is not in network, return False.
def count_common_connections(network, user_A, user_B):
    if user_A not in network:
        return False
    elif user_B not in network:
        return False
    else:
        A = get_connections(network,user_A)
        B = get_connections(network,user_B)
        #print A,'A',B,'B'
        return len([val for val in A if val in B])

def list_common_connections(network, user_A, user_B):
    A = get_connections(network,user_A)
    B = get_connections(network,user_B)
    #print A,'A',B,'B'
    return [val for val in A if val in B]
# -----------------------------------------------------------------------------
# find_path_to_friend(network, user_A, user_B):
#   Finds a connections path from user_A to user_B. It has to be an existing
#   path but it DOES NOT have to be the shortest path.
#
# Arguments:
#   network: The network you created with create_data_structure.
#   user_A:  String holding the starting username ("Abe")
#   user_B:  String holding the ending username ("Zed")
#
# Return:
#   A list showing the path from user_A to user_B.
#   - If such a path does not exist, return None.
#   - If user_A or user_B is not in network, return None.
#
# Sample output:
#   >>> print find_path_to_friend(network, "Abe", "Zed")
#   >>> ['Abe', 'Gel', 'Sam', 'Zed']
#   This implies that Abe is connected with Gel, who is connected with Sam,
#   who is connected with Zed.
#
# Note:
#   You must solve this problem using recursion!
#
# Hints:
# - Be careful how you handle connection loops, for example, A is connected to B.
#   B is connected to C. C is connected to B. Make sure your code terminates in
#   that case.
# - If you are comfortable with default parameters, you might consider using one
#   in this procedure to keep track of nodes already visited in your search. You
#   may safely add default parameters since all calls used in the grading script
#   will only include the arguments network, user_A, and user_B.

#traces random path to friend...not necessarily in the most efficient path
def trace_random_path_to_friend(network, user_A, user_B):
    path = [user_A]
    if user_A and user_B in network:
        if user_B in get_connections(network,path[-1]):
            path.append(user_B)
            return path
        else:
            connections = get_connections(network,path[-1])
            choice = random.choice(connections) #picks random connection
            path.append(choice)
            return path + trace_random_path_to_friend(network,path[-1],user_B)
    else:
        #print 'User(s) not in network, no path possible'
        return False

#removes adjacent duplicates from list
def dedupe_adjacent(alist):
    #print 'alist',alist, type(alist)
    if alist != False:
        for i in xrange(len(alist) - 1, 0, -1):
            if alist[i] == alist[i-1]:
                del alist[i]
        return alist
    else:
        return None

def find_path_to_friend(network,user_A,user_B):
    if user_A and user_B in network:
        #print 'user_A connections:',get_connections(network,user_A)
        if get_connections(network,user_A) != None:
            if get_connections(network,user_A)!= [] and get_connections(network,user_B)!= []:
                path = trace_random_path_to_friend(network,user_A,user_B)
                #print 'path', path
                #print 'shortened path:',dedupe_adjacent(path)
                return dedupe_adjacent(path)
        else:
            return None
    else:
        return None

# Make-Your-Own-Procedure (MYOP)
# -----------------------------------------------------------------------------
# Your MYOP should either perform some manipulation of your network data
# structure (like add_new_user) or it should perform some valuable analysis of
# your network (like path_to_friend). Don't forget to comment your MYOP. You
# may give this procedure any name you want.

def find_users_of_game(network,game):
    users = []
    for i in network:
        if game in network[i]['games']:
            users.append(i)
    return users

#evaluates numerous path options and chooses the shortest
def find_shortest_path_to_friend(network,user_A,user_B):
    shortest = find_path_to_friend(network,user_A,user_B)
    for i in range(50): # 50 iterations
        candidate = find_path_to_friend(network,user_A,user_B)
        if len(candidate) < len(shortest):
            shortest = candidate
    return shortest

#print find_shortest_path_to_friend(net, "John", "Ollie")
#print find_shortest_path_to_friend(net, "Debra", "Bryant")
#print find_shortest_path_to_friend(net, "Walter", "Jennie")
#net = create_data_structure(example_input)
#print get_connections(net, "Joyy")
#print get_connections(net, "Debra")
#print get_connections(net, "Mercedes")
#print get_games_liked(net, "John")
#add_connection(net, "Freda", "Bryant")
#add_connection(net, "Olive", "Freda")
#print add_connection(net, "Freda", "John")
#print add_connection(net, "John", "Bryant")
#print add_connection(net, "John", "Freda")
#print add_connection(net, "John", "Joyy")
#print add_new_user(net, "Debra", [])
#print add_new_user(net, "Nick", ["Seven Schemers", "The Movie: The Game"]) # True
#print 'secondary connections of Mercedes:', get_secondary_connections(net, "Mercedes")
#print count_common_connections(net, "Mercedes", "John")
#print find_users_of_game(net,'Dinosaur Diner')
#print find_users_of_game(net,'The Movie: The Game')
#print find_users_of_game(net,'The Legend of Corgi')
#print find_path_to_friend(net, "John", "Ollie")
#print find_path_to_friend(net, "Debra", "Bryant")
#print find_path_to_friend(net, "Walter", "Jennie")
#print net

#network = create_data_structure('')
#network = add_new_user(network, 'Alice', [])
#network = add_new_user(network, 'Bob', [])
#network = add_connection(network, 'Alice', 'Bob')
#network = add_connection(network, 'Alice', 'Bob')
#print get_connections(network, 'Alice')
#print add_connection(network, 'Alice', 'Bob')
#find_path_to_friend(network, 'Alice', 'Bob')
#find_path_to_friend(network, 'Carol', 'Alice')


#network = create_data_structure(example_input)
#print count_common_connections(network, 'John', 'Mercedes')
#print find_path_to_friend(network,"John","Mercedes")

#print 'network',network
