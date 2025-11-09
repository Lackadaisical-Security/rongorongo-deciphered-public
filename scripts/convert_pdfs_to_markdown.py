#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Convert Pdfs To Markdown

Copyright © 2025 Lackadaisical Security
Website: https://lackadaisical-security.com
Support: support@lackadaisical-security.com
GitHub: https://github.com/Lackadaisical-Security/rongorongo-deciphered-public

Licensed under Creative Commons Attribution-NonCommercial 4.0 International (CC BY-NC 4.0)
https://creativecommons.org/licenses/by-nc/4.0/

Convert Second Pass PDF Phase Documents to Markdown

This script properly extracts text from PDF files and converts them to
well-formatted markdown, preserving structure and fixing common PDF extraction issues.

Author: Lackadaisical Security (The Operator)
Created: 2025-10-30
Modified: 2025-10-30
Version: 1.0.0
"""

__version__ = "1.0.0"
__author__ = "Lackadaisical Security"
__copyright__ = "Copyright © 2025 Lackadaisical Security"
__license__ = "CC BY-NC 4.0"


import pdfplumber
import re
import os
from pathlib import Path


class PDFToMarkdownConverter:
    def __init__(self, repo_root):
        self.repo_root = Path(repo_root)
        
    def join_pages(self, page_texts):
        """Join text from multiple pages, handling sentence splits at boundaries"""
        if not page_texts:
            return ""
        
        if len(page_texts) == 1:
            return page_texts[0]
        
        result = []
        for i, text in enumerate(page_texts):
            lines = text.split('\n')
            
            if i == 0:
                # First page - add all lines
                result.extend(lines)
            else:
                # Subsequent pages - check if first line continues from previous
                if lines and result:
                    last_line = result[-1].strip()
                    first_line = lines[0].strip()
                    
                    # If last line of previous page doesn't end with sentence punctuation
                    # and first line doesn't start with bullet/uppercase, join them
                    if last_line and not last_line.endswith(('.', '!', '?', ':', '"', '"')) and \
                       first_line and not first_line[0].isupper() and \
                       not first_line.startswith(('* ', '- ', '• ')):
                        # Join the lines
                        result[-1] = last_line + ' ' + first_line
                        lines = lines[1:]  # Skip first line since we merged it
                    elif last_line and first_line and \
                         not last_line.endswith(('.', '!', '?', ':', '"', '"', ')', ']')) and \
                         first_line[0].islower():
                        # Also join if first line starts with lowercase
                        result[-1] = last_line + ' ' + first_line
                        lines = lines[1:]
                
                # Add remaining lines from this page
                result.extend(lines)
        
        return '\n'.join(result)
    
    def clean_text(self, text):
        """Clean up common PDF extraction artifacts"""
        if not text:
            return ""
        
        # Fix hyphenation at line breaks
        text = re.sub(r'(\w+)-\s*\n\s*(\w+)', r'\1\2', text)
        
        # Remove excessive whitespace but preserve paragraph breaks
        lines = text.split('\n')
        cleaned_lines = []
        prev_empty = False
        
        for line in lines:
            line = line.strip()
            
            # Skip standalone page numbers (single digits or small numbers at end of pages)
            # These appear as isolated lines in PDFs
            if re.match(r'^\d{1,2}$', line):
                continue
            
            if not line:
                if not prev_empty:
                    cleaned_lines.append('')
                prev_empty = True
            else:
                cleaned_lines.append(line)
                prev_empty = False
        
        text = '\n'.join(cleaned_lines)
        
        # Fix common character issues
        text = text.replace('ﬁ', 'fi')
        text = text.replace('ﬂ', 'fl')
        text = text.replace('–', '-')
        text = text.replace('—', '--')
        text = text.replace('"', '"')
        text = text.replace('"', '"')
        text = text.replace(''', "'")
        text = text.replace(''', "'")
        
        return text
    
    def detect_headers(self, lines):
        """Detect potential headers based on formatting and content"""
        formatted_lines = []
        
        for i, line in enumerate(lines):
            stripped = line.strip()
            if not stripped:
                formatted_lines.append('')
                continue
            
            # Skip if already a markdown header
            if stripped.startswith('# '):
                formatted_lines.append(stripped)
                continue
            
            # Check if line is all caps or title case and relatively short
            if len(stripped) < 100 and (stripped.isupper() or stripped.istitle()):
                # Check if next line is empty or different style
                is_header = False
                if i + 1 < len(lines) and not lines[i + 1].strip():
                    is_header = True
                elif i == 0 or (i > 0 and not lines[i-1].strip()):
                    is_header = True
                
                if is_header:
                    # Determine header level
                    if len(stripped) < 50:
                        formatted_lines.append(f'## {stripped}')
                    else:
                        formatted_lines.append(f'### {stripped}')
                    continue
            
            # Check for bullet points
            if re.match(r'^[•●○▪▫-]\s+', stripped):
                formatted_lines.append('* ' + stripped[2:])
            # Check for numbered lists
            elif re.match(r'^\d+\.\s+', stripped):
                formatted_lines.append(stripped)
            else:
                formatted_lines.append(stripped)
        
        return formatted_lines
    
    def convert_pdf_to_markdown(self, pdf_path, output_path):
        """Convert a single PDF file to markdown"""
        try:
            print(f"Converting: {pdf_path.name}")
            
            with pdfplumber.open(pdf_path) as pdf:
                # Extract title from first page
                first_page_text = pdf.pages[0].extract_text()
                title_lines = first_page_text.split('\n')[:3]
                title = title_lines[0].strip() if title_lines else pdf_path.stem
                
                # Build content
                content = [f"# {title}\n"]
                
                # Extract text from all pages and join them
                all_text = []
                for page_num, page in enumerate(pdf.pages, 1):
                    page_text = page.extract_text()
                    if page_text:
                        cleaned = self.clean_text(page_text)
                        if cleaned:
                            # Don't repeat the title from first page
                            if page_num == 1:
                                # Remove title lines from content
                                lines = cleaned.split('\n')
                                # Skip first few lines that match the title
                                start_idx = 0
                                for i, line in enumerate(lines[:5]):
                                    if line.strip() == title.strip():
                                        start_idx = i + 1
                                        break
                                cleaned = '\n'.join(lines[start_idx:])
                            
                            all_text.append(cleaned)
                
                # Join all pages together, handling sentence splits at page boundaries
                combined_text = self.join_pages(all_text)
                content.append(combined_text)
                
                # Combine all content
                full_text = '\n\n'.join(content)
                
                # Process for better formatting
                lines = full_text.split('\n')
                formatted_lines = self.detect_headers(lines)
                
                # Clean up any malformed headers (e.g., "## # Title")
                cleaned_lines = []
                for line in formatted_lines:
                    # Fix double header markers
                    line = re.sub(r'^##\s*#\s+', '# ', line)
                    cleaned_lines.append(line)
                
                # Write to file
                with open(output_path, 'w', encoding='utf-8') as f:
                    f.write('\n'.join(cleaned_lines))
                
                print(f"  ✓ Created: {output_path.name} ({len(pdf.pages)} pages)")
                return True
                
        except Exception as e:
            print(f"  ✗ Error converting {pdf_path.name}: {e}")
            return False
    
    def convert_all_phase_pdfs(self):
        """Convert all second-pass phase PDF files to markdown"""
        pdf_files = sorted(self.repo_root.glob('rongorongo-secondpass-phase*.pdf'))
        
        if not pdf_files:
            print("No phase PDF files found!")
            return
        
        print(f"\nFound {len(pdf_files)} PDF files to convert\n")
        
        success_count = 0
        for pdf_file in pdf_files:
            # Generate output filename
            output_name = pdf_file.stem + '.md'
            output_path = self.repo_root / output_name
            
            if self.convert_pdf_to_markdown(pdf_file, output_path):
                success_count += 1
        
        print(f"\n{'='*60}")
        print(f"Conversion complete: {success_count}/{len(pdf_files)} files converted")
        print(f"{'='*60}\n")


def main():
    repo_root = Path(__file__).parent.parent
    converter = PDFToMarkdownConverter(repo_root)
    converter.convert_all_phase_pdfs()


if __name__ == '__main__':
    main()
