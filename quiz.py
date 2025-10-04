
def risk_profile_quiz():
    """
    Makes the user answer some questions and gives a resulting score
    """
    points = 0
    answer = ""
    questions = ["1. What is your primary investment goal?\na) Preserve my capital\nb) Grow steadily with some risk\nc) Maximize growth, even with high risk",
                "2. How long do you plan to invest before needing this money?\na) Less than 3 years\nb) 3–10 years\nc) More than 10 years",
                "3. How would you react if your portfolio dropped 15% in a year?\na) Sell immediately to avoid more losses\nb) Wait it out, but feel uneasy\nc) Buy more because prices are low",
                "4. How much of your savings are you comfortable putting in higher-risk assets (stocks, real estate, etc.)?\na) Less than 30%\nb) Around half\nc) More than 70%",
                "5. If you received $100,000 tomorrow, how would you invest it?\na) Mostly in cash, GICs, or bonds\nb) A mix of safe and growth investments\nc) Mostly in stocks, real estate, or high-growth opportunities"
    ]

    for question in questions:
        while answer not in ("a", "b", "c"):
            print(question+"\n\nPlease anser a, b, or c\n")
            answer = input()
            if answer == "a":
                points += 1
            elif answer == "b":
                points += 2
            elif answer == "c":
                points += 3
            else:
                print("Invalid answer, please try again.")
        answer = ""
        
    if points<8:
        print("You are conservative.\n\nYou prefer safety and stability, even if returns are modest. Best fit: bonds, GICs, and conservative balanced funds.")
    elif points>7 and points<12:
        print("You are balanced.\n\nYou’re open to some risk for higher returns, but still value stability. Best fit: a diversified mix of stocks and bonds.")
    else:
        print("You are aggressive.\n\nYou’re comfortable with risk and market swings for long-term growth. Best fit: equities, growth funds, real estate, and alternative assets.")
    
    return

risk_profile_quiz()