import marimo as mo

__generated_with = "0.13.15"
app = mo.App(width="medium")


@app.cell
def __():
    import marimo as mo
    return mo,


@app.cell
def __(mo):
    mo.md("""
    # Chapter 5: Numbers and Expressions
    
    Welcome to this interactive exploration of Python's numeric objects and operations! 
    This notebook will guide you through hands-on experiments with Python's core numeric types.
    
    ## Learning Objectives
    By the end of this interactive session, you will be able to:
    - [ ] Work with Python's core numeric types (integers, floats, complex numbers)
    - [ ] Apply arithmetic operators and understand operator precedence
    - [ ] Convert between different numeric bases (decimal, hex, octal, binary)
    - [ ] Use advanced numeric types (Decimal, Fraction, Set)
    - [ ] Perform bitwise operations and understand their applications
    - [ ] Apply numeric built-in functions and methods effectively
    """)
    return

@app.cell
def __(mo):
    mo.md("""
    ## 🔢 Numeric Object Basics
    
    Python supports several numeric types. Let's explore the most fundamental ones:
    
    - **Integer objects**: Whole numbers with unlimited precision
    - **Floating-point objects**: Numbers with decimal points
    - **Complex number objects**: Numbers with real and imaginary parts
    """)
    return

@app.cell
def __(mo):
    # Interactive numeric literals playground
    integer_input = mo.ui.text(
        value="42",
        label="Enter an integer:",
        full_width=True
    )
    
    float_input = mo.ui.text(
        value="3.14159",
        label="Enter a floating-point number:",
        full_width=True
    )
    
    complex_input = mo.ui.text(
        value="3+4j",
        label="Enter a complex number:",
        full_width=True
    )
    
    mo.vstack([
        mo.md("### 🎮 Interactive Numeric Playground"),
        integer_input,
        float_input,
        complex_input
    ])
    return integer_input, float_input, complex_input

@app.cell
def __(mo, integer_input, float_input, complex_input):
    try:
        # Process user inputs
        int_val = int(integer_input.value) if integer_input.value else 0
        float_val = float(float_input.value) if float_input.value else 0.0
        complex_val = complex(complex_input.value) if complex_input.value else 0+0j
        
        result_display = mo.md(f"""
        **Your Numbers:**
        - Integer: `{int_val}` (type: {type(int_val).__name__})
        - Float: `{float_val}` (type: {type(float_val).__name__})
        - Complex: `{complex_val}` (type: {type(complex_val).__name__})
        
        **Interesting Facts:**
        - Integer bit length: {int_val.bit_length()} bits
        - Float as integer ratio: {float_val.as_integer_ratio() if float_val else (0, 1)}
        - Complex real part: {complex_val.real}, imaginary part: {complex_val.imag}
        """)
        result_display
    except ValueError as e:
        mo.md(f"❌ **Error:** {str(e)} - Please check your input format!")
    return int_val, float_val, complex_val, result_display

@app.cell
def __(mo):
    mo.md("""
    ## ⚡ Python Expression Operators
    
    Let's explore Python's operator precedence and mixed-type operations through interactive examples.
    """)
    return

@app.cell
def __(mo):
    expression_input = mo.ui.text(
        value="2 ** 3 + 4 * 5",
        label="Enter a mathematical expression:",
        full_width=True
    )
    
    evaluate_button = mo.ui.button(label="Evaluate Expression")
    
    mo.vstack([
        mo.md("### 🧮 Expression Calculator"),
        mo.md("Try expressions like: `2 ** 3 + 4 * 5`, `(1 + 2) * 3`, or `10 / 3`"),
        expression_input,
        evaluate_button
    ])
    return expression_input, evaluate_button

@app.cell
def __(mo, expression_input, evaluate_button):
    if evaluate_button.value and expression_input.value:
        try:
            result = eval(expression_input.value)
            
            # Demonstrate operator precedence
            expr = expression_input.value
            feedback = mo.md(f"""
            ✅ **Expression:** `{expr}`
            
            **Result:** `{result}` (type: {type(result).__name__})
            
            **Operator Precedence Reminder:**
            - `**` (exponentiation) - highest precedence
            - `*`, `/`, `//`, `%` (multiplication, division)
            - `+`, `-` (addition, subtraction) - lowest precedence
            - Use parentheses `()` to override precedence!
            """)
            feedback
        except Exception as e:
            mo.md(f"❌ **Error:** {str(e)}")
    else:
        mo.md("*Enter an expression above and click Evaluate...*")
    return result, feedback

