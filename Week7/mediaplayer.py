
class Song:
    def __init__(self,title,artist):
        self.title = title
        self.artist = artist

    def getTitle(self):
        return self.title

    def getArtist(self):
        return self.artist
        
    def __str__(self):
        return self.title + " by " + self.artist 

    def __eq__(self, other):
        return ((self.title, self.artist) == (other.title, other.artist))
        
    def __ne__(self, other):
        return not (self == other)

    def __lt__(self, other):
        return ((self.title, self.artist) < (other.title, other.artist))
        
    def __gt__(self, other):
        return ((self.title, self.artist) < (other.title, other.artist))

class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, e):
        return self.queue.append(e)

    def dequeue(self):
        if len(self.queue) < 1:
            return None
        return self.queue.pop(0)

    def removeSong(self, e):
        for i in range(len(self.queue)):
            if e == self.queue[i]['Title']:
                self.queue.pop(i)
                return
    
    def prevSong(self):
        prev = len(self.queue)-1
        self.queue.insert(0, self.queue[prev])
        self.queue.pop(prev+1)
        return

    def size(self):
        return len(self.queue)

    def peek(self):
        return f"Title: {self.queue[0]['Title']}, Artist: {self.queue[0]['Artist']}"

    def showQueue(self):
        return self.queue

    def shuffleQueue(self):
        size = len(self.queue)
        a = self.queue.pop(size//2)
        tempList = []
        for i in self.queue:
            tempList.append(a)
        self.queue = tempList
        return

def menu():
    print()
    print(20 * "-" , "MENU" , 20 * "-")
    print("1. Add Song to Playlist")
    print("2. Remove song from Playlist")
    print("3. Play")
    print("4. Skip")
    print("5. Go Back")
    print("6. Shuffle")
    print("7. Show Currently Playing Song")
    print("8. Show Current Playlist Order")
    print("0. Exit")
    print(47 * "-")

playlist = Queue()
startList = [
    {"Title": "I am a God","Artist": "Kanye West"},
    {"Title": "Coldest Winter","Artist":  "Kanye West"},
    {"Title": "Runaway","Artist":  "Kanye West"},
    {"Title": "Black Skinhead","Artist":  "Kanye West"},
    {"Title": "Addiction","Artist":  "Kanye West"},
    {"Title": "Hold My Liquor","Artist":  "Kanye West"}]
for i in range(len(startList)):
        string = {"Title": startList[i]["Title"], "Artist": startList[i]["Artist"]}
        playlist.enqueue(string)    
while True:
    menu()
    choice = int(input())
    if choice == 1:
        # Add code to prompt user for Song Title and Artist Name
        # Add song to playlist
        title = input("Song Title: ")
        artist = input("Artist Name: ")
        inst = Song(title, artist)
        string = {"Title": inst.getTitle(), "Artist": inst.getArtist()}
        playlist.enqueue(string)
        print("New Song Added to Playlist")
    elif choice == 2:
        # Prompt user for Song Title 
        # remove song from playlist
        title = input("What song do you want to remove? ")
        playlist.removeSong(title)
        print("Song Removed to Playlist")
    elif choice == 3:
        # Play the playlist from the beginning
        # Display song name that is currently playing
        print("Playing....", end=playlist.peek())        
    elif choice == 4:
        # Skip to the next song on the playlist
        # Display song name that is now playing
        e = playlist.dequeue()
        playlist.enqueue(e)
        print("Skipping.... Playing Now -> ", end=playlist.peek())                     
    elif choice == 5:
        # Go back to the previous song on the playlist
        # Display song name that is now playing
        playlist.prevSong()
        print("Replaying.... Playing Now -> ", end=playlist.peek())  
    elif choice == 6:
        # Randomly shuffle the playlist and play the first song
        # Display song name that is now playing
        playlist.shuffleQueue()
        print("Shuffling.... Playing Now -> ", end=playlist.peek())          
    elif choice == 7:
        # Display the song name and artist of the currently playing song
        print("Currently playing: ", end=playlist.peek())    
    elif choice == 8:
        # Show the current song list order
        print("\nSong list:\n", playlist.showQueue())
    elif choice == 0:
        print("Goodbye.")
        break

            
# 10 songs
# 1."‘I am a God’", "Kanye West"
# 2."‘Coldest Winter’", "Kanye West"
# 3."‘Runaway’", "Kanye West"
# 4."‘Black Skinhead’", "Kanye West"
# 5."‘Addiction’", "Kanye West"
# 6."‘Hold My Liquor’", "Kanye West"
# 7."‘On Sight’", "Kanye West"
# 8."‘Monster’", "Kanye West"
# 9."‘Gold Digger’", "Kanye West"
# 10."‘All of the Lights’", "Kanye West"