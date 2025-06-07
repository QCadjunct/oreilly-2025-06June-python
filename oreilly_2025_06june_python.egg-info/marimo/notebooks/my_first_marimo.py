import marimo

__generated_with = "0.13.15"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo

    return


@app.cell
def _():
    import matplotlib.pyplot as plt
    import matplotlib.gridspec as gridspec
    import numpy as np
    return gridspec, np, plt


@app.cell
def _(gridspec, np, plt):
    def create_advanced_subplots():
        # Create figure with GridSpec
        fig = plt.figure(figsize=(12, 8))
        gs = gridspec.GridSpec(3, 3)

        # Spanning multiple cells
        ax1 = fig.add_subplot(gs[0, :])  # Span all columns
        ax2 = fig.add_subplot(gs[1:, 0:2])  # Span 2 rows, 2 columns
        ax3 = fig.add_subplot(gs[1:, 2])  # Span 2 rows, 1 column

        # Add sample plots
        x = np.linspace(0, 10, 100)
        ax1.plot(x, np.sin(x))
        ax2.scatter(x[::5], np.cos(x[::5]))
        ax3.hist(np.random.randn(100))

        plt.tight_layout()

        return ax1, ax2, ax3

    create_advanced_subplots()
    return


@app.cell
def _(np, plt):
    def create_3d_surface():
        # Create data for 3D plot
        x = np.linspace(-2, 2, 30)
        y = np.linspace(-2, 2, 30)
        X, Y = np.meshgrid(x, y)
        Z = np.sin(np.sqrt(X**2 + Y**2))

        # Create 3D plot
        fig = plt.figure(figsize=(8, 6))
        ax = fig.add_subplot(111, projection='3d')
        surf = ax.plot_surface(X, Y, Z, cmap='viridis')

        # Add colorbar
        fig.colorbar(surf)

        return ax

    create_3d_surface()
    return


if __name__ == "__main__":
    app.run()