@app.cell
def __(mo):
    mo.md("""
    ## 🔄 Number Base Conversions
    
    Python supports multiple number bases. Let's explore conversions between decimal, binary, octal, and hexadecimal.
    """)
    return

@app.cell
def __(mo):
    base_number = mo.ui.number(
        value=255,
        label="Enter a decimal number:",
        start=0,
        stop=10000
    )
    
    base_selector = mo.ui.dropdown(
        options=["decimal", "binary", "octal", "hexadecimal"],
        value="decimal",
        label="Input base:"
    )
    
    mo.vstack([
        mo.md("### 🔢 Base Conversion Tool"),
        base_number,
        base_selector
    ])
    return base_number, base_selector

@app.cell
def __(mo, base_number, base_selector):
    if base_number.value is not None:
        num = int(base_number.value)
        
        # Convert to all bases
        decimal_form = str(num)
        binary_form = bin(num)
        octal_form = oct(num)
        hex_form = hex(num)
        
        conversion_display = mo.md(f"""
        **Number: {num} (input as {base_selector.value})**
        
        | Base | Representation | Python Literal |
        |------|----------------|----------------|
        | Decimal | {decimal_form} | `{decimal_form}` |
        | Binary | {binary_form[2:]} | `{binary_form}` |
        | Octal | {octal_form[2:]} | `{octal_form}` |
        | Hexadecimal | {hex_form[2:].upper()} | `{hex_form}` |
        
        **Verification:**
        - Binary → Decimal: `{int(binary_form, 2)}`
        - Octal → Decimal: `{int(octal_form, 8)}`  
        - Hex → Decimal: `{int(hex_form, 16)}`
        """)
        conversion_display
    else:
        mo.md("*Enter a number to see base conversions...*")
    return decimal_form, binary_form, octal_form, hex_form, conversion_display

@app.cell
def __(mo):
    mo.md("""
    ## 🔧 Bitwise Operations
    
    Explore how Python handles binary operations at the bit level.
    """)
    return

@app.cell
def __(mo):
    bit_num1 = mo.ui.number(value=5, label="First number:", start=0, stop=255)
    bit_num2 = mo.ui.number(value=3, label="Second number:", start=0, stop=255)
    
    mo.vstack([
        mo.md("### ⚙️ Bitwise Operations Explorer"),
        bit_num1,
        bit_num2
    ])
    return bit_num1, bit_num2

@app.cell
def __(mo, bit_num1, bit_num2):
    if bit_num1.value is not None and bit_num2.value is not None:
        a = int(bit_num1.value)
        b = int(bit_num2.value)
        
        bitwise_results = mo.md(f"""
        **Numbers:** {a} and {b}
        
        | Operation | Result | Binary Representation | Description |
        |-----------|--------|----------------------|-------------|
        | `{a} & {b}` | {a & b} | `{bin(a & b)}` | Bitwise AND |
        | `{a} \\| {b}` | {a | b} | `{bin(a | b)}` | Bitwise OR |
        | `{a} ^ {b}` | {a ^ b} | `{bin(a ^ b)}` | Bitwise XOR |
        | `~{a}` | {~a} | `{bin(~a & 0xFF)}` | Bitwise NOT (8-bit) |
        | `{a} << 2` | {a << 2} | `{bin(a << 2)}` | Left shift by 2 |
        | `{a} >> 1` | {a >> 1} | `{bin(a >> 1)}` | Right shift by 1 |
        
        **Binary Visualization:**
        - {a} = `{bin(a)[2:].zfill(8)}`
        - {b} = `{bin(b)[2:].zfill(8)}`
        """)
        bitwise_results
    else:
        mo.md("*Enter numbers to explore bitwise operations...*")
    return a, b, bitwise_results

@app.cell
def __(mo):
    mo.md("""
    ## 📊 Advanced Numeric Types
    
    Python provides specialized numeric types for enhanced precision and specific use cases.
    """)
    return

@app.cell
def __(mo):
    from decimal import Decimal, getcontext
    from fractions import Fraction
    
    precision_selector = mo.ui.slider(
        start=2,
        stop=10,
        value=4,
        label="Decimal precision:"
    )
    
    fraction_num = mo.ui.number(value=1, label="Fraction numerator:")
    fraction_den = mo.ui.number(value=3, label="Fraction denominator:")
    
    mo.vstack([
        mo.md("### 🎯 Precision Numeric Types"),
        precision_selector,
        fraction_num,
        fraction_den
    ])
    return Decimal, getcontext, Fraction, precision_selector, fraction_num, fraction_den

