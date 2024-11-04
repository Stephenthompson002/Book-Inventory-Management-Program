# m3Pro_Purchase.py
# 10/3/2024
# CSC-121 m3Pro-Purchases
# Robin Buie

# List of authors, books, years published, and prices
authors = ["William Shakespeare", "Charles Dickens", "James Joyce", "Earnest Hemingway", "J.K. Rowling"]
books = ["Hamlet", "A Tale of Two Cities", "Ulysses", "The Old Man and the Sea", "Harry Potter and the Philosopher's Stone"]
published = [1601, 1859, 1922, 1952, 1997]
prices = [14.52, 9.56, 19.97, 10.35, 16.62]

def book_display():
    """Display the list of available books with authors, publication years, and prices."""
    print(f"{'Num':<5} {'Book':<40} {'Author':<25} {'Year':<10} {'Price':<10}")
    print("-" * 90)
    for i in range(len(books)):
        print(f"{i+1:<5} {books[i]:<40} {authors[i]:<25} {published[i]:<10} ${prices[i]:<10.2f}")

def show_purchase(book_nums):
    """Display the details of books purchased based on user selection."""
    print(f"\n{'Book':<40} {'Author':<25} {'Year':<10} {'Price':<10}")
    print("-" * 90)
    for num in book_nums:
        index = num - 1  # Adjusting for zero-based index
        print(f"{books[index]:<40} {authors[index]:<25} {published[index]:<10} ${prices[index]:<10.2f}")

def totals(book_nums):
    """Calculate the total cost, tax, and final total for selected books."""
    before_tax = sum(prices[num - 1] for num in book_nums)
    tax = before_tax * 0.05  # Calculate 5% tax
    final_total = before_tax + tax
    return before_tax, tax, final_total

def main():
    """Main function to run the program."""
    # Display the list of books
    book_display()
    
    # Initialize an empty list to store selected book numbers
    book_nums = []
    
    # Loop for selecting books to purchase
    while True:
        try:
            num = int(input("\nEnter the number of the book you want to buy: "))
            if 1 <= num <= len(books):
                book_nums.append(num)
            else:
                print(f"Please choose a number between 1 and {len(books)}.")
        except ValueError:
            print("Invalid input. Please enter a number.")
        
        # Ask if the user wants to select another book
        another = input("Would you like to purchase another book? (y for yes): ").lower()
        if another != 'y':
            break
    
    # Display the selected books
    show_purchase(book_nums)
    
    # Calculate and display the total cost, tax, and final amount
    before_tax, tax, final_total = totals(book_nums)
    print("\nTotal price (cost of book(s) + 5% tax):")
    print(f"Book(s) cost Before Tax: ${before_tax:.2f}")
    print(f"Tax: ${tax:.2f}")
    print(f"Total (after tax): ${final_total:.2f}")

# Run the main function
if __name__ == "__main__":
    main()
