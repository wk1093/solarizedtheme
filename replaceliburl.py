import os
from pathlib import Path

def update_repo_links():
    # Resolve the 'styles/' directory relative to where the script is located
    base_dir = Path(__file__).parent
    styles_dir = base_dir / "styles"
    
    old_text = "userstyles.catppuccin.com/lib/lib.less"
    new_text = "raw.githubusercontent.com/wk1093/solarizedtheme/refs/heads/main/lib/lib.less"
    
    # Verify the directory exists before proceeding
    if not styles_dir.exists() or not styles_dir.is_dir():
        print(f"Error: Could not find the '{styles_dir.name}' directory at {styles_dir}")
        return

    modified_files_count = 0
    print(f"Scanning '{styles_dir.name}/' for links to replace...\n")

    # rglob("*") recursively finds all files in folders and subfolders
    for filepath in styles_dir.rglob("*"):
        if filepath.is_file():
            try:
                # Read file contents (using UTF-8 as standard for web/style files)
                with open(filepath, 'r', encoding='utf-8') as file:
                    content = file.read()
                
                # If the string is found, replace and overwrite
                if old_text in content:
                    new_content = content.replace(old_text, new_text)
                    
                    with open(filepath, 'w', encoding='utf-8') as file:
                        file.write(new_content)
                        
                    print(f"Updated: {filepath.relative_to(base_dir)}")
                    modified_files_count += 1
                    
            except UnicodeDecodeError:
                # Silently skip binary files (like images/icons) that can't be read as text
                pass
            except Exception as e:
                print(f"Skipped {filepath.relative_to(base_dir)} due to an error: {e}")

    print(f"\nDone! Updated the URL in {modified_files_count} file(s).")

if __name__ == "__main__":
    update_repo_links()
