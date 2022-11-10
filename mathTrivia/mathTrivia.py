#!/usr/bin/env python3

def displayScore(score, triviaQA):
    print(f'Score: {score} / {len(triviaQA)}')

def main():
    triviaQA = {
        "What is the longest side of a triangle called?": "hypotenuse",
        "In a Fibonacci Sequence, what comes next? (0, 1, 1, 2, 3, _)": "5",
        "What is zero to the power of zero, 0^0?": "1",
        "What is the only even prime number?": "2",
        "Average time complexity of QuickSort?": "nlgn"
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

        displayScore(score, triviaQA)
        playAgainQuery = input("Would you like to try for a better score? (y/n): ")
    
        if (playAgainQuery.lower().startswith("y")):
            score = 0
        else:
            print("Thanks for playing!")
            playAgain = False

if __name__ == "__main__":
    main()
