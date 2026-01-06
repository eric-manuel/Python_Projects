# ERIC MANUEL MANZANERO
# BSCPE 2A
# DOUBLY LINK LIST
# PROBLEM: 
#     CREATE A PROGRAM THAT CAN CREATE A NEW PLAYLIST. THE PLAYLIST SHOULD HAVE THE FOLLOWING OPTIONS ADD SONGS, DELETE SONGS, AND PRINT THE PLAYLIST.

# CLASS THAT CREATES NODE OBJECT
class Song:
    def __init__(self, songName, nextSong = None, prevSong = None):
        self.songName = songName
        self.nextSong = nextSong
        self.prevSong = prevSong

#CLASS THAT CREATE THE WHOLE LINK LIST
class PlayList:
    def __init__(self, head = None, tail = None):
        self.head = head
        self.tail = tail
    
    #FUNCTION FOR ADDING SONG INTO THE  PLAYLIST
    def addSong(self, songName):
        newSong = Song(songName)
        if not self.head:  # If the playlist is empty
            self.head = self.tail = newSong
        else:
            self.tail.nextSong = newSong
            newSong.prevSong = self.tail
            self.tail = newSong
        print(f"Song '{songName}' added to the playlist.")
    
  #FUNCTION FOR DELETING SONG INTO THE  PLAYLIST
    def delSong(self, songName):
        current = self.head
        while current:
            if current.songName == songName:
                if current.prevSong:
                    current.prevSong.nextSong = current.nextSong
                else:
                    self.head = current.nextSong  # If deleting the first node
                if current.nextSong:
                    current.nextSong.prevSong = current.prevSong
                else:
                    self.tail = current.prevSong  # If deleting the last node
                print(f"Song '{songName}' deleted from the playlist.")
                return
            current = current.nextSong
        print(f"Song '{songName}' not found in the playlist.")  
            
  #FUNCTION FOR PRINTING THE  PLAYLIST 
    def printPlaylist(self):
        if not self.head:
            print("The playlist is empty.")
            return
        current = self.head
        print("Playlist:")
        while current:
            print(f"- {current.songName}")
            current = current.nextSong

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
    
    
