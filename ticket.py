try :

    age=int(input("Enter your age :"))
    member=input("Enter your membership status as true /False :")
    if age > 18 :
        if member.upper() == "TRUE" :
                print("Your ticket price is 120 INR")
        else:
            print("Your ticket price is 180 INR")
    else :
        if member.upper() == "TRUE":
            print("Your ticket price is 80 INR")
        else:
            print("Your ticket price is 100 INR")
except ValueError:
    print("Kindly enter numeric value of age....!")

