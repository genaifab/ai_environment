# AI Environment Setup Checklist (Stage 1)

This checklist provides side-by-side instructions for setting up your AI environment on **Mac** and **Windows**.

---

## 🖥️ Mac Setup

1. **Install Homebrew**
   ```bash
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
   ```

2. **Install Xcode Command Line Tools (for Git)**
   ```bash
   xcode-select --install
   ```

3. **Install VS Code**
   - Download from [https://code.visualstudio.com/](https://code.visualstudio.com/) and drag into Applications.

4. **Install uv via Homebrew**
   ```bash
   brew install uv
   ```

5. **Terminal**
   - Already available on macOS (zsh by default).

---

## 🖥️ Windows Setup

1. **Install Winget (Windows Package Manager)**
   - Verify:
     ```powershell
     winget --version
     ```
   - If missing, install via [Microsoft Store](https://learn.microsoft.com/en-us/windows/package-manager/winget/).

2. **Install Git for Windows**
   - Download from [https://git-scm.com/download/win](https://git-scm.com/download/win).

3. **Install VS Code**
   - Download `.exe` from [https://code.visualstudio.com/](https://code.visualstudio.com/).

4. **Install uv via Winget**
   ```powershell
   winget install --id=astral-sh.uv
   ```
   - Alternative: Download installer from [uv releases](https://github.com/astral-sh/uv/releases).

5. **Terminal**
   - Use PowerShell (preinstalled).
   - Optionally install Windows Terminal:
     ```powershell
     winget install --id=Microsoft.WindowsTerminal
     ```

---

✅ After completing these steps, you will have:
- A package manager (Homebrew or Winget)
- Git installed
- VS Code editor ready
- uv installed for managing environments
- A terminal to run commands
