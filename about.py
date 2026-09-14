# Program: personal information card
def main():
    name = "Nikita"
    surname = "Krilovets"
    group = "IT-31"
    birth_year = 2009
    print(f"Name: {name} {surname}")
    print(f"Group: {group}")
    print(f"Age in 2026: {2026 - birth_year}")
    print("Favourite language: Python")
    
    #Add line in about.py
    print(f"Surname length: {len(surname)}")


main()