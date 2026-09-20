class Playlist:
    def __init__(self, name, genre):
        self.name = name
        self.genre = genre
        self.songs = [ ]
        print(f"Playlist '{self.name}' ({self.genre}) is ready!")
        def add_song(self, song):
            self.songs.append(song)
            print(f"'{song}' removed.")
        def remove_song(self, song):
            if song in self.songs:
                self.songs.remove(song)
                print(f"'{song}'removed.")
            else:
                print(f"'(song)' not found in playlist.")
        def display(self):
            print(f"\n--- {self.name} ({self.genre}) ---")
            if self.songs:
                for i, song in enumerate(self.songs, 1):
                    print(f" {i}. {song}")
            else:
                print(" No songs yet. Add some!")
        def _del_(self):
            print(f"Playlist '{self.name}' has been deleted. Goodbye! ")
my_playlist = Playlist("Road Trip Mix", "Pop" )
while True:
    print("\n. Add Song 2. Remove Song 3. View Playlist 4. Delete & Quit")
    choice = input("Enter your choice: ")
    if choice == "1":
        song = input("Enter song name: ")
        my_playlist.add_song(song)
    elif choice == "2":
        song = input("Enter song to remove:")
        my_playlist.remove_song(song)
    elif choice == "3":
        my playlist.display()
    elif choice == "4":
        del my_playlist
        break
    else:
        print("Invalid choice. Enter 1, 2, 3, or 4. ")