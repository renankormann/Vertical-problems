# This program is a function that receives simple addition and subtraction problems and separates them in vertical form.

# The function is called vertProblems.
def main():
    # Create an empty list that will "hold" the problems and set up initial conditions for the loop that add the problems to the list.
    allProblems = list()
    problem = 0
    holdTmp = 1

    # Start the loop to get the problems.
    print("Enter the problems then type enter, and type 'done' after you are done.")
    while problem != "done":
        problem = input()
        problem = problem.replace(" ", "")
        if(problem != "done"):
            allProblems.append(problem)
        holdTmp += 1

    # Ask if the user wants the solutions.
    print("Do you want to print the solutions as well?")
    printSolutions = input()
    if printSolutions == "yes" or printSolutions == "Yes":
        printSolutions = True
    else:
        printSolutions = False

    # Call vertProblems.
    print(vertProblems(allProblems, printSolutions))

def vertProblems(problems, solve):
    
    allProblems = problems
    printValues = solve


    # Define a function that finds the errors in vertProblems.
    def errorFinder(problems):
        # Too many problems error.
        if len(problems) > 5:
            return("Error: Too many problems.")

        # Appropriate operators error.
        for element in range(len(problems)):
            if problems[element].find("+") == -1 and problems[element].find("-") == -1:
                return("Error: Operator must be '+' or '-'.")

        # If numbers are not all digits error.
        for i in range(len(problems)):
            if "+" in problems[i]:
                hold1 = (problems[i].rsplit("+"))[0]
                hold2 = (problems[i].rsplit("+"))[1]
            else:
                hold1 = (problems[i].rsplit("-"))[0]
                hold2 = (problems[i].rsplit("-"))[1]
            if hold1.isdigit() == False or hold2.isdigit() == False:
                return("Error: Numbers must only contain digits.")
    
        # Amount of digits error.
        for i in range(len(problems)):
            if "+" in problems[i]:
                hold1 = (problems[i].rsplit("+"))[0]
                hold2 = (problems[i].rsplit("+"))[1]
            else:
                hold1 = (problems[i].rsplit("-"))[0]
                hold2 = (problems[i].rsplit("-"))[1]
            if len(hold1) > 4 or len(hold2) > 4:
                return("Error: Numbers cannot be more than four digits.")

        # No errors.
        return(int(1))

    # Call errorFinder function to see if there are errors.
    error = errorFinder(allProblems)
    if error != 1:
        return(error)

    # Create two lists to separate all problems and other two list to hold the horizontal lines
    firstLine = list()
    secondLine = list()
    thirdLine = list()

    # List to hold the solutions if necessary
    if printValues:
        solutions = list()
        
    # From this point I used 'hold1' and 'hold2' to hold respectively the first part and second part of the problems.
    # Computing the solutions and assigning it to the list solutions.
    if printValues:
        for i in range(len(allProblems)):
            if "+" in allProblems[i]:
                hold1 = (allProblems[i].rsplit("+"))[0]
                hold2 = (allProblems[i].rsplit("+"))[1]
                elementSolution = int(hold1) + int(hold2)
                solutions.append(str(elementSolution).rjust(max(len(hold1), len(hold2))+2))
            else:
                hold1st = (allProblems[i].rsplit("-"))[0]
                hold2nd = (allProblems[i].rsplit("-"))[1]
                elementSolution = int(hold1st) - int(hold2nd)
                solutions.append(str(elementSolution).rjust(max(len(hold1st), len(hold2nd))+2))
            if i < len(allProblems) - 1:
                solutions.append("    ")
    
    # The first list gets the first numbers from each problem, the second list gets the sign and the second number from each problem.
    for i in range(len(allProblems)):
        resultLine = ""
        if "+" in allProblems[i]:
            hold1 = (allProblems[i].rsplit("+"))[0]
            hold2 = (allProblems[i].rsplit("+"))[1]
            firstLine.append(hold1.rjust(max(len(hold1), len(hold2))+2))
            secondLine.append("+" + hold2.rjust(max(len(hold1), len(hold2))+1))
        else:
            hold1 = (allProblems[i].rsplit("-"))[0]
            hold2 = (allProblems[i].rsplit("-"))[1]
            firstLine.append(hold1.rjust(max(len(hold1), len(hold2))+2))
            secondLine.append("-" + hold2.rjust(max(len(hold1), len(hold2))+1))
        resultLine = resultLine.rjust(max(len(hold1), len(hold2))+2, "-")
        thirdLine.append(resultLine)
        if i < len(allProblems) - 1:
            firstLine.append("    ")
            secondLine.append("    ")
            thirdLine.append("    ")

    # Printing the vertical problems.

    arrenged_problems = ""
    
    for element in range(len(firstLine)):
        if element < len(firstLine) - 1:
            arrenged_problems += firstLine[element]
        else:
            arrenged_problems += firstLine[element] + "\n"
    for element in range(len(firstLine)):
        if element < len(firstLine) - 1:
            arrenged_problems += secondLine[element]
        else:
            arrenged_problems += secondLine[element] + "\n"
    for element in range(len(firstLine)):
        if element < len(firstLine) - 1:
            arrenged_problems += thirdLine[element]
        else:
            arrenged_problems += thirdLine[element] + "\n"
    if printValues:
        for element in range(len(firstLine)):
            if element < len(firstLine) - 1:
                arrenged_problems += solutions[element]
            else:
                arrenged_problems += solutions[element]

    return(arrenged_problems)
    
# Call the main function.
if __name__ == "__main__":
    main()
