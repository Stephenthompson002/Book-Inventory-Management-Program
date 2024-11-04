import csv

# Data lists for the book inventory
authors = ["William Shakespeare", "Charles Dickens", "James Joyce", "Earnest Hemingway", "J.K. Rowling"]
books = ["Hamlet", "A Tale of Two Cities", "Ulysses", "The Old Man and the Sea", "Harry Potter and the Philosopher’s Stone"]
published = [1601, 1859, 1922, 1952, 1997]
prices = [14.52, 9.56, 19.97, 10.35, 16.62]

# Purchased books list to store selected books
purchased_books = []

def book_display():
    """
    Displays a list of books with detailed information including title, author, publication year, and price.
    """
    print(f"{'Num':<5}{'Book':<60}{'Author':<30}{'Year':<8}{'Price'}")
    print('-' * 120)
    for i in range(len(authors)):
        print(f"{i+1:<5}{books[i]:<60}{authors[i]:<30}{published[i]:<8}${prices[i]:.2f}")
    print('-' * 120)

    # Write to text and CSV files
    with open("enventory.txt", "w") as txt_file:
        txt_file.write(f"{'Num':<5}{'Book':<60}{'Author':<30}{'Year':<8}{'Price'}\n")
        txt_file.write('-' * 120 + '\n')
        for i in range(len(authors)):
            txt_file.write(f"{i+1:<5}{books[i]:<60}{authors[i]:<30}{published[i]:<8}${prices[i]:.2f}\n")
    
    with open("env_report.csv", "w", newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(["Book Name", "Author", "Year Pub", "Price"])
        for i in range(len(authors)):
            writer.writerow([books[i], authors[i], published[i], f"{prices[i]:.2f}"])

def purchase_books():
    """
    Allows user to select books for purchase and stores the selection.
    """
    while True:
        try:
            num = int(input("\nEnter the number of the book you want to buy (1-5): "))
            if 1 <= num <= len(books):
                purchased_books.append(num - 1)
            else:
                print(f"Please choose a number between 1 and {len(books)}.")
        except ValueError:
            print("Invalid input. Please enter a number.")
        
        another = input("Would you like to purchase another book? (y for yes): ").lower()
        if another != 'y':
            break

def show_purchase():
    """
    Displays purchased books and calculates total cost and tax. Also writes report to CSV file.
    """
    if not purchased_books:
        print("No books have been purchased.")
        return

    print(f"\n{'Book':<60}{'Author':<30}{'Year':<8}{'Price'}")
    print('-' * 115)
    total_cost = 0

    for i in purchased_books:
        print(f"{books[i]:<60}{authors[i]:<30}{published[i]:<8}${prices[i]:.2f}")
        total_cost += prices[i]

    tax = total_cost * 0.05
    final_total = total_cost + tax

    print("\nTotal cost (cost of book(s) + 5% tax):")
    print(f"Cost Before Tax: ${total_cost:.2f}")
    print(f"Tax: ${tax:.2f}")
    print(f"Total After Tax: ${final_total:.2f}")

    # Write purchase report to CSV
    with open("purchased.csv", "w", newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(["Book Name", "Author", "Year Pub", "Price"])
        for i in purchased_books:
            writer.writerow([books[i], authors[i], published[i], f"{prices[i]:.2f}"])
        
        writer.writerow([])  # Blank row
        writer.writerow(["Total", "", "", f"${total_cost:.2f}"])
        writer.writerow(["Tax", "", "", f"${tax:.2f}"])
        writer.writerow(["Final Total", "", "", f"${final_total:.2f}"])

def main():
    """
    Main function to display the menu and handle user choices.
    """
    while True:
        print("\nMenu:")
        print("1. Display Book Inventory (Create Reports)")
        print("2. Purchase Book(s)")
        print("3. Display List of Purchases with Total Cost & Write Report")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            book_display()
        elif choice == '2':
            purchase_books()
        elif choice == '3':
            show_purchase()
        elif choice == '4':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please choose an option from 1 to 4.")

# Run the main function
if __name__ == "__main__":
    main()
