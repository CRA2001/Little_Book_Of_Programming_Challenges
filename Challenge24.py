'''
Create a program with the following record structure
Structure Results
 HomeTeam as string
 HomeTeamScore as integer
 AwayTeam as string
 AwayTeamScore as integer
End Structure
Make an array of 20 Results
Create a program with a menu whose options are
1. Add a result
2. Search for all results for a team

Write the code to carry out these two things.
If option 1 is selected
 collect the result and add it to the end of the results array
If option 2 is selected
 Collect team name
 display all the results that in includes that team in either the
home or away team
Hint
Include a variable to store the current number of results
'''
def fun24():
    results = {
        "HomeTeam": {
            "name": "HomeTeam",
            "score": 0
        },
        "AwayTeam": {
            "name": "AwayTeam",
            "score": 0
        }
    }

    option = 0
    while option != 3:
        results_arr = []
        print("Main Menu: ")
        print("1. Add a result")
        print("2. Search for all results for a team")
        print("Enter 3 to exit")
        option = int(input("Enter: \t"))

        if option == 1:
            for i in range(0, 20):
                score = input("Enter 'HT' for Home Team and 'AT' for Away Team: ")
                results_arr.append(score)

            # count for home team and away team
            countHome = results_arr.count('HT')
            countAway = results_arr.count('AT')

            # updating the dictionary
            results["HomeTeam"]['score'] += countHome
            results["AwayTeam"]['score'] += countAway
            print("Added")

        if option == 2:
            team = input("Enter the team name: ")
            if team in results:
                print("\t Name: {0} \n\t Score: {1}".format(results[team]['name'], results[team]['score']))

fun24()

fun24()