Marks = int(input("Fugen sie ihr Marks ein:"))

if Marks == 100:
    print("Full Marks with distinction")
elif Marks > 100:
    print("ungultig")
elif Marks >= 90:
    print("Sehr gut")
elif Marks >=80:
    print("gut")
elif Marks >=70:
    print("bestanden")
elif Marks >=60:
    print("befriedend")
else:
    print("nicht bestanden")