@app.cell
def __(mo, Decimal, getcontext, Fraction, precision_selector, fraction_num, fraction_den):
    # Set decimal precision
    getcontext().prec = precision_selector.value
    
    # Floating point precision issues
    float_calc = 0.1 + 0.1 + 0.1 - 0.3
    
    # Decimal precision
    decimal_calc = Decimal('0.1') + Decimal('0.1') + Decimal('0.1') - Decimal('0.3')
    
    # Fraction arithmetic
    if fraction_num.value and fraction_den.value:
        frac1 = Fraction(int(fraction_num.value), int(fraction_den.value))
        frac2 = Fraction(1, 4)
        frac_sum = frac1 + frac2
    else:
        frac1 = Fraction(1, 3)
        frac2 = Fraction(1, 4)
        frac_sum = frac1 + frac2
    
    precision_demo = mo.md(f"""
    **Precision Comparison: 0.1 + 0.1 + 0.1 - 0.3**
    
    | Type | Result | Exact? |
    |------|--------|--------|
    | Float | `{float_calc}` | ❌ No |
    | Decimal | `{decimal_calc}` | ✅ Yes |
    
    **Fraction Arithmetic: {frac1} + {frac2}**
    - Result: `{frac_sum}` = {float(frac_sum):.6f}
    - Exact rational representation maintained!
    
    **Current decimal precision:** {precision_selector.value} digits
    **Division example:** 1 ÷ 7 = `{Decimal(1) / Decimal(7)}`
    """)
    precision_demo
    return float_calc, decimal_calc, frac1, frac2, frac_sum, precision_demo

@app.cell
def __(mo):
    mo.md("""
    ## 📁 Set Operations
    
    Sets provide mathematical set theory operations and are useful for data analysis.
    """)
    return

@app.cell
def __(mo):
    set1_input = mo.ui.text(
        value="1,2,3,4,5",
        label="Set 1 (comma-separated):",
        full_width=True
    )
    
    set2_input = mo.ui.text(
        value="4,5,6,7,8",
        label="Set 2 (comma-separated):",
        full_width=True
    )
    
    mo.vstack([
        mo.md("### 🔗 Set Operations Explorer"),
        set1_input,
        set2_input
    ])
    return set1_input, set2_input

@app.cell
def __(mo, set1_input, set2_input):
    try:
        # Parse input sets
        set1 = set(map(int, set1_input.value.split(','))) if set1_input.value else set()
        set2 = set(map(int, set2_input.value.split(','))) if set2_input.value else set()
        
        set_operations = mo.md(f"""
        **Set A:** `{set1}`
        **Set B:** `{set2}`
        
        | Operation | Python | Result | Description |
        |-----------|---------|--------|-------------|
        | Union | `A \\| B` | `{set1 | set2}` | All elements in either set |
        | Intersection | `A & B` | `{set1 & set2}` | Elements in both sets |
        | Difference | `A - B` | `{set1 - set2}` | Elements in A but not B |
        | Symmetric Diff | `A ^ B` | `{set1 ^ set2}` | Elements in either but not both |
        | Subset | `A <= B` | `{set1 <= set2}` | Is A a subset of B? |
        | Superset | `A >= B` | `{set1 >= set2}` | Is A a superset of B? |
        
        **Set Comprehension Example:**
        `{{x**2 for x in A}}` = `{set(x**2 for x in set1)}`
        """)
        set_operations
    except ValueError:
        mo.md("❌ Please enter comma-separated integers (e.g., '1,2,3,4')")
    return set1, set2, set_operations

@app.cell
def __(mo):
    mo.md("""
    ## 🧪 Interactive Exercises
    
    Test your understanding with these hands-on challenges!
    """)
    return

@app.cell
def __(mo):
    exercise_selector = mo.ui.dropdown(
        options=[
            "Operator Precedence Challenge",
            "Base Conversion Quiz", 
            "Precision Comparison",
            "Set Theory Problem"
        ],
        value="Operator Precedence Challenge",
        label="Choose an exercise:"
    )
    
    mo.vstack([
        mo.md("### 🏋️ Interactive Exercises"),
        exercise_selector
    ])
    return exercise_selector,

