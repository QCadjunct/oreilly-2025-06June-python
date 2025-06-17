import marimo

__generated_with = "0.13.15"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo

    app = mo.App(width="medium")
    __generated_with = "0.13.15"
    return (mo,)


@app.cell
def _(complex_input):
    int_val = 12 #int(integer_input.value) if integer_input.value else 0
    float_val = 36.02 #float(float_input.value) if float_input.value else 0.0
    complex_val = complex(complex_input.value) if complex_input.value else 0+0j

    return complex_val, float_val, int_val


@app.cell
def _(mo):
    mo.md(
        """
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
    """
    )
    return


@app.cell
def _(mo):
    mo.md(
        """
    ## 🔢 Numeric Object Basics

    Python supports several numeric types. Let's explore the most fundamental ones:

    - **Integer objects**: Whole numbers with unlimited precision
    - **Floating-point objects**: Numbers with decimal points
    - **Complex number objects**: Numbers with real and imaginary parts
    """
    )
    return


@app.cell
def _(mo):
    # Interactive numeric literals playground
    int_input = mo.ui.text(
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
        int_input,
        float_input,
        complex_input
    ])
    return (complex_input,)


@app.cell
def _():
    return


@app.cell
def _(complex_val, float_val, int_val, mo):
    result_display = mo.md(f"""
    ## **Your Numbers:**

        - Integer: `{int_val}` (type: {type(int_val).__name__})  
        - Float: `{float_val}` (type: {type(float_val).__name__})  
        - Complex: `{complex_val}` (type: {type(complex_val).__name__})  

    ## **Interesting Facts:**
        - Integer bit length: {int_val.bit_length()} bits  
        - Float as integer ratio: {float_val.as_integer_ratio() if float_val else (0, 1)}  
        - Complex real part: {complex_val.real}, imaginary part: {complex_val.imag}  
    """)
    result_display

    return


@app.cell
def _(mo):
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
    return (expression_input,)


@app.cell
def _(expression_input, mo):
    # if evaluate_button.value and expression_input.value:
    #    try:
    result = eval(expression_input.value)

    # Demonstrate operator precedence
    expr = expression_input.value
    feedback = mo.md(f"""
    ✅ **Expression:** `{expr}`

    ### **Result:** `{result}` (type: {type(result).__name__})

    #### **Operator Precedence Reminder:**
        - `**` (exponentiation) - highest precedence  
        - `*`, `/`, `//`, `%` (multiplication, division)  
        - `+`, `-` (addition, subtraction) - lowest precedence  
        - Use parentheses `()` to override precedence!  
    """)
    feedback
    #    except Exception as e:
    #        mo.md(f"❌ **Error:** {str(e)}")
    #else:
    #    mo.md("*Enter an expression above and click Evaluate...*")
    return


@app.cell
def _(mo):
    base_number = mo.ui.number(
        value=255, label="Enter a decimal number:", start=0, stop=10000
    )

    base_selector = mo.ui.dropdown(
        options=["decimal", "binary", "octal", "hexadecimal"],
        value="decimal",
        label="Input base:",
    )

    mo.vstack([mo.md("### 🔢 Base Conversion Tool"), base_number, base_selector])
    return base_number, base_selector


@app.cell
def _(base_number, base_selector, mo):
    num = int(base_number.value)
    # Convert to all bases
    decimal_form = str(num)
    binary_form = bin(num)
    octal_form = oct(num)
    hex_form = hex(num)

    conversion_display = mo.md(f"""
    ## **Number: {num} (input as {base_selector.value})**  

    | Base        | Representation         | Python Literal   |
    |-------------|------------------------|------------------|
    | Decimal     | {decimal_form}         | `{decimal_form}` |
    | Binary      | {binary_form[2:]}      | `{binary_form}`  |
    | Octal       | {octal_form[2:]}       | `{octal_form}`   |
    | Hexadecimal | {hex_form[2:].upper()} | `{hex_form}`     |

    **Verification:**
    - Binary → Decimal: `{int(binary_form, 2)}`  
    - Octal → Decimal: `{int(octal_form, 8)}`  
    - Hex → Decimal: `{int(hex_form, 16)}`  
    """)
    conversion_display

    return


@app.cell
def _(mo):
    mo.md(
        """
    ## 🔧 Bitwise Operations

    Explore how Python handles binary operations at the bit level.
    """
    )
    return


@app.cell
def _(mo):
    bit_num1 = mo.ui.number(value=5, label="First number:", start=0, stop=255)
    bit_num2 = mo.ui.number(value=3, label="Second number:", start=0, stop=255)

    mo.vstack([
        mo.md("### ⚙️ Bitwise Operations Explorer"),
        bit_num1,
        bit_num2
    ])
    return bit_num1, bit_num2


@app.cell(hide_code=True)
def _(bit_num1, bit_num2, mo):
    # Simple debug test - try this first
    def __():
        return mo.md(f"Debug: bit_num1 = {bit_num1.value}, bit_num2 = {bit_num2.value}")

    # If the debug works, then try this full version:
    def __():
        if bit_num1.value is not None and bit_num2.value is not None:
            a = int(bit_num1.value)
            b = int(bit_num2.value)

            and_result = a & b
            or_result = a | b
            xor_result = a ^ b

            return mo.md(f"""
    ### Bitwise Operations: {a} and {b}
    # 
    # - **AND:** `{a} & {b}` = **{and_result}** (`{and_result:08b}`)
    # - **OR:** `{a} | {b}` = **{or_result}** (`{or_result:08b}`)
    # - **XOR:** `{a} ^ {b}` = **{xor_result}** (`{xor_result:08b}`)
    # """)
        else:
            return mo.md("*Waiting for values...*")

    # Alternative: No function wrapper (if functions are not working)
    mo.md(f"Values: {bit_num1.value} and {bit_num2.value}")
    return


@app.cell
def _(bit_num1, bit_num2, mo):
    # Copy this EXACT code into a new cell in Marimo:

    a = int(bit_num1.value)
    b = int(bit_num2.value)
    and_result = a & b
    or_result = a | b
    xor_result = a ^ b

    mo.md(f"""
    ## Bitwise Operations: {a} and {b}

    - **AND:** `{a} & {b}` = **{and_result}** (`{and_result:08b}`)
    - **OR:** `{a} | {b}` = **{or_result}** (`{or_result:08b}`)  
    - **XOR:** `{a} ^ {b}` = **{xor_result}** (`{xor_result:08b}`)

    ### Binary:
    - **{a}** = `{a:08b}`
    - **{b}** = `{b:08b}`
    """)
    return


@app.cell
def _(mo):
    mo.md(
        """
    ## 🔄 Number Base Conversions

    Python supports multiple number bases. Let's explore conversions 
    between decimal, binary, octal, and hexadecimal.
    """
    )
    return


@app.cell
def _():
    import marimo
    print(f"Marimo version: {marimo.__version__}")
    return


@app.cell
def _():
    def __():
        return "Hello World"  # Simplest possible test
    return


if __name__ == "__main__":
    app.run()
