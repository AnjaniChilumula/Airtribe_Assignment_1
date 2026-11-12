
from models import Book, Magazine, DVD, Member, LibraryItem


# Create library items
book = Book("Python 101", 1, "A. Rao")
magazine = Magazine("Tech Today", 2, 15)
dvd = DVD("Python Tutorials", 3, 120)

# Create members
alice = Member("Alice", 101)
bob = Member("Bob", 102, max_items=1)


print("===== LIBRARY MANAGEMENT SYSTEM =====")

# 1. Successful borrowing
print("\n1. Borrowing Items")

try:
    alice.borrow(book)
    print("Alice borrowed:", book.describe())

    alice.borrow(magazine)
    print("Alice borrowed:", magazine.describe())

except ValueError as e:
    print("Could not borrow:", e)


# 2. Already borrowed error
print("\n2. Already Borrowed Error")

try:
    bob.borrow(book)

except ValueError as e:
    print("Could not borrow:", e)


# 3. Borrowing limit error
print("\n3. Borrowing Limit Error")

try:
    bob.borrow(dvd)
    print("Bob borrowed:", dvd.describe())

    # Bob can borrow only one item
    bob.borrow(magazine)

except ValueError as e:
    print("Could not borrow:", e)


# 4. Returning an item not borrowed
print("\n4. Invalid Return Error")

try:
    bob.return_item(book)

except ValueError as e:
    print("Could not return:", e)


# 5. Polymorphism: Late fee calculation
print("\n5. Late Fee Calculation")

items = [book, magazine, dvd]

for item in items:
    print(
        item.describe(),
        "-> Late fee for 3 days: Rs",
        item.late_fee(3)
    )


# 6. Successful return
print("\n6. Returning Items")

fee = alice.return_item(book, days_late=3)
print("Alice returned Python 101.")
print("Late fee: Rs", fee)

fee = alice.return_item(magazine, days_late=3)
print("Alice returned Tech Today.")
print("Late fee: Rs", fee)


# 7. Borrowed items
print("\n7. Member Borrowed List")

print("Alice's borrowed items:", alice.borrowed_titles())
print("Bob's borrowed items:", bob.borrowed_titles())


# 8. Encapsulation
print("\n8. Encapsulation")

try:
    print(book.__available)

except AttributeError as e:
    print("Private attribute cannot be accessed:", e)

print("Book availability:", book.is_available())


# 9. Class attribute
print("\n9. Total Library Items")

print("Total items created:", LibraryItem.total_items)


# 10. Abstract class demonstration
print("\n10. Abstraction")

try:
    item = LibraryItem("Test Item", 100)

except TypeError as e:
    print("Cannot create LibraryItem directly:", e)
