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
def _():
    return


if __name__ == "__main__":
    app.run()
