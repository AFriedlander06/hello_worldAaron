

class CalculateGrade:
    
    def __init__(self):
        """Initializes the attributes to describe a calculated grade"""
        
        # createst the empty list "self.assignments"
        self.assignments = []
        
        # creates the empty list "self.grades"
        self.grades = []
        
        # creates the empty list "self.weights"
        self.weights = []
        
        # creates the variable self.course_grade and sets it equal to 0
        self.course_grade = 0
        
    def add_assignment(self, assignment_name):
        """Adds the assignment name to the list of assignments"""
        
        # appends the assignment_name to the empty list "assignments
        self.assignments.append(assignment_name)
        
        # appends a blank to the list "grades" to account for the fact that
        # there is an assignment already created, but a grade hasn't been
        # entered
        self.grades.append("")
        
        # appends a blank to the list "weights" to account for the fact that
        # there is an assignment already created, but a weight hasn't been
        # entered
        self.weights.append("")
        
        # prints "{entered assignment} added to assignments" to the console
        print(f"{assignment_name} added to assignments" )
        
    def add_grade(self, assignment_name, grade):
        """Adds grade that corresponds to a specific assignemnt to the list of 
        grades"""
        
        # creates an if statement saying that if the assignment name that the
        # user is trying to enter a grade for exists, then the code creates the
        # variable "ind" which searches for the assignment name in the list
        # "assignments" using index.
        if  assignment_name in self.assignments:
            ind = self.assignments.index(assignment_name)
            
            # creates an if statement saying that if the grade entered is a 
            # number (using the function is_number), then the index of the list
            # "grades" correlating to the index of the corresponding assignment
            # name is changed to the entered grade. Additionally the f-string
            # {assignment_name} has been assigned a grade of {grade} is printed
            # to the console
            if self.is_number(grade):
                self.grades[ind] = str(grade)
                print(f"{assignment_name} has been assigned a grade of {grade}")
            
            # If the entered grade is not a number then "Grade is not a valid
            # number" is printed to the console
            else:
                print("Grade is not a valid number.")   
        # If the assingment name which the grade is being entered for does not
        # exist, then "That assignment does not exist." is printed to the 
        # console
        else:
            print("That assignment does not exist.")
            
            
    def add_weight(self, assignment_name, weight):
        """Adds weight that corresponds to a specific assignment tothe list of 
        weights"""
        
        # creates an if statement saying that if the assignment name that the
        # user is trying to enter a grade for exists, then the code creates the
        # variable "ind" which searches for the assignment name in the list
        # "assignments" using index.
        if  assignment_name in self.assignments:
            ind = self.assignments.index(assignment_name)
            
            # creates an if statement saying that if the weight entered is a 
            # number (using the function is_number), then the index of the list
            # "weights" correlating to the index of the corresponding assignment
            # name is changed to the entered weight. Additionally the f-string
            # {assignment_name} has been assigned a weight of {weight} is 
            # printed to the console
            if self.is_number(weight):
                self.weights[ind] = str(weight)
                print(f"{assignment_name} has been assigned a weight of {weight}")
            
            # If the entered weight is not a number then "Weight is not a valid
            # number" is printed to the console
            else:
                print("Weight is not a valid number.")   
        
        # If the assingment name which the weight is being entered for does not
        # exist, then "That assignment does not exist." is printed to the 
        # console                
        else:
            print("That assignment does not exist.")
                  
            
    def print_grades(self):
        """Prints all of a person's grades to the console"""
        
        # creates the variable col_width which sets the widths of the three
        # columns with titles "Assignment", "Grade", and "Weight" to the
        # length of (the longest word or number of the titles or the entered 
        # exams, grades, or weights) + 3. In this example the longest word or
        # number was "Assignment", thus the length of each column is the length
        # of the number of characters in "Assignment" + 3.
        col_width = max(len(value) for value in ["Assignment", "Grade", "Weight"] +
self.assignments + self.grades + self.weights) + 3 
        print("\n")
        print("Assignment".ljust(col_width) + "Grade".ljust(col_width) + 
"Weight".ljust(col_width))
        
        # This for loop makes a row for each assingment name containing the
        # assignment name in the first column, the grade in the second column,
        # and the weight of the assignment in the third column. The number of 
        # rows below the row of titles is equal to the number of assignments
        for i in range(len(self.assignments)):
            print(self.assignments[i].ljust(col_width) + 
self.grades[i].ljust(col_width) + self.weights[i].ljust(col_width))
                
        print("\n")
            
    def calculate_grade(self):
        """Calculates a person's overall grade"""
        
        # if the sum of the weights of all the assignments is not equal to
        # 1, then the code prints the f-string "The weights do not sum to 1.
        # They sum to {sum([float(i) for i in self.weights])} (the sum of all
        # the weights)
        if sum([float(i) for i in self.weights])!=1:
            print(f"The weights do not sum to 1. They sum to {sum([float(i) for i in self.weights])}")
        
        # This for loop takes the sum of the grades*the weights of all the 
        # assignment types for all i in range of the length of "self.weights"
        # (the number of weights a.k.a the number of assignments). The variable
        # self.course_grade is this calculated value.
        for i in range(len(self.weights)):
            self.course_grade += float(self.grades[i])*float(self.weights[i])
        
        # prints the calculated self.course_grade to the console in the 
        # f-string "Your grade is {self.course_grade}
        print(f"Your grade is {self.course_grade}")
        
        
    def is_number(self, s):
        """Tests to see if an entry is a number"""
        
        # If the entry is a number, then the code returns True and knows that
        # it is a number
        try:
            float(s)
            return True
        
        # If the entry is not a number, then the code returns False as well as
        # an error
        except ValueError:
            return False
                    
