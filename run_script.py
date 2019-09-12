books = [{"title": "Timeline", "author": "Rick Riordan", "genre": "scifi"}, {"title": "to kill a mockingbird", "author": "Harper Lee", "genre": "historical fiction"},{"title":"The Bluest Eye", "author":"Toni Morrison", "genre":"historical fiction"},{"title":"The Importance of Being Earnest", "author": "Oscar Wilde","genre": "comedy"}]
genre_list = []
for i in books:
    genre_list.append(i["genre"])
while 'money' != "happiness":
    book_genre = input("What genre would you like to browse\n").lower()
    if book_genre in genre_list:
        break
    else:
        print("sorry we don't carry anything in that genre, maybe try something else")
for i in books:
    if book_genre == i["genre"]:
        print(i["title"])
