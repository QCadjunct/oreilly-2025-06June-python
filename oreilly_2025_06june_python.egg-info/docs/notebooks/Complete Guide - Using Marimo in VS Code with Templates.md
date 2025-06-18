# Complete Guide: Using Marimo in VS Code with Templates

## 🚀 Quick Start Instructions

### Method 1: Create New Notebook with Template (Recommended)

1. **Open VS Code** in your project directory
2. **Create new Python file**:
   - `Ctrl+N` (new file)
   - Save as `my_notebook.py`
3. **Use your template**:
   - Type: `marimo-new`
   - Press: `Tab`
   - Template appears with placeholders!
4. **Fill in the template**:
   - Tab through: Title → Description → Code
   - Customize as needed
5. **Start Marimo**:
   - Right-click in editor → "Open with Marimo"
   - OR Command Palette (`Ctrl+Shift+P`) → "Marimo: Open"
   - OR Terminal: `uv run marimo edit my_notebook.py`

### Method 2: Start from Scratch

1. **Create notebook via terminal:** 

   ```bash
   uv run marimo create my_notebook.py
   ```

2. **Open in VS Code**:
   - File appears in explorer
   - Right-click → "Open with Marimo"

### Method 3: Open Existing Notebook

1. **Open notebook file** in VS Code
2. **Start Marimo**:
   - Right-click → "Open with Marimo"
   - OR `Ctrl+Shift+P` → "Marimo: Open"

## 📝 Template Usage Details

### When you type `marimo-new` + Tab:

```python
import marimo as mo
__generated_with = "0.13.15"
app = mo.App(width="medium")

@app.cell
def __():
    import marimo as mo
    return (mo,)

@app.cell 
def __():
    mo.md("""
    # [Cursor here - type your title]
    
    [Tab to description area]
    """)

@app.cell
def __():
    [Tab to code area]
    return

if __name__ == "__main__":
    app.run()
```

### **Tab Navigation:**

- **First Tab**: Edit notebook title
- **Second Tab**: Edit description  
- **Third Tab**: Start coding

## 🔧 Marimo Commands in VS Code

| Action | Method |
|--------|--------|
| **Create notebook** | `uv run marimo create filename.py` |
| **Open notebook** | Right-click file → "Open with Marimo" |
| **Edit notebook** | `Ctrl+Shift+P` → "Marimo: Open" |
| **Run as app** | `uv run marimo run filename.py` |
| **Convert Jupyter** | `uv run marimo convert notebook.ipynb` |

## 🖥️ VS Code Integration Features

### **Available Commands (`Ctrl+Shift+P`):**

- **Marimo: Open** - Start editing current file
- **Marimo: Run** - Run notebook as app
- **Marimo: Export** - Export to HTML/Markdown
- **Marimo: Show Diagnostics** - Debug issues

### **Right-click Context Menu:**

- **Open with Marimo** - Launch in Marimo editor
- **Run Marimo App** - Serve as web app

## 🌐 Marimo Interface

**When Marimo opens, you'll see:**

- **Browser window** (embedded in VS Code or separate)
- **Reactive cells** that auto-update
- **UI elements** (sliders, buttons, etc.)
- **Real-time outputs**

## ⚙️ Your Configuration Benefits

**Your setup provides:**

- ✅ **Latest Marimo** (0.13.15) via UV
- ✅ **Project isolation** via pyproject.toml
- ✅ **Fast templates** via snippets
- ✅ **Integrated workflow** in VS Code
- ✅ **Consistent versions** across team

## 🔄 Typical Workflow

1. **Start project**: `uv sync` (install dependencies)
2. **Create notebook**: Type `marimo-new` + Tab
3. **Fill template**: Tab through placeholders
4. **Launch Marimo**: Right-click → "Open with Marimo"
5. **Develop**: Add cells, create UI elements
6. **Save**: Auto-saves as Python file
7. **Share**: Commit .py file to git
8. **Deploy**: `uv run marimo run notebook.py`

## 🚨 Troubleshooting

**If Marimo doesn't start:**

- Check terminal: `uv run marimo --version`
- Verify VS Code settings point to correct Python
- Try: `Ctrl+Shift+P` → "Marimo: Show Diagnostics"

**If template doesn't work:**

- Verify `python.json` snippet is saved
- Try typing `marimo` to see available snippets
- Check file is saved as `.py` extension

**If wrong Python version:**

- Ensure VS Code uses workspace Python: `${workspaceFolder}/.venv/Scripts/python.exe`

## 🎯 Pro Tips

- **Save frequently** - Marimo auto-saves but VS Code might not
- **Use direct execution** for simple cells (your KISS (Keep It Simple and Standard) approach!)
- **Keep cells small** - Better for reactivity
- **Name your notebooks descriptively** - They're just Python files
- **Use version control** - Track changes with git