'''
Our class Song, 
which represents a Song on a streaming platform
'''
class Song:
    # constructor
    # anyb time we are providing a method
    # that python has a special use for 
    # we denote it with two underscores (__)
    # at front and end
    # specifies what happens when we create a new Song
    # self always has to be first param of all class methods
    def __init__(self, title, artist):
        self.title = title
        self.artist = artist
        self.n_streams = 0 

    # the __str__ method defines what should be printed
    # when a developer prints out your object
    def __str__(self):
        # return a string object 
        # python will automatically print that for us
        return f"{self.title} by {self.artist} \nStreams: {self.n_streams}"

    # this is a method unique to our Song objects,
    # not an expected python method
    # so we do not need the double underscores
    def play(self):
        print("Now Playing: " + self.title)
        self.n_streams += 1 # increment streams by 1
    

#####################################
# outside of our class definition
# #####################################
# a_list = [] # creates a list object
# a_list.append(4) # using the list method append
# single_ladies = Song("Single Ladies", "Beyonce") # creates a Song object
# print(single_ladies)
# sorry = Song("Sorry", "Justin Bieber")
# print(sorry)
# print(type(single_ladies))
# sorry.play() # using the Song method play (just like append)
# print(sorry)