@app.cell
def __(mo, exercise_selector):
    if exercise_selector.value == "Operator Precedence Challenge":
        exercise_content = mo.md("""
        **Challenge:** Predict the result of `2 + 3 * 4 ** 2`
        
        Think step by step:
        1. What operation has the highest precedence?
        2. What's the order of evaluation?
        3. What's the final result?
        """)
        
        answer_input = mo.ui.number(label="Your answer:")
        check_button = mo.ui.button(label="Check Answer")
        
        mo.vstack([exercise_content, answer_input, check_button])
        
    elif exercise_selector.value == "Base Conversion Quiz":
        exercise_content = mo.md("""
        **Challenge:** Convert binary `1010` to decimal
        
        Binary place values: 8, 4, 2, 1
        """)
        
        answer_input = mo.ui.number(label="Decimal equivalent:")
        check_button = mo.ui.button(label="Check Answer")
        
        mo.vstack([exercise_content, answer_input, check_button])
        
    else:
        mo.md("More exercises coming soon! Try the other options.")
        
    return exercise_content, answer_input, check_button

@app.cell
def __(mo, exercise_selector, answer_input, check_button):
    if check_button.value and answer_input.value is not None:
        if exercise_selector.value == "Operator Precedence Challenge":
            correct_answer = 2 + 3 * 4 ** 2  # 2 + 3 * 16 = 2 + 48 = 50
            user_answer = int(answer_input.value)
            
            if user_answer == correct_answer:
                feedback = mo.md("""
                ✅ **Correct!** The answer is 50.
                
                **Step-by-step:**
                1. `4 ** 2` = 16 (exponentiation first)
                2. `3 * 16` = 48 (multiplication second)  
                3. `2 + 48` = 50 (addition last)
                """)
            else:
                feedback = mo.md(f"""
                ❌ **Incorrect.** You answered {user_answer}, but the correct answer is {correct_answer}.
                
                Remember: `**` has higher precedence than `*`, which has higher precedence than `+`.
                """)
                
        elif exercise_selector.value == "Base Conversion Quiz":
            correct_answer = int('1010', 2)  # Binary to decimal
            user_answer = int(answer_input.value)
            
            if user_answer == correct_answer:
                feedback = mo.md("""
                ✅ **Correct!** Binary 1010 = Decimal 10.
                
                **Calculation:** 1×8 + 0×4 + 1×2 + 0×1 = 8 + 0 + 2 + 0 = 10
                """)
            else:
                feedback = mo.md(f"""
                ❌ **Incorrect.** You answered {user_answer}, but the correct answer is {correct_answer}.
                
                **Hint:** Add up the place values where you see a '1'.
                """)
        else:
            feedback = mo.md("Exercise not implemented yet.")
            
        feedback
    else:
        mo.md("*Complete the exercise above and click Check Answer...*")
    return feedback,

@app.cell
def __(mo):
    mo.md("""
    ## 🎯 Summary & Next Steps
    
    Congratulations! You've completed this interactive exploration of Python numbers and expressions.
    
    ### Key Concepts Mastered
    - [x] **Numeric Types**: Integers, floats, complex numbers
    - [x] **Operators**: Arithmetic, bitwise, and comparison operators  
    - [x] **Precision**: Decimal and Fraction types for exact arithmetic
    - [x] **Base Conversions**: Binary, octal, and hexadecimal representations
    - [x] **Set Operations**: Mathematical set theory in Python
    - [x] **Interactive Problem Solving**: Hands-on numeric programming
    
    ### What You've Accomplished
    ✅ Explored Python's rich numeric ecosystem interactively
    ✅ Experimented with operator precedence and type conversions
    ✅ Mastered base conversions and bitwise operations
    ✅ Applied advanced numeric types for precision computing
    ✅ Solved practical problems using set operations
    
    ### Next Steps
    1. **Practice More**: Try creating your own numeric expressions and test edge cases
    2. **Explore Extensions**: Look into NumPy, SciPy, and pandas for advanced numeric computing
    3. **Build Projects**: Apply these concepts in calculator apps, data analysis, or scientific computing
    4. **Continue Learning**: Move on to the next chapter about strings and text processing
    
    ### Additional Resources
    - [Python Numeric Types Documentation](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)
    - [Math Module Reference](https://docs.python.org/3/library/math.html)
    - [Decimal Module Guide](https://docs.python.org/3/library/decimal.html)
    
    **Happy coding! 🐍✨**
    """)
    return

if __name__ == "__main__":
    app.run()