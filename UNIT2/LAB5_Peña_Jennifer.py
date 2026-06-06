def show_menu():
    
    print("1. Action")
    print("2. Comedy")
    print("3. Horror")


def get_genre():
    option = int(input("Select a genre: "))
    return option


def recommend_content(genre):
    if genre == 1:
        return "Fast & Furious, John Wick"
    elif genre == 2:
        return "Grown Ups, Ted"
    elif genre == 3:
        return "The Conjuring, Annabelle"
    else:
        return "Invalid genre"


def rate_content():
    rating = int(input("Rate the recommendations from 1 to 5: "))
    return rating


continue_search = "Y"

while continue_search == "Y":

    show_menu()

    genre = get_genre()

    recommendations = recommend_content(genre)

    print("\nRecommendations:")
    print(recommendations)

    rating = rate_content()
    print("Rating recorded:", rating)

    continue_search = input("\nWould you like to perform another search? (Y/N): ").upper()

print("Program finished.")