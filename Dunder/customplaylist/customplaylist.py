class Playlist:

    def __init__(self):
        self.songs = []

    def add_song(self, song):
        self.songs.append(song)

    def __len__(self):
        return len(self.songs)

    def __getitem__(self, index):
        return self.songs[index]

    def __str__(self):
        return "\n".join(self.songs)


playlist = Playlist()

playlist.add_song("Believer")
playlist.add_song("Shape of You")
playlist.add_song("Faded")

print("Number of Songs:", len(playlist))

print()

print("Third Song:", playlist[2])

print()

print("Playlist:")
print(playlist)