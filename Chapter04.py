import marimo

__generated_with = "0.13.15"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo

    __generated_with = "0.13.15"
    app = mo.App(width="medium")
    return (mo,)


@app.cell
def _():
    def __():
        import marimo as mo
        return mo,
    return


@app.cell
def _(mo):
    def __():
        return mo.md("""
        ## 🔢 Numeric Object Basics

        Python supports several numeric types. Let's explore the most fundamental ones:

        - Integer objects: Whole numbers with unlimited precision
        - Floating-point objects: Numbers with decimal points
        - Complex number objects: Numbers with real and imaginary parts
        """)
    __()
    return


@app.cell
def _(mo):
    def intro_cell():
        return mo.md("""
        ## 🔢 Numeric Object Basics
    
        Python supports several numeric types. Let's explore the most fundamental ones:
    
        - Integer objects: Whole numbers with unlimited precision
        - Floating-point objects: Numbers with decimal points
        - Complex number objects: Numbers with real and imaginary parts
        """)
    intro_cell()
    return (intro_cell,)


@app.cell
def _(intro_cell):
    intro_cell()
    return


@app.cell
def _(mo):
    def numbers_and_expressions():
        return mo.md("""
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
    

    return (numbers_and_expressions,)


@app.cell
def _(numbers_and_expressions):
    numbers_and_expressions()
    return


if __name__ == "__main__":
    app.run()
