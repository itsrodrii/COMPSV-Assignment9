class Person:
    '''
    A class representing a person in a social network.
    Attributes:
        name (str): The name of the person.
        friends (list): A list of friends (Person objects).
    Methods:
        add_friend(friend): Adds a friend to the person's friend list.
    '''
    def __init__(self, name):
        self.name = name
        self.friends = []

    def add_friend(self, friend):
        if friend not in self.friends:
            self.friends.append(friend)


class SocialNetwork:
    '''
    A class representing a social network.
    Attributes:
        people (dict): A dictionary mapping names to Person objects.
    Methods:
        add_person(name): Adds a new person to the network.
        add_friendship(person1_name, person2_name): Creates a friendship between two people.
        print_network(): Prints the names of all people and their friends.
    '''
    def __init__(self):
        self.people = {}

    def add_person(self, name):
        if name in self.people:
            print(f"{name} already exists in the network!")
        else:
            self.people[name] = Person(name)

    def add_friendship(self, person1_name, person2_name):
        if person1_name not in self.people or person2_name not in self.people:
            missing = person1_name if person1_name not in self.people else person2_name
            print(f"Friendship not created. {missing} doesn't exist!")
            return
        
        person1 = self.people[person1_name]
        person2 = self.people[person2_name]
        
        person1.add_friend(person2)
        person2.add_friend(person1)

    def print_network(self):
        for person in self.people.values():
            friends_names = [friend.name for friend in person.friends]
            print(f"{person.name} is friends with: {', '.join(friends_names)}")


# Test your code here
if __name__ == "__main__":
    network = SocialNetwork()

    # Adding people
    network.add_person("Alex")
    network.add_person("Jordan")
    network.add_person("Morgan")
    network.add_person("Taylor")
    network.add_person("Casey")
    network.add_person("Riley")

    # Creating friendships
    network.add_friendship("Alex", "Jordan")
    network.add_friendship("Alex", "Morgan")
    network.add_friendship("Jordan", "Taylor")
    network.add_friendship("Jordan", "Johnny")  # Should print an error
    network.add_friendship("Morgan", "Casey")
    network.add_friendship("Taylor", "Riley")
    network.add_friendship("Casey", "Riley")
    network.add_friendship("Morgan", "Riley")
    network.add_friendship("Alex", "Taylor")

    network.print_network()

'''
Design Memo:

A graph is better for a social network because it can show connections between people in both directions. 
Each person is a node and each friendship is an edge. Lists or trees arenot as good because lists are 
just a straight line of items, so it's hard to see who is friends with who. Trees have a hierarchy 
with parent and child, which doesn't match how friendships work since friendships are mutual for the most part.

Using a graph with an adjacency list lets each person keep a list of their friends, which makes it 
easy to add new friends and see who they are connected to. When you add a friendship, it just adds 
each person to the other's friends list. Printing the network shows everyone and their friends in a 
simple way.

One thing to notice is that adding friends takes a little checking to make sure both people exist 
and that the friendship isn't duplicated. Printing the network takes longer if there are lots of 
people and friendships, but it's fine for a small network. Overall, graphs are good for this because 
they match real social connections, let you quickly find friends, and handle changes easily.
'''

