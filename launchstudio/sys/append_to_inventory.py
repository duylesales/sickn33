import sys
import os

def main():
    if len(sys.argv) != 2:
        print("Usage: python append_to_inventory.py <file_with_content_to_append>")
        sys.exit(1)
        
    source_file = sys.argv[1]
    inventory_file = "/Users/duyle/sickn33/launchstudio/content_inventory.md"
    
    with open(source_file, "r", encoding="utf-8") as f:
        content_to_append = f.read()
        
    with open(inventory_file, "a", encoding="utf-8") as f:
        f.write(content_to_append)
        if not content_to_append.endswith("\n"):
            f.write("\n")
            
    print(f"Successfully appended {len(content_to_append)} characters to {inventory_file}")

if __name__ == "__main__":
    main()
