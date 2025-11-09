# Script Copyright and Metadata Templates

This directory contains templates for ensuring consistent copyright notices and metadata across all scripts in the Rongorongo Decipherment Project.

## Copyright Information

**Copyright Holder:** Lackadaisical Security  
**Year:** 2025  
**Website:** https://lackadaisical-security.com  
**Support Email:** support@lackadaisical-security.com  
**GitHub:** https://github.com/Lackadaisical-Security/rongorongo-deciphered-public  

**License:** Creative Commons Attribution-NonCommercial 4.0 International (CC BY-NC 4.0)  
**License URL:** https://creativecommons.org/licenses/by-nc/4.0/

## Templates

### 1. SCRIPT_METADATA_TEMPLATE.json
Complete JSON metadata template for documenting scripts. This should be created as a separate `[script_name]_metadata.json` file alongside each major script.

**Usage:**
1. Copy `SCRIPT_METADATA_TEMPLATE.json` to `[your_script_name]_metadata.json`
2. Fill in all bracketed placeholders `[like this]` with actual values
3. Remove any sections that don't apply to your script
4. Keep the metadata file updated as the script evolves

**Sections:**
- **metadata**: Core information about the script (title, version, copyright, license)
- **usage**: How to run the script, arguments, examples
- **technical_details**: Functions, algorithms, performance characteristics
- **validation**: Input/output validation, error handling
- **changelog**: Version history
- **related_scripts**: Dependencies and relationships
- **notes**: Additional important information

### 2. PYTHON_COPYRIGHT_TEMPLATE.py
Python script header template with full copyright notice and metadata structure.

**Usage:**
1. Copy the header section (lines 1-87) from this template
2. Paste at the beginning of your Python script
3. Replace all bracketed placeholders `[like this]` with actual values
4. Update the `SCRIPT_METADATA` dictionary with your script's information
5. Add your script logic after the "Main Script Code Below" separator

**Key Elements:**
- Shebang and encoding declaration
- Copyright notice and license information
- Attribution requirements
- Script description and usage instructions
- Module-level metadata constants (`__version__`, `__author__`, etc.)
- `SCRIPT_METADATA` dictionary for runtime access

## Applying Copyright to Existing Scripts

To add copyright headers to existing scripts:

### For Python Scripts:

1. **Backup the script** (recommended)
2. **Copy header** from `PYTHON_COPYRIGHT_TEMPLATE.py` (lines 1-70)
3. **Insert at top** of your existing script
4. **Fill in placeholders:**
   - `[Script Title/Name]` - Replace with script's actual name
   - `[Brief one-line description]` - Add concise description
   - `[Detailed multi-line description...]` - Expand on purpose
   - `[YYYY-MM-DD]` - Add creation/modification dates
   - `[X.Y.Z]` - Add version number
   - `[script_name].py` - Replace with actual filename
   - `[arguments]` - List actual command-line arguments
   - `[List input files...]` - Document input files
   - `[List output files...]` - Document output files
   - `[List Python packages...]` - List dependencies

5. **Update metadata dictionary:**
   ```python
   SCRIPT_METADATA = {
       "name": "Your Script Name",
       "version": "1.0.0",
       "description": "What it does",
       # ... etc
   }
   ```

6. **Test the script** to ensure it still works

### Example: Adding Copyright to validate_data.py

Before:
```python
#!/usr/bin/env python3
"""
Validation script for Phase 1-20 data
Ensures all bank files are properly formatted and internally consistent
"""

import json
import sys
```

After:
```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Rongorongo Data Validation Script
Validates Phase 1-20 data for proper formatting and consistency

Copyright © 2025 Lackadaisical Security
Website: https://lackadaisical-security.com
Support: support@lackadaisical-security.com
GitHub: https://github.com/Lackadaisical-Security.com

Licensed under Creative Commons Attribution-NonCommercial 4.0 International (CC BY-NC 4.0)
https://creativecommons.org/licenses/by-nc/4.0/

[... rest of copyright header ...]
"""

import json
import sys
```

## Minimal Copyright Header

If the full header is too verbose for your script, use this minimal version:

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
[Script Title]

Copyright © 2025 Lackadaisical Security
Website: https://lackadaisical-security.com
Licensed under CC BY-NC 4.0: https://creativecommons.org/licenses/by-nc/4.0/
"""

__version__ = "1.0.0"
__author__ = "Lackadaisical Security"
__copyright__ = "Copyright © 2025 Lackadaisical Security"
__license__ = "CC BY-NC 4.0"
```

## Requirements

### Attribution Requirements
- Lackadaisical Security must be credited in any use or derivative work
- Copyright notice must be retained in all copies
- License information must be included or referenced

### Usage Restrictions
- **Non-commercial use only** unless explicit permission granted
- Commercial licensing inquiries: support@lackadaisical-security.com
- Forked work must include original copyright notice

### Derivative Works
- Must include attribution to Lackadaisical Security
- Must retain copyright notices
- Must include or link to original license (CC BY-NC 4.0)
- Must clearly indicate what modifications were made

## Batch Application Script

To apply copyright headers to all scripts at once, you can create a helper script:

```python
#!/usr/bin/env python3
"""Apply copyright headers to all Python scripts in directory"""

import os
from pathlib import Path

SCRIPTS_DIR = Path(__file__).parent
TEMPLATE_HEADER = """#!/usr/bin/env python3
# -*- coding: utf-8 -*-
\"\"\"
{title}

Copyright © 2025 Lackadaisical Security
Website: https://lackadaisical-security.com
Licensed under CC BY-NC 4.0: https://creativecommons.org/licenses/by-nc/4.0/
\"\"\"

__version__ = "1.0.0"
__author__ = "Lackadaisical Security"
__copyright__ = "Copyright © 2025 Lackadaisical Security"
__license__ = "CC BY-NC 4.0"

"""

def add_copyright_to_script(script_path):
    \"\"\"Add minimal copyright header to a script\"\"\"
    with open(script_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Extract title from first docstring or filename
    title = script_path.stem.replace('_', ' ').title()
    
    # Skip if copyright already present
    if 'Copyright © 2025 Lackadaisical Security' in content:
        print(f"Skipping {script_path.name} - copyright already present")
        return
    
    # Remove old shebang and encoding if present
    lines = content.split('\n')
    start_idx = 0
    if lines[0].startswith('#!'):
        start_idx = 1
    if start_idx < len(lines) and lines[start_idx].startswith('# -*-'):
        start_idx += 1
    
    new_content = TEMPLATE_HEADER.format(title=title) + '\n'.join(lines[start_idx:])
    
    # Write back
    with open(script_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print(f"Updated {script_path.name}")

def main():
    for script in SCRIPTS_DIR.glob('*.py'):
        if script.name == 'apply_copyright.py':  # Skip self
            continue
        if script.name.startswith('PYTHON_COPYRIGHT_TEMPLATE'):  # Skip template
            continue
        add_copyright_to_script(script)

if __name__ == '__main__':
    main()
```

## Questions?

For questions about licensing, copyright, or commercial use:
- Email: support@lackadaisical-security.com
- Website: https://lackadaisical-security.com

## Version History

- **v1.0** (2025-01-09): Initial template creation
  - JSON metadata template
  - Python copyright header template
  - Documentation and usage guide
