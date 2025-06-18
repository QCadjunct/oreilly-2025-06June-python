# 🚀 Marimo + VS Code + UV Quick Start Guide

## ⚙️ One-Time Setup (5 minutes)

### 1. Install & Configure VS Code Extension

```bash
# Install Marimo VS Code extension from marketplace
# Search: "marimo" by marimo-team
```

### 2. Update VS Code Workspace Settings

**Edit `.vscode/settings.json`** - Add these 3 lines:

```json
{
    // ... your existing settings ...
    "marimo.pythonPath": "${workspaceFolder}/.venv/Scripts/python.exe",
    "marimo.marimoPath": "uv run marimo", 
    "marimo.sandbox": false
}
```

### 3. Create Python Code Snippet

**Steps:**

1. `Ctrl+Shift+P` → "Configure User Snippets" → "python.json"
2. **Add this snippet:**

```json
{
    "Marimo Notebook Template": {
        "prefix": "marimo-new",
        "body": [
            "import marimo as mo",
            "__generated_with = \"0.13.15\"",
            "app = mo.App(width=\"medium\")",
            "",
            "@app.cell",
            "def __():",
            "    import marimo as mo",
            "    return (mo,)",
            "",
            "@app.cell", 
            "def __():",
            "    mo.md(\"\"\"",
            "    # ${1:Notebook Title}",
            "    ",
            "    ${2:Description}",
            "    \"\"\")",
            "",
            "@app.cell",
            "def __():",
            "    ${3:# Your code here}",
            "    return",
            "",
            "if __name__ == \"__main__\":",
            "    app.run()"
        ],
        "description": "Create new Marimo notebook with current version"
    }
}
```

### 4. Verify Your Project Setup

**Check you have:**

- ✅ `pyproject.toml` with `marimo>=0.13.15`
- ✅ UV environment: `uv sync`
- ✅ Marimo installed: `uv run marimo --version`

---

## 🚀 Quick Start (30 seconds)

### Create & Launch Notebook:

1. **Open VS Code** in your project directory
2. **Create new file**: `Ctrl+N`, save as `test.py`
3. **Use template**: Type `marimo-new` → Press `Tab`
4. **Fill placeholders**: Tab through Title → Description → Code
5. **Launch Marimo**: Right-click → "Open with Marimo"

**That's it!** 🎉 Marimo opens with your template!

---

## 📋 What You Get

### Perfect Template Structure:

```python
import marimo as mo
__generated_with = "0.13.15"  # ✅ Current version
app = mo.App(width="medium")

@app.cell
def __():
    import marimo as mo
    return (mo,)

@app.cell 
def __():
    mo.md("""
    # Your Notebook Title    # ← First tab stop
    
    Your description here    # ← Second tab stop
    """)

@app.cell
def __():
    # Your code here          # ← Third tab stop
    return

if __name__ == "__main__":
    app.run()
```

### **Tab Navigation:**

- **Tab 1**: Edit title
- **Tab 2**: Edit description  
- **Tab 3**: Start coding

---

## ⚡ Key Commands

| Action | Command |
|--------|---------|
| **Create template** | `marimo-new` + `Tab` |
| **Open in Marimo** | Right-click → "Open with Marimo" |
| **Command palette** | `Ctrl+Shift+P` → "Marimo: Open" |
| **Terminal launch** | `uv run marimo edit filename.py` |
| **Run as app** | `uv run marimo run filename.py` |

---

## 🎯 Pro Tips

### **Your "Keep It Simple, and Standard" Approach:**

- **Direct execution works**: `mo.md("Hello")` 
- **Functions can be tricky**: Use when needed, fallback to direct
- **KISS principle**: Simple code that works > complex code that doesn't

### **Best Practices:**

- ✅ **Keep cells small** - Better reactivity
- ✅ **Use direct execution** for simple content
- ✅ **Save frequently** - VS Code + Marimo sync
- ✅ **Name files descriptively** - They're just Python files
- ✅ **Commit .py files** - Perfect for Git

---

## 🔧 Your Perfect Setup Benefits

- ✅ **Latest Marimo** (0.13.15) via UV
- ✅ **Project isolation** via pyproject.toml  
- ✅ **Fast templates** via VS Code snippets
- ✅ **Integrated workflow** in VS Code
- ✅ **Version consistency** across team
- ✅ **No more function wrapper issues**
- ✅ **Elegant KISS approach** that actually works

---

## 🚨 Quick Troubleshooting

**Template not working?**

- Check snippet saved in `python.json`
- File must be `.py` extension
- Try `Ctrl+Space` to see available snippets

**Marimo not starting?**

- Verify: `uv run marimo --version`
- Check VS Code settings point to `.venv`
- Try: `Ctrl+Shift+P` → "Marimo: Show Diagnostics"

**Functions not executing?**

- Use your proven direct execution approach
- Remember: `mo.md("content")` works better than `def __(): return mo.md("content")`

---

## 🎉 Success!

**You now have:**

- **Professional setup** with UV + Marimo + VS Code
- **Instant templates** with correct versions
- **Proven workflow** that just works
- **Elegant approach** following KISS principles

**Ready to create amazing reactive notebooks!** 🚀
