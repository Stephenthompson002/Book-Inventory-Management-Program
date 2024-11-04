# Book Inventory Management Program

This Python program provides a menu-driven interface for managing a book inventory. Users can display the inventory, purchase books, view purchases, and generate detailed reports in both .txt and .csv formats.

## Table of Contents

* Features
* Project Structure
* Installation
* Usage
* File Output
* Requirements
* License

### Features
1. Display Book Inventory: View a list of available books including title, author, year published, and price. Additionally, generate a report (**enventory.txt** and **env_report.csv**) of the book inventory.
2. Purchase Books: Select books for purchase by entering their inventory number. The program allows multiple book purchases.
3. View Purchases: Display a list of purchased books and calculate the total cost, including a 5% tax. Generate a report (**purchased.csv**) that includes purchased books, their details, and cost breakdown.
4. Exit: Terminate the program.

### Project Structure
The program contains the following files:

* m3pro.py: The main program file with the menu-based interface.
* m3_functions.py: A module containing functions for displaying book inventory, showing purchases, and calculating totals.
* enventory.txt: A text report of the full book inventory, generated when selecting option 1.
* env_report.csv: A CSV report of the full book inventory, generated when selecting option 1.
* purchased.csv: A CSV report of purchased books and their costs, generated when selecting option 3.

### Installation
1. Clone the Repository (or download the files directly):

```
git clone https://github.com/your-repo/book-inventory-management
cd book-inventory-management
```

2. Ensure Python Is Installed:

* This program requires Python 3.x. Check your Python version with:
```
python --version
```

3. Install Required Packages:

* This program only requires Python's built-in **csv** module, which is included in standard Python installations.

### Usage
1. Run the Program: Execute the program from the command line:

```
python m3pro.py
```

2. Navigate the Menu:

* The program will display a menu with the following options:

```
Menu:
1. Display Book Inventory (Create Reports)
2. Purchase Book(s)
3. Display List of Purchases with Total Cost & Write Report
4. Exit
```

3. Choose an Option:

* Enter the number corresponding to your desired action:
  * 1: Display the inventory and generate .txt and .csv reports of the book inventory.
  * 2: Select books to purchase by entering the book number. The program will prompt you to add more books or finalize the selection.
  * 3: Display the list of purchased books, calculate the total cost with a 5% tax, and write this information to purchased.csv.
  * 4: Exit the program.

### Example Interaction
```
Menu:
1. Display Book Inventory (Create Reports)
2. Purchase Book(s)
3. Display List of Purchases with Total Cost & Write Report
4. Exit

Enter your choice (1-4): 1
```
* After selecting 1, the program will display the book inventory and generate reports (**enventory.txt** and **env_report.csv**).
* Choosing 2 will allow you to enter book numbers to purchase. Confirm by typing y if you want to add more books.
* Selecting 3 will show your purchases, calculate the total cost, and generate a detailed report (**purchased.csv**).
* Choosing 4 will exit the program.

### File Output
1. enventory.txt: A text file containing a table of the full book inventory with **book number**, **title**, **author**, **publication year**, and **price**.
2. env_report.csv: A CSV file containing the book inventory, with columns **Book Name**, **Author**, **Year Pub**, and **Price**.
3. purchased.csv: A CSV file containing details of purchased books with columns Book Name, Author, Year Pub, Price, and a summary of cost, tax, and final total.

### File Example: **purchased.csv**
```
Book Name,Author,Year Pub,Price
Hamlet,William Shakespeare,1601,14.52
Harry Potter and the Philosopher's Stone,J.K. Rowling,1997,16.62

Total,,,31.14
Tax,,,1.56
Final Total,,,32.70
```

### Requirements
* Python 3.x
* No additional libraries are needed as only built-in modules are used (csv).

### License
This project is licensed under the MIT License. See LICENSE file for more information.
