age = "enter an age"
user_age = input(age)
try:
    print(type(user_age))
    if user_age.isdigit:
        user_age=int(user_age)
        print(type(user_age))
        if user_age>0:
            print(f"this is not age, we are taking it as {user_age}")
            print(type(user_age))
        else:
            print(user_age)

except ValueError:
    print("this is error input")

