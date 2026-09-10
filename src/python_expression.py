#operands
class PythonExpression:
    def __init__(self, operator, left_operand, right_operand):
        self.operator = operator
        self.left_operand = left_operand
        self.right_operand = right_operand

    def evaluate(self):
        if self.operator == '+':
            return self.left_operand + self.right_operand
        elif self.operator == '-':
            return self.left_operand - self.right_operand
        elif self.operator == '*':
            return self.left_operand * self.right_operand
        elif self.operator == '/':
            return self.left_operand / self.right_operand
        elif self.operator == '//':
            return self.left_operand // self.right_operand
        elif self.operator == '%':
            return self.left_operand % self.right_operand
        else:
            raise ValueError(f"Unsupported operator: {self.operator}")
# Example usage:
expr = PythonExpression('+', 5, 3)
result = expr.evaluate()
print(result)  # Output: 8
expr2 = PythonExpression('*', 4, 7)
result2 = expr2.evaluate()
print(result2)  # Output: 28

my_variable = 1
my_variable = 10
print(my_variable)  # Output: 10
type(my_variable)  # Output: <class 'int'>
my_variable = "Hello, World!"   
print(my_variable)  # Output: Hello, World!
type(my_variable)  # Output: <class 'str'>

x= 20
my_variable = x/2
print(my_variable)  # Output: 10.0
type(my_variable)  # Output: <class 'float'>    

print( len(['A','B',1]))  # Output: 3 - the length of the list is 3 since it contains 3 elements^

len([sum([1,1,1])]) # Output: 1 - the length of the list is 1 since it contains one element which is the sum of [1,1,1] = 3