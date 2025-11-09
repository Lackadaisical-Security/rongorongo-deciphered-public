#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Complete Phases 3 6 7

Copyright © 2025 Lackadaisical Security
Website: https://lackadaisical-security.com
Support: support@lackadaisical-security.com
GitHub: https://github.com/Lackadaisical-Security/rongorongo-deciphered-public

Licensed under Creative Commons Attribution-NonCommercial 4.0 International (CC BY-NC 4.0)
https://creativecommons.org/licenses/by-nc/4.0/

Master script to complete Phases 3, 6, and 7
Runs all three completion scripts in sequence

Author: Lackadaisical Security (The Operator)
Created: 2025-10-30
Modified: 2025-10-30
Version: 1.0.0
"""

__version__ = "1.0.0"
__author__ = "Lackadaisical Security"
__copyright__ = "Copyright © 2025 Lackadaisical Security"
__license__ = "CC BY-NC 4.0"


import sys
import subprocess
from datetime import datetime

def run_script(script_name, description):
    """Run a completion script and report results"""
    print(f'\n{"=" * 60}')
    print(f'{description}')
    print(f'{"=" * 60}')
    
    try:
        result = subprocess.run(
            ['python3', f'scripts/{script_name}'],
            check=True,
            capture_output=True,
            text=True
        )
        print(result.stdout)
        if result.stderr:
            print('STDERR:', result.stderr)
        return True
    except subprocess.CalledProcessError as e:
        print(f'ERROR running {script_name}:')
        print(e.stdout)
        print(e.stderr)
        return False

def main():
    print('=' * 60)
    print('COMPLETING PHASES 3, 6, AND 7')
    print('=' * 60)
    print(f'Started: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}')
    
    success_count = 0
    total_count = 3
    
    # Run Phase 3 completion
    if run_script('complete_phase_3_data.py', 'PHASE 3: Orientation & Line Topology'):
        success_count += 1
    
    # Run Phase 6 completion
    if run_script('complete_phase_6_data.py', 'PHASE 6: Parallels & Alignment Atlas'):
        success_count += 1
    
    # Run Phase 7 completion
    if run_script('complete_phase_7_data.py', 'PHASE 7: Segmentation'):
        success_count += 1
    
    print('\n' + '=' * 60)
    print('COMPLETION SUMMARY')
    print('=' * 60)
    print(f'Completed: {success_count}/{total_count} phases')
    print(f'Finished: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}')
    
    if success_count == total_count:
        print('\n✅ ALL PHASES 3, 6, AND 7 COMPLETED SUCCESSFULLY!')
        return 0
    else:
        print(f'\n⚠️  {total_count - success_count} phase(s) had errors')
        return 1

if __name__ == '__main__':
    sys.exit(main())
