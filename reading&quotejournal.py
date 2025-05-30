#personal reading journal and quote collector
books= [
    {
        "title" : "hidden",
        "year_published" : 2023,
        "user_year": 2025,
        "author": "elven fictional",
        "genre": {"thriller"},
        "status":"on hold",
        "quotes":[
            { "text":"What you don't see can hurt you the most.", "page": 102},
            {"text":"Not everything that's hidden is meant to stay buried forever", "page":45}
        ]
    },
    {
        "title" : "namal",
        "year_published" : 2015,
        "user_year": 2024,
        "author": "nimra ahmed",
        "genre": {"thriller","romance","criminal" },
        "status":"completed",
        "quotes" : [
            { "text":"Sometimes, the people who are meant to be in your life are not the ones you expect.","page":112},
            { "text":"Love can heal the deepest wounds, but only if you let it.","page":201},
            {"text":"Every secret has a story waiting to be told.","page":275}
        ]
    },
    {
        "title" : "Anxious people",
        "year_published" : 2021,
        "user_year": 2025,
        "author": " fredrick",
        "genre": {"humour","fiction"},
        "status":"reading",
        "quotes" : [
            {"text":"The most important thing in life is not what happens to you but how you respond to it","page":150},
            {"text":"It's okay to be a little scared. It's okay to be a little anxious. It means you care","page":412}
        ]
    },
    {
        "title" : "peer-e-kamil",
        "year_published" : 2004,
        "user_year": 2024,
        "author": "umera ahmed",
        "genre": {"fiction","drama","religious"},
        "status":"completed",
        "quotes" : [
            {"text":"People do not leave you. Time does","page":225},
            {"text":"When a person bows only before Allah, the world bows before him ","page":240},
            {"text":"Love that brings you closer to Allah is the only love worth having","page":325},
            {"text":"Guidance is not forced; it is gifted","page":340}
        ]
    }
    
]

def book_entry():
    title=input("Enter the title of book: ")
    author=input("Enter the author of book: ")
    year_published=int(input("Enter the year of publication: "))
    user_year=int(input("Enter the year you completed this book (or started if reading and on hold)"))
    genres=(input("enter genres(separate them by comma ): "))
    genres=set(g.strip() for g in genres.split(","))
    status=input("Status of book?  (reading, completed, on hold) ")
    book={
        "title" : title,
        "year_published" : year_published ,
        "user_year": user_year,
        "author": author,
        "genre": genres,
        "status":status,
        "quotes": []
    }
    books.append(book)
    
def view_book():
    sorted_books= sorted(books, key=lambda book:book["year_published"])
    for book in sorted_books:
        print(book["title"],"",book["year_published"])

def update_status():
    print("If you want to update status press 1 ")
    print("If you want to add genre press 2 ")
    choice=int(input("enter the number: "))
    if choice==1:
      target_book=input("which book's status you want to update? ")
      target_book=target_book.lower()
      for value in books:
        if value["title"].lower()==target_book:
           print("previous status: ",value["status"])
           update=input("Enter updated status: ")
           value["status"]=update
           print("status updated! ")
           break
      else:
        print("book not found!")
    elif choice==2:
        target_book=input("which book's genre you want to add? ")
        target_book=target_book.lower()
        for value in books:
            if value["title"].lower()==target_book:
                print(value["genre"])
                ans=input("Enter genre you want to add: ").strip()
                value["genre"].add(ans)
                print("added successfully! ")
    else:
        print("Invalid! ")

def search_bygenre():
    print("If you want to search by genre press 1 ")
    print("If you want to search by status press 2 ")
    choice=int(input("enter the number: "))
    
    if choice==1:
     target_genre=input("Enter genre of book you want to search for: ").lower()
     for book in books:
         for genre in book["genre"]:
          if target_genre in genre:
           print(book["title"]," ",book["author"],"    ",book["genre"])
    elif choice==2:
        target_status=input("enter status you want to search by: (completed/reading/on hold) ").lower()
        for book in books:
            if target_status == book ["status"].lower():
                print(book["title"]," ",book["author"],"     ",book["status"])
    else:
        print("Enter valid number! ")

def delete_book():
    to_delete=input("Enter book you want to delete entry for: ").lower()
    for book in books:
        if book["title"].lower()==to_delete:
            books.remove(book)
            print("deleted! ")
            break
    else:
      print("book not found! ")
# now functions for quote collector menu :
def add_quote():
    target_book=input("Enter name of book in which you want to enter quote: ").lower()
    for book in books:
        if book["title"].lower()==target_book:
            line=input("Enter quote you want to add: ")
            page=int(input("Enter page number: "))
            new={"text":line,"page":page}
            book["quotes"].append(new)
            print("added successfully! ")
            break
    else:
        print(" Invalid choice!")
        
def view_quotes():
    for book in books:
        print("quotes from book: ",book["title"])
        for quote in book["quotes"]:
            print(quote["text"],"  ",quote["page"])
        print("")
        
def search_quote():
    key=input("Enter word/words to search for quote ").lower()
    exists=False
    for book in books:
        for quote in book["quotes"]:
            if key in quote["text"].lower():
                print(quote["text"])
                print("    From book ",book["title"]," and page number: ",quote["page"])
                exists=True
    if not exists:
        print("Doesn't exists.")

def delete_quote():
    line=input("which quote you want to delete: ").lower()
    found=False
    for book in books:
        for quote in book["quotes"]:
            if line in quote["text"].lower():
                print( quote["text"])
                confirm=(input("Is this the quote you want to delete? (yes/no) ")).lower()
                if (confirm=="yes"):
                    book["quotes"].remove(quote)
                    found=True
                    break
    if not found:
        print("Not found!")

def books_inyear():
    year=int(input("Enter year you want to check for: "))
    found=False
    books_completed=[]
    for book in books:
          if year==book["user_year"] and book["status"]=="completed":
              books_completed.append(book["title"])
              print (book["title"])
              found=True
    if not found:
        print("No book completed in your entered year.")
        
def most_quotes():
    max=0
    name =""
    for book in books:
        count=0
        for quote in book["quotes"]:
            count+=1
        if(max<count):
            max=count
            name=book["title"]
    print("the book with most quotes is: ", name, " ",max)

def author_most_enteries():
    author_count={}
    for book in books:
        author=book["author"].lower()
        if author in author_count:
            author_count [author] += 1
        else:
            author_count [author] = 1
    max_count=max(author_count.values())
    for author in author_count:
        if author_count[author]==max_count:
            print("author with most entries is:  name : ",author," books: ",max_count)
           
#  menu      
print("PERSONAL READING JOURNAL & QUOTE COLLECTOR:")
print("Press 1 to manage books.")
print("Press 2 to manage quotes.")
print("Press 3 to access analysis features.")
main_choice=int(input("now enter (1 ,2 or 3 ):  "))

if main_choice==1:
    print(" ....PERSONAL READING JOURNAL....")
    print("Welcome to the menu: ")
    print("Below our options you can select: ")
    print("Press 1 to add a new book entry. ")
    print("Press 2 to view all books. ")
    print("Press 3 to search book by genre or status. ")
    print("Press 4 to update a book's status or add genre")
    print("Press 5 to delete a book entry")
    user=int(input("Enter your choice:  "))
    if user==1:
        book_entry()
    elif user==2:
        view_book()
    elif user==3:
        search_bygenre()
    elif user==4:
        update_status()
    elif user==5:
        delete_book()
    else:
        print("Enter valid number!")
elif( main_choice==2):
    print(" .... QUOTE COLLECTOR ....")
    print("Welcome to the menu: ")
    print("Below our options you can select: ")    
    print("Press 1 to add a new quote. ")
    print("Press 2 to view all quotes. ")
    print("Press 3 to search quotes by keyword ")
    print("Press 4 to delete a quote")
    user=int(input("Enter your choice:  "))
    if (user==1):
        add_quote()
    elif (user==2):
        view_quotes()
    elif (user==3):
        search_quote()
    elif (user==4):
        delete_quote()
    else:
        print("invalid! ")
    
elif(main_choice==3):              
    print("Analysis: ")
    print("Want to check books read in particular year? press 1 ")
    print("Want to check book with most quotes?  press 2 ")
    print("Want to check author with most entries? press 3 ")
    choice=int(input("Enter: "))
    if (choice==1):
            books_inyear()
    elif(choice==2):
            most_quotes()
    elif(choice==3):
            author_most_enteries()
    else:
         print("Invalid! ")  
else:
    print("Invalid!")

        