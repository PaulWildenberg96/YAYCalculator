import operator

class BasicMathSolver:
    def __init__(self):
        self.operations = {
            '+': operator.add,
            '-': operator.sub,
            '*': operator.mul,
            '/': operator.truediv
        }

    def get_user_input(self):
        try:
            # Asking for the two numbers and the operator
            num1 = float(input("Enter the first number: "))
            operator_symbol = input("Enter an operator (+, -, *, /): ")
            num2 = float(input("Enter the second number: "))
            
            # Check if operator is valid
            if operator_symbol not in self.operations:
                print("Invalid operator! Please use one of: +, -, *, /")
                return None
            
            return num1, operator_symbol, num2
        except ValueError:
            print("Invalid input! Please enter numbers for the operands.")
            return None

    def solve(self, num1, operator_symbol, num2):
        try:
            # Get the corresponding operation function
            operation = self.operations[operator_symbol]
            # Perform the operation
            result = operation(num1, num2)
            return result
        except ZeroDivisionError:
            print("Error: Division by zero is undefined!")
            return None

    def run(self):
        print("Welcome to Basic Math Solver!")
        while True:
            user_input = self.get_user_input()
            if user_input:
                num1, operator_symbol, num2 = user_input
                result = self.solve(num1, operator_symbol, num2)
                if result is not None:
                    print(f"Result: {num1} {operator_symbol} {num2} = {result}")
            
            # Ask if the user wants to continue
            cont = input("Do you want to solve another problem? (yes/no): ").strip().lower()
            if cont != 'yes':
                print("Goodbye!")
                break

if __name__ == "__main__":
    solver = BasicMathSolver()
    solver.run()
