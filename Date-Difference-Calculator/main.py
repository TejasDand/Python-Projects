# Date Difference Calculator Project
from datetime import datetime
from dateutil.relativedelta import relativedelta


try:
    # Taking input from the user
    start_input = input("Enter Start Date (YYYY-MM-DD): ")
    end_input = input("Enter End Date (YYYY-MM-DD): ")

    # Convert string input into date object
    start_date = datetime.strptime(start_input, "%Y-%m-%d").date()
    end_date = datetime.strptime(end_input, "%Y-%m-%d").date()

    if end_date < start_date:
        print("⚠️ Error: End date cannot be earlier than start date. Please check your input.")

    else:
    # Calculating difference
        diff = relativedelta(end_date, start_date)
        total_days = (end_date - start_date).days

        # Printing the results
        print("\nDate Difference:")
        print(f"Years : {diff.years}")
        print(f"Months : {diff.months}")
        print(f"Days : {diff.days}")
        print(f"Total Days : {total_days}")


except ValueError:
     # Custom error message for invalid input
    print("❌ Invalid date format! Please enter the date in (YYYY-MM-DD) format or Please check your input.")