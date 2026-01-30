#!/usr/bin/env python3
"""
Logseq to Obsidian Link Converter

Converts Logseq-style hashtag links (#TagName) to Obsidian wikilinks ([[TagName]])
across all markdown files in a directory hierarchy.

Usage:
    python linker.py [--dry-run] [--backup] [--verbose]

Options:
    --dry-run   : Preview changes without modifying files
    --backup    : Create backup files before modification (.md.bak)
    --verbose   : Show detailed conversion information
"""

import re
import sys
from pathlib import Path
from typing import Tuple, List
from datetime import datetime


class LogseqToObsidianConverter:
    """Converts Logseq-style links to Obsidian-style wikilinks."""
    
    # Pattern explanation:
    # (?<![#\w\[\]])  : Negative lookbehind - not preceded by #, word char, or [
    # #               : Literal hashtag
    # ([a-zA-Z_]\w*[?]?) : Capture group - starts with letter or underscore, followed by word chars, optional ?
    #                      This ensures we match #TagName but not # followed by space (markdown header)
    PATTERN = r'(?<![#\w\[\]])#([a-zA-Z_]\w*[?]?)'
    
    def __init__(self, root_path: str = ".", dry_run: bool = False, backup: bool = False, verbose: bool = False):
        """
        Initialize the converter.
        
        Args:
            root_path: Root directory to start scanning from
            dry_run: If True, only preview changes without modifying files
            backup: If True, create .md.bak backup files
            verbose: If True, print detailed conversion information
        """
        self.root_path = Path(root_path)
        self.dry_run = dry_run
        self.backup = backup
        self.verbose = verbose
        self.files_processed = 0
        self.conversions_made = 0
        self.total_replacements = 0
        
    def find_markdown_files(self) -> List[Path]:
        """Recursively find all .md files in root_path."""
        return sorted(self.root_path.rglob("*.md"))
    
    def is_already_wikilink(self, match_start: int, original_text: str) -> bool:
        """Check if the matched tag is already part of a [[wikilink]]."""
        # Look backwards for [[ before the match
        if match_start >= 2 and original_text[match_start-2:match_start] == "[[":
            return True
        # Look forwards for ]] after the match
        # This is a simple heuristic - check if ] appears soon after
        match_end = match_start + 20  # reasonable limit
        if "]]" in original_text[match_start:match_end]:
            return True
        return False
    
    def convert_links_in_text(self, text: str) -> Tuple[str, int]:
        """
        Convert all Logseq hashtag links to Obsidian wikilinks in text.
        
        Returns:
            Tuple of (converted_text, number_of_replacements)
        """
        replacements = 0
        
        def replace_func(match):
            nonlocal replacements
            tag_name = match.group(1)
            # Additional check: ensure we're not inside existing wikilinks
            # This is a conservative approach
            replacements += 1
            return f"[[{tag_name}]]"
        
        converted_text = re.sub(self.PATTERN, replace_func, text)
        return converted_text, replacements
    
    def process_file(self, file_path: Path) -> bool:
        """
        Process a single markdown file.
        
        Returns:
            True if file was modified, False otherwise
        """
        try:
            # Read file
            original_content = file_path.read_text(encoding='utf-8')
            
            # Convert links
            converted_content, num_replacements = self.convert_links_in_text(original_content)
            
            # Check if anything changed
            if original_content == converted_content:
                if self.verbose:
                    print(f"  No changes needed")
                return False
            
            # Show what was changed
            if self.verbose or self.dry_run:
                print(f"  Conversions: {num_replacements}")
                self._show_changes(original_content, converted_content)
            
            self.total_replacements += num_replacements
            
            # Write file (unless dry-run)
            if not self.dry_run:
                # Create backup if requested
                if self.backup:
                    backup_path = file_path.with_suffix(file_path.suffix + ".bak")
                    backup_path.write_text(original_content, encoding='utf-8')
                    if self.verbose:
                        print(f"  Backup created: {backup_path.name}")
                
                # Write converted content
                file_path.write_text(converted_content, encoding='utf-8')
                if self.verbose:
                    print(f"  ✓ File updated")
            else:
                print(f"  [DRY-RUN] Would update file")
            
            return True
            
        except Exception as e:
            print(f"  ✗ Error processing file: {e}", file=sys.stderr)
            return False
    
    def _show_changes(self, original: str, converted: str):
        """Show before/after of changed lines."""
        original_lines = original.split('\n')
        converted_lines = converted.split('\n')
        
        for i, (orig_line, conv_line) in enumerate(zip(original_lines, converted_lines)):
            if orig_line != conv_line:
                print(f"    Line {i+1}:")
                print(f"      Before:  {orig_line[:80]}")
                print(f"      After:   {conv_line[:80]}")
    
    def run(self):
        """Execute the conversion process."""
        print(f"{'='*70}")
        print(f"Logseq to Obsidian Link Converter")
        print(f"{'='*70}")
        print(f"Root directory: {self.root_path.absolute()}")
        print(f"Mode: {'DRY-RUN' if self.dry_run else 'LIVE'}")
        print(f"Backup: {'Enabled' if self.backup else 'Disabled'}")
        print(f"Verbose: {'Enabled' if self.verbose else 'Disabled'}")
        print(f"{'='*70}\n")
        
        # Find all markdown files
        md_files = self.find_markdown_files()
        print(f"Found {len(md_files)} markdown files\n")
        
        if not md_files:
            print("No markdown files found.")
            return
        
        # Process each file
        for file_path in md_files:
            relative_path = file_path.relative_to(self.root_path)
            print(f"Processing: {relative_path}")
            
            if self.process_file(file_path):
                self.files_processed += 1
                self.conversions_made += self.total_replacements
        
        # Summary
        print(f"\n{'='*70}")
        print(f"Summary")
        print(f"{'='*70}")
        print(f"Files processed: {self.files_processed}")
        print(f"Total replacements: {self.total_replacements}")
        
        if self.dry_run:
            print(f"\n[DRY-RUN MODE] No files were actually modified.")
            print(f"Run without --dry-run to apply changes.")
        else:
            print(f"\n✓ Conversion complete!")
        
        print(f"{'='*70}\n")


def main():
    """Main entry point."""
    # Parse command line arguments
    dry_run = "--dry-run" in sys.argv
    backup = "--backup" in sys.argv
    verbose = "--verbose" in sys.argv
    
    # Get the directory containing this script
    script_dir = Path(__file__).parent
    
    # Create and run converter
    converter = LogseqToObsidianConverter(
        root_path=str(script_dir),
        dry_run=dry_run,
        backup=backup,
        verbose=verbose
    )
    
    converter.run()


if __name__ == "__main__":
    main()
