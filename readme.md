# File Organizer

This Python script organizes files in a specified directory based on their file extensions into respective folders. It also includes functionality to reverse this organization.

## Features

- **Organization**: Files are categorized into folders such as Documents, Images, Videos, etc., based on their extensions.
- **Disorganization**: Reverses the organization by moving files from categorized folders back to the main directory and removes empty subdirectories.

## Usage

### Requirements

- Python 3.x
- `os` and `shutil` modules (standard library)

### Installation

No installation required. Just download `file_organizer.py`.

### How to Use

1. **Run the Script**: Execute the script `file_organizer.py`.
   
2. **Input Directory**: Enter the path of the directory you want to organize/disorganize when prompted.

3. **Choose Operation**:
   - For Organization: Type `1`.
   - For Disorganization: Type `2` and confirm by typing `1`.

4. **View Results**: The script will display a table showing each file moved and its new location.

### Example

```bash
$ python file_organizer.py

Enter the directory: /path/to/your/directory
Choose operation type:
Organization    == 1
Disorganization == 2: 1

# Output showing files organized

 No:  | File Name           |  Move To
------|---------------------|----------
1     | my_file.pdf         | PDF-document
2     | image.png           | Images
3     | report.docx         | Documents
4     | data.csv            | Data
5     | script.py           | Python Scripts
------|---------------------|----------
----- |--- Successfully! ---|----------


# OR

Enter the directory: /path/to/your/directory
Choose operation type:
Organization    == 1
Disorganization == 2: 2

Are you sure you want to disorganize files? (Press 1 to confirm): 1

# Output showing files disorganized

 No:  | File Name           |  Move To
------|---------------------|----------
 1    | my_file.pdf         | directory
 2    | report.docx         | directory
 3    | image.png           | directory
 4    | data.csv            | directory
 5    | another_file.pdf    | directory
 6    | picture.jpg         | directory
 7    | notes.txt           | directory
------|---------------------|----------
 Removed directory: Folders
 Removed directory: PDF-document
 Removed directory: Images
 Removed directory: Documents
------|---------------------|----------
----- |--- Successfully! ---|----------
 
...
```

### Notes
 - **File Types:** The script categorizes files based on their extensions. If an extension isn't specified in `file_memo`, files are categorized as `"Other Files"`.
 - **Safety:** The script is designed to handle typical file operations safely, including checking if directories exist before moving files, the script checks if the target directories (e.g., Documents, Images) exist. If they don't, it creates them using `os.makedirs(target_dir, exist_ok=True)`.


- **Avoid Overwriting**: The script does not overwrite existing files. If a file with the same name exists in the destination directory, `shutil.move()` will raise an exception. This ensures that existing data is not unintentionally overwritten.


- **Confirmation for Disorganization**: When performing disorganization (moving files back to the main directory), the script asks for user confirmation (`Are you sure you want to disorganize files?`). This prevents accidental data loss or unintended directory removal.



`Contact information: ruzibek.work@gmail.com`
