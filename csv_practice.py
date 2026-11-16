# Reflection 1: Both Python and Excel can read sales data, calculate totals,
# and filter orders. Python makes it easier to repeat the same process across
# many files automatically, while Excel makes quick visual checks, charts,
# and interactive edits easier without writing code.
#
# Reflection 2: A store could append a log entry after each daily sales import
# with its timestamp and revenue total. Append mode preserves previous runs,
# so the manager can review the history and investigate missing imports.

import csv
from datetime import datetime


# Exercise 1: Verify the input file's header and number of data rows.
with open("data/sales.csv", newline="", encoding="utf-8") as file:
    reader = csv.reader(file)
    header = next(reader)
    rows = list(reader)
assert header == ["product", "price", "quantity"]
assert len(rows) == 12
print(f"Exercise 1: Found {len(rows)} data rows with header {header}")

# Exercise 2: csv.reader returns a list of strings for every row.
print("\nExercise 2: Raw rows (including header)")
with open("data/sales.csv", newline="", encoding="utf-8") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

# Exercise 3: Consume the header before looping over the data.
print("\nExercise 3: Header and data separately")
with open("data/sales.csv", newline="", encoding="utf-8") as file:
    reader = csv.reader(file)
    header = next(reader)
    print("Header:", header)
    for row in reader:
        print(row)

# Exercise 4: Convert prices and quantities before multiplying.
print("\nExercise 4: Order totals")
total_revenue = 0.0
orders = []
with open("data/sales.csv", newline="", encoding="utf-8") as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        product = row[0]
        price = float(row[1])
        quantity = int(row[2])
        total = round(price * quantity, 2)
        total_revenue += total
        orders.append([product, price, quantity, total])
        print(f"{product}: {quantity} units × ${price:.2f} = ${total:.2f}")
total_revenue = round(total_revenue, 2)
print(f"Overall total revenue: ${total_revenue:.2f}")

# Exercise 5: Keep only orders strictly greater than $100.
rows_written = 0
with open("data/cleaned.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Product", "Price", "Qty", "Total"])
    for product, price, quantity, total in orders:
        if total > 100:
            writer.writerow([product, f"{price:.2f}", quantity, f"{total:.2f}"])
            rows_written += 1
print(f"\nExercise 5: Wrote {rows_written} of {len(orders)} original rows.")

# Exercise 6: Prefer reader for simple positional data with a fixed column order.
# Prefer DictReader for named columns; names stay clear even if columns move.
print("\nExercise 6: DictReader totals")
dict_total = 0.0
with open("data/sales.csv", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        product = row["product"]
        price = float(row["price"])
        quantity = int(row["quantity"])
        total = round(price * quantity, 2)
        dict_total += total
        print(f"{product}: {quantity} units × ${price:.2f} = ${total:.2f}")
dict_total = round(dict_total, 2)
assert dict_total == total_revenue
print(f"DictReader total: ${dict_total:.2f} (matches Exercise 4)")

# Exercise 7: Accumulate repeat products and sort by product name.
summary = {}
with open("data/sales.csv", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        product = row["product"]
        revenue = round(float(row["price"]) * int(row["quantity"]), 2)
        summary[product] = summary.get(product, 0.0) + revenue
print("\nExercise 7: Sales summary by product")
for product in sorted(summary):
    print(f"{product}: ${summary[product]:.2f}")

# Exercise 8: Append exactly one timestamped entry per script execution.
with open("data/run_log.txt", "a", encoding="utf-8") as file:
    file.write(f"{datetime.now().isoformat(sep=' ', timespec='microseconds')} | Total revenue: ${total_revenue:.2f}\n")
print("\nExercise 8: Appended this run to data/run_log.txt.")
