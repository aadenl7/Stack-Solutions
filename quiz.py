import sys
import json

def calculate_risk_profile(answers):
    """
    Calculates the risk score and determines the risk profile based on a list of 'a', 'b', or 'c' answers.
    """
    points = 0
    
    if len(answers) != 5:
        print("Error: Did not receive the expected 5 answers.")
        return
        
    # Scoring Calculation 
    for answer in answers:
        if answer == "a":
            points += 1
        elif answer == "b":
            points += 2
        elif answer == "c":
            points += 3
        else:
            print(f"Error: Invalid answer '{answer}' received.")
            return


    risk_level = ""
    advice = ""
    
    if points < 8: # Scores 5, 6, 7
        risk_level = "Conservative"
        advice = f"You prefer safety and stability, even if returns are modest. Best fit: bonds, GICs, and conservative balanced funds."
    elif points < 12: # Scores 8, 9, 10, 11
        risk_level = "Balanced"
        advice = f"You're open to some risk for higher returns, but still value stability. Best fit: a diversified mix of stocks and bonds."
    else: # Scores 12, 13, 14, 15
        risk_level = "Aggressive"
        advice = f"You're comfortable with risk and market swings for long-term growth. Best fit: equities, growth funds, real estate, and alternative assets."


    result_message = f"Your total score is: {points}/15.\n\n"
    result_message += f"You are {risk_level}.\n\n{advice}"
    print(result_message)



if __name__ == "__main__":
    try:
        data_line = sys.stdin.readline() 
        data = json.loads(data_line) 
        calculate_risk_profile(data) 
        
    except json.JSONDecodeError:
        print("Error: Could not decode JSON data sent to the script. Ensure Node.js is sending a valid JSON string.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}", file=sys.stderr)
        sys.exit(1)