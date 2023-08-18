import pandas as pd
import sys

def getRandomNotes(choice, amt):
    route = "csvs/" + choice + ".xlsx"
    book = pd.read_excel(route)
    # If no amt specified, get all notes
    if not amt:
        sample = book
    else:
        sample = book.sample(amt)
    return sample.to_numpy()

if __name__ == "__main__":
    if(len(sys.argv) < 2):
        print("## Provide a title arguement")
        quit()
    elif(len(sys.argv) < 3):
        print("## Provide a quantity arguement")
        quit()

    getRandomNotes(sys.argv[1], int(sys.argv[2]))