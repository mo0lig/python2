def reduce_equation(equation):
    # Replace spaces and handle negative signs
    equation = equation.replace(" ", "")
    equation = equation.replace("(-", "(0-")
    equation = equation.replace("--", "+")

    # Expand and simplify the expression
    while '(' in equation:
        # Find the innermost parentheses and evaluate
        start = equation.rfind('(')
        end = equation.find(')', start)
        inner_expression = equation[start + 1:end]
        inner_result = str(eval(inner_expression))
        equation = equation[:start] + inner_result + equation[end + 1:]

    # Simplify further
    simplified_expression = str(eval(equation))

    return simplified_expression

# Example usage
input_equation = "-24*x - (1 - x)*((2 - x)*(4 - x) - 6) + 12"
reduced_equation = reduce_equation(input_equation)

# Display the result
print("Original equation:", input_equation)
print("Reduced equation:", reduced_equation)
