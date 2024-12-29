import random
import art
from game_data import data

# score = 0


def compare(user_guess, followers_a, followers_b):
    """compare a and b to check"""
    if followers_a >followers_b:
        return user_guess=="a"
    else:
        return user_guess=="b"
        
def formate_data(account):
    """formating data into printable form"""
    account_name = account["name"]
    account_description = account["description"]
    account_country = account["country"]
    return  f"{account_name}, {account_description}, {account_country}"
    # account_name = b_account["name"]
    # account_description = b_account["description"]
    # account_country = b_account["country"]


def game():
    """display art/logo"""
    print("welcome to the higher lower game".title())
    print("")
    print(art.logo)
    print("")

    score = 0

    """to make a = b after guessing the right answer"""
    b_account = random.choice(data)

    game_should_continue =True

    """making game to repeat it self"""
    while game_should_continue:

        """generate a random account from the game_data"""
        a_account = b_account
        b_account = random.choice(data)
        if a_account == b_account:
            b_account = random.choice(data)
        
        print(f"Compare A: {formate_data(account=a_account)}")
        print(art.vs)
        print(f"Compare B: {formate_data(account=b_account)}")

        """ask user to guess"""
        guess = input("Who has more followers? Type 'A' or 'B':".lower())
        

        """see a and b followers"""
        a_follower_count = a_account["follower_count"]
        b_follower_count = b_account["follower_count"]

        """using our compare() function to check"""
        is_correct = compare(user_guess=guess, followers_a= a_follower_count, followers_b= b_follower_count)
        
        """giving feedback to the user"""

        if is_correct:
            """increase score"""
            score += 1
            print(f"You're right! Current score: {score}")
            print("")
            
        else:
            print(f"sorry, that's wrong! Your final score is: {score}".title())
            game_should_continue =False
    
print(game())
