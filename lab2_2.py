numb = input("Enter your age: ")

try:
    numb = int(numb)
    if numb < 0:
        print("Are you born yet?!")
    elif numb < 5:
        print("You're too young for movies! Enjoy cartoons.")
    elif numb < 13:
        print("G-rated or PG-rated movies.")
    elif numb < 18:
        print("PG-13 or R-rated (with parental guidance).")
    else:
        print("Any movie rating.")

        movie = input("Do you like action movies? (yes/no): ")
        if movie.lower == 'yes':
            print("You might enjoy the latest action blockbuster!")
        elif movie.lower == 'no':
            print("I suggest you porn")
        else:
            print('Answer must be only "yes" or "no"')
        
except ValueError:
    print("Your age must be NUMBER!")



