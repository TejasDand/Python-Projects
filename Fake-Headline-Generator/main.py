import random as r

def generate_business_headline():
    business_subjects = [
        "CEO of Tesla", "Amazon Founder", "Apple Inc.", "Google Executive", "Microsoft Board", "Facebook Developer", "Uber Driver"
    ]

    business_actions = [
        "announces", "launches", "acquires", "invests in", "partners with", "expands", "reports"
    ]

    business_places_or_things = [
        "new product line", "major investment", "global expansion", "partnership deal", "quarterly earnings", "market strategy", "innovation hub"
    ]

    while True:
        subject = r.choice(business_subjects)
        action = r.choice(business_actions)
        places_or_thing = r.choice(business_places_or_things)

        headline = f" 🚨 BREAKING NEWS: {subject} {action} {places_or_thing}."
        print("\n" + headline)

        while True:
            user_input = input("\nDo you want another fake headline of Business 💼 ? (Yes/No): ").strip().capitalize()
            if user_input == "Yes":
                break  # show another headline
            elif user_input == "No":
                return  # exit function
            else:
                print("⚠️  ENTER YES OR NO ONLY!")

def generate_politics_headline():
    politics_subjects = [
        "President of USA", "Prime Minister of UK", "Senator from California", "Governor of Texas", "Mayor of New York", "Congresswoman", "Political Analyst"
    ]

    politics_actions = [
        "proposes", "vetoes", "signs", "debates", "campaigns for", "addresses", "criticizes"
    ]

    politics_places_or_things = [
        "new legislation", "policy reform", "election results", "public speech", "town hall meeting", "press conference", "political rally"
    ]

    while True:
        subject = r.choice(politics_subjects)
        action = r.choice(politics_actions)
        places_or_thing = r.choice(politics_places_or_things)

        headline = f" 🚨 BREAKING NEWS: {subject} {action} {places_or_thing}."
        print("\n" + headline)

        while True:
            user_input = input("\nDo you want another fake headline of Politics 🤑 ? (Yes/No): ").strip().capitalize()
            if user_input == "Yes":
                break
            elif user_input == "No":
                return
            else:
                print("⚠️  ENTER YES OR NO ONLY!")

def generate_stock_headline():
    stocks_subjects = [
        "Dow Jones", "NASDAQ", "S&P 500", "Tesla Stock", "Apple Shares", "Amazon Stock", "Microsoft Equity"
    ]

    stocks_actions = [
        "rises", "falls", "stabilizes", "surges", "plummets", "recovers", "fluctuates"
    ]

    stocks_places_or_things = [
        "after earnings report", "amid market volatility", "due to investor sentiment", "following merger news", "during trading session", "on economic data", "amid geopolitical tensions"
    ]

    while True:
        subject = r.choice(stocks_subjects)
        action = r.choice(stocks_actions)
        places_or_things = r.choice(stocks_places_or_things)

        headline = f" 🚨 BREAKING NEWS: {subject} {action} {places_or_things}."
        print("\n" + headline)

        while True:
            user_input = input("\nDo you want another fake headline of Stocks 📉 ? (Yes/No): ").strip().capitalize()
            if user_input == "Yes":
                break
            elif user_input == "No":
                return
            else:
                print("⚠️  ENTER YES OR NO ONLY!")



print("\n📰 Welcome to the Fake News Headline Generator!")

while True:
    category_input = input("\nWhich category would you like to generate a fake headline for? (Business-B, Politics-P, Stocks-S). To exit, type 'Exit': ").strip().capitalize()

    if category_input == "Exit" or category_input == "E":
        break

    match category_input:
        case "B" | "Business":
            generate_business_headline()
        case "P" | "Politics":
            generate_politics_headline()
        case "S" | "Stocks":
            generate_stock_headline()
        case _:
            print("⚠️  Please enter proper Category Name or Character!")

print("\nThanks for using the Fake News Headline Generator. Have a fun day!⛅")