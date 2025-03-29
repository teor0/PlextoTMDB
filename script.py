import plex
import tmdb

def main():
    selection=input("Enter 1 to migrate all your films, 2 to migrate all yout TV shows: ")
    tmdb.migrateList(selection)

if __name__ == '__main__':
    main()