# Creates my grade which calls the class "Calculate Grade"                 
my_grade = CalculateGrade()

# Uses the function "add_assignment" to add "exam 1" to the list "assignments"
my_grade.add_assignment("exam 1")

# Uses the function "add_grade" to add "87" to the list "grades" which 
# corresponds to the assignment "exam 1"
my_grade.add_grade("exam 1", 87)

# Uses the function "add_weight" to add ".2" to the list "weights" which 
# corresponds to the assignment "exam 1"
my_grade.add_weight("exam 1", .2)

# Uses the function "add_assignment" to add "exam 2" to the list "assignments"
my_grade.add_assignment("exam 2")

# Uses the function "add_grade" to add "74" to the list "grades" which 
# corresponds to the assignment "exam 2"
my_grade.add_grade("exam 2", 74)

# Uses the function "add_weight" to add ".2" to the list "weights" which 
# corresponds to the assignment "exam 2"
my_grade.add_weight("exam 2", .2)

# Uses the function "add_assignment" to add "exam 3" to the list "assignments"
my_grade.add_assignment("exam 3")

# Uses the function "add_grade" to add "92" to the list "grades" which 
# corresponds to the assignment "exam 3"
my_grade.add_grade("exam 3", 92)

# Uses the function "add_weight" to add ".2" to the list "weights" which 
# corresponds to the assignment "exam 3"
my_grade.add_weight("exam 3", .2)

# Uses the function "add_assignment" to add "hw" to the list "assignments"
my_grade.add_assignment("hw")

# Uses the function "add_grade" to add "99.6" to the list "grades" which 
# corresponds to the assignment "hw"
my_grade.add_grade("hw", 99.6)

# Uses the function "add_weight" to add ".15" to the list "weights" which 
# corresponds to the assignment "hw"
my_grade.add_weight("hw", .15)

# Uses the function "add_assignment" to add "final" to the list "assignments"
my_grade.add_assignment("final")

# Uses the function "add_grade" to add "93" to the list "grades" which 
# corresponds to the assignment "final"
my_grade.add_grade("final", 93)

# Uses the function "add_weight" to add ".25" to the list "weights" which 
# corresponds to the assignment "final"
my_grade.add_weight("final", .25)

# Uses the function "print_grades" to print the Assignments with their 
# corresponding Grades and Weights in a table to the console.
# This is the table:
# Assignment   Grade        Weight       
# exam 1       87           0.2          
# exam 2       74           0.2          
# exam 3       92           0.2          
# hw           99.6         0.15         
# final        93           0.25   
my_grade.print_grades()

# Uses the function "calculate_grade" to calculate the overall grade given the
# grades and weights for each assignment and prints it to the console. 
# The final grade in this example is an 88.79
my_grade.calculate_grade()
