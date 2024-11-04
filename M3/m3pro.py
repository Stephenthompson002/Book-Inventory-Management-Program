import csv  # Add this import statement
import m3_functions as fn

def main():
    """
    Main function to display the menu and handle user choices.
    """
    purchased_books = []  # List to keep track of purchased books

    while True:
        # Display the main menu
        print("\nMenu:")
        print("1. Display Book Inventory (Create Reports)")
        print("2. Purchase Book(s)")
        print("3. Display List of Purchases with Total Cost & Write Report")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            # Option 1: Display the inventory and create reports
            fn.book_display()
            with open("enventory.txt", "w") as txt_file:
                txt_file.write(f"{'Num':<5}{'Book':<60}{'Author':<30}{'Year':<8}{'Price'}\n")
                txt_file.write('-' * 120 + '\n')
                for i in range(len(fn.authors)):
                    txt_file.write(f"{i+1:<5}{fn.books[i]:<60}{fn.authors[i]:<30}{fn.published[i]:<8}${fn.prices[i]:.2f}\n")

            with open("env_report.csv", "w", newline='') as csv_file:
                writer = csv.writer(csv_file)
                writer.writerow(["Book Name", "Author", "Year Pub", "Price"])
                for i in range(len(fn.authors)):
                    writer.writerow([fn.books[i], fn.authors[i], fn.published[i], f"{fn.prices[i]:.2f}"])
            print("Reports generated: 'enventory.txt' and 'env_report.csv'.")

        elif choice == '2':
            # Option 2: Purchase books
            run_again = 'y'
            while run_again == 'y':
                try:
                    book_num = int(input("\nEnter number of book you want to buy: "))
                    if 1 <= book_num <= len(fn.books):
                        purchased_books.append(book_num - 1)
                    else:
                        print(f"Please choose a number between 1 and {len(fn.books)}.")
                except ValueError:
                    print("Invalid input. Please enter a number.")
                
                run_again = input("Would you like to purchase another book? (y for yes): ").lower()
            print("Books added to purchase list.")

        elif choice == '3':
            # Option 3: Display purchased books and write purchase report
            if not purchased_books:
                print("No books have been purchased.")
            else:
                fn.show_purchase(purchased_books)
                cost, tax, total = fn.totals(purchased_books)

                print("\nTotal price (cost of book(s) + 5% tax):")
                print(f'Book(s) cost Before Tax: ${cost:,.2f}')
                print(f'Tax: ${tax:,.2f}')
                print(f'Total After Tax: ${total:,.2f}')

                # Write purchased books report
                with open("purchased.csv", "w", newline='') as csv_file:
                    writer = csv.writer(csv_file)
                    writer.writerow(["Book Name", "Author", "Year Pub", "Price"])
                    for i in purchased_books:
                        writer.writerow([fn.books[i], fn.authors[i], fn.published[i], f"{fn.prices[i]:.2f}"])
                    writer.writerow([])
                    writer.writerow(["Total", "", "", f"${cost:.2f}"])
                    writer.writerow(["Tax", "", "", f"${tax:.2f}"])
                    writer.writerow(["Final Total", "", "", f"${total:.2f}"])
                print("Purchase report generated: 'purchased.csv'.")

        elif choice == '4':
            # Option 4: Exit the program
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Please choose an option from 1 to 4.")

# Call the main function
if __name__ == "__main__":
    main()
