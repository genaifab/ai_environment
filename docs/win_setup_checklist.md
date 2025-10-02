# Windows Setup Checklist (Stage 1)

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
   - Command:
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
