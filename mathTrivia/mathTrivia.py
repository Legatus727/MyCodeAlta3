#!/usr/bin/env python3

def displayScore(score):
    print("Score: ", score)

def main():
    triviaQA = {
        "What is the longest side of a triangle called?": "hypotenuse",
        "What is the only number that is spelt with letters in descending order": "one",
        "What is zero to the power of zero, 0^0?": "1",
        "What is the only even prime number?": "2"
    }

    playAgain = True
    score = 0
    name = input("Enter player name: ")

    while (playAgain):
        print("Good Luck " + name + "!")

        for q in triviaQA:
            answer = input(q + ": ")

            if (answer.lower() != triviaQA[q]):
                print("Incorrect!\nAnswer: " + triviaQA[q])
            else:
                print("Correct! Well Done!")
                score += 1;
    
        playAgainQuery = input("Would you like to try for a better score? (y/n): ")
    
        if (playAgainQuery.lower().startswith("y")):
            displayScore(score)
            score = 0
        else:
            displayScore(score)
            print("Thanks for playing!")

if __name__ == "__main__":
    main()
