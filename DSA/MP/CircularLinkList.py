# ERIC MANUEL MANZANERO
# BSCPE 2A
# DOUBLY LINK LIST
# PROBLEM: 
#     CREATE A PROGRAM THAT CAN CREATE A NEW PLAYLIST. THE PLAYLIST SHOULD HAVE THE FOLLOWING OPTIONS ADD SONGS, DELETE SONGS, AND PRINT THE PLAYLIST.

# CLASS THAT CREATES NODE OBJECT
class Song:
    def __init__(self, songName, nextSong = None):
        self.songName = songName
        self.nextSong = nextSong
        
#CLASS THAT CREATE THE WHOLE LINK LIST
class PlayList:
    def __init__(self, head = None, tail = None):
        self.head = head
        
    #FUNCTION FOR ADDING SONG INTO THE  PLAYLIST       
    def addSong(self, songName):
        """Add a new song to the playlist."""
        newNode = Song(songName)

        if self.head is None:
            # If the playlist is empty, the new node points to itself
            self.head = newNode
            newNode.nextSong = self.head
        else:
            # Traverse to the last node in the playlist
            temp = self.head
            while temp.nextSong != self.head:
                temp = temp.nextSong
            # Insert the new node after the last node
            temp.nextSong = newNode
            newNode.nextSong = self.head
            
  #FUNCTION FOR DELETING SONG INTO THE  PLAYLIST         
    def delSong(self, songName):
        """Delete a song from the playlist."""
        if self.head is None:
            print("Playlist is empty.")
            return

        temp = self.head
        prev = None

        # If the song to be deleted is the head node
        if temp.songName == songName:
            # Special case: The playlist has only one node
            if temp.nextSong == self.head:
                self.head = None
            else:
                # Find the last node and adjust its next pointer
                while temp.nextSong != self.head:
                    temp = temp.nextSong
                temp.nextSong = self.head.nextSong
                self.head = self.head.nextSong
            print(f"Song '{songName}' deleted.")
            return

        # Traverse the list to find the song
        while temp.nextSong != self.head and temp.songName != songName:
            prev = temp
            temp = temp.nextSong
        
        if temp.songName == songName:
            prev.nextSong = temp.nextSong
            print(f"Song '{songName}' deleted.")
        else:
            print(f"Song '{songName}' not found in the playlist.")

  #FUNCTION FOR PRINTING THE  PLAYLIST            
    def printPlaylist(self):
        """Print all songs in the playlist."""
        if self.head is None:
            print("Playlist is empty.")
            return

        temp = self.head
        print("Playlist:")
        while True:
            print(f"- {temp.songName}")
            temp = temp.nextSong
            if temp == self.head:
                break

# MAIN FUNCTION
def main():
    print("-----Welcome to your Playlist-----")
    playlist = PlayList()
    while True:
        try:
            control = input("\nINPUT \"add\" to add songs\nINPUT \"del\" to delete songs\nINPUT \"view\" to display the whole playlist\nINPUT \"s\" to stop\n>>").strip()
            if control.lower() == "s":
                break
            elif control.lower() == "add":
                songToAdd = input("Song to add: ")
                playlist.addSong(songToAdd)
            elif control.lower() == "del":
                songToDelete = input("Song to delete: ")
                playlist.delSong(songToDelete)
            elif control.lower() == "view":
                playlist.printPlaylist()
            else:
                print("Invalid Input")   
        except ValueError:
            print("Invalid input. Please enter a valid inputs or \"s\" to stop")

main()