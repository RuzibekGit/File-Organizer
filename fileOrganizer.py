import os
import shutil


file_memo = {
    'for-folders': "Folders",
    'for-other-files': "Other Files",

    'pdf': 'PDF-document',
    'png': 'Images',
    'jpg': 'Images',
    'jpeg': 'Images',
    'gif': 'Images',
    'webp': 'Images',
    'doc': 'Documents',
    'docx': 'Documents',
    'txt': 'Documents',
    'csv': 'Data',
    'xlsx': 'Data',
    'zip': 'Archives',
    'rar': 'Archives',
    'exe': 'Program Files',
    'mp3': 'Music',
    'wav': 'Music',
    'mp4': 'Videos',
    'avi': 'Videos',
    'flv': 'Videos',
    'wmv': 'Videos',
    'html': 'HTML',
    'json': 'Data',
    'xml': 'Data',
    'ppt': 'Presentations',
    'pptx': 'Presentations',
    'svg': 'Vector Graphics',
    'css': 'Stylesheets',
    'js': 'JavaScript',
    'py': 'Python Scripts',
    'java': 'Java',
    'cpp': 'C++',
    'h': 'Header Files',
    'php': 'PHP Scripts',
    'md': 'Markdown',
    'log': 'Logs',
    'bak': 'Backups',
    'cfg': 'Configuration Files',
    'dll': 'Dynamic Link Libraries',
    'bat': 'Batch Scripts',
    'sh': 'Shell Scripts',
    'sql': 'SQL Scripts',
    'apk': 'Android Apps',
    'ipa': 'iOS Apps',
    'iso': 'Disk Images',
    'torrent': 'Torrent Files',
    'ttf': 'TrueType Fonts',
    'woff': 'Web Fonts',
    'svg': 'Scalable Vector Graphics',
    'ico': 'Icons',
    'jar': 'Java Archives',
    'rpm': 'Linux Packages',
    'deb': 'Debian Packages',
    'rpm': 'Red Hat Packages',
    'tar': 'Tar Archives',
    'gz': 'Gzip Archives',
    'bz2': 'Bzip2 Archives',
    '7z': '7-Zip Archives',
    'dmg': 'Mac Disk Images',
    'app': 'Mac Applications',
    'bat': 'Batch Files',
    'ps1': 'PowerShell Scripts',
    'vbs': 'VBScript Files',
    'reg': 'Registry Files',
    'cfg': 'Configuration Files',
    'ini': 'INI Files',
    'bak': 'Backup Files',
    'tmp': 'Temporary Files',
    'swf': 'Flash Files',
    'class': 'Java Class Files',
    'obj': 'Object Files',
    'pdb': 'Program Database Files',
    'o': 'Object Files',
    'so': 'Shared Object Files',
    'dll': 'Dynamic Link Libraries',
    'lib': 'Library Files',
    'a': 'Static Libraries',
    'h': 'Header Files',
    'hpp': 'C++ Header Files',
    'cs': 'C# Source Files',
    'vb': 'Visual Basic Files',
    'pl': 'Perl Scripts',
    'rb': 'Ruby Scripts',
    'lua': 'Lua Scripts',
    'swift': 'Swift Source Files',
    'go': 'Go Source Files',
    'rs': 'Rust Source Files',
    'kt': 'Kotlin Source Files',
    'scala': 'Scala Source Files',
    'coffee': 'CoffeeScript Files',
    'scss': 'Sass Stylesheets',
    'less': 'Less Stylesheets',
    'ejs': 'EJS Templates',
    'jsx': 'React JSX Files',
    'tsx': 'TypeScript JSX Files',
    'vue': 'Vue.js Files',
    'yaml': 'YAML Files',
    'toml': 'TOML Files',
    'gitignore': 'Git Ignore Files',
    'dockerfile': 'Dockerfiles',
    'htaccess': 'Apache Configuration Files',
    'htpasswd': 'Apache Password Files'
}


def table_pretty(func):
    def wrapper(*args, **kwargs):
        print("\n No:  | File Name           |  Move To ")
        print(  "------|---------------------|----------")
        func(*args, **kwargs)
        print("------|---------------------|----------")
        print("----- |--- Successfully! ---|----------\n")

    return wrapper


def print_like_table(index, filename, ext, your_path):
    formatted_index = f"{index:<5}"
    formatted_filename = f"{filename[:10]}{'_' * (12 - len(filename[:10]))}"
    formatted_ext = f"{ext:<6}"

    print(f"{formatted_index} | {formatted_filename}.{formatted_ext} | {your_path}")





@table_pretty
def organize_files(directory):
    """
    Organizes files in the specified directory based on their extensions.

    Args:
        directory (str): The path to the directory containing files to be organized.

    Returns:
        None
    """
    for index, file in enumerate(os.listdir(directory), 1):
        filename, ext = os.path.splitext(file)

        def engine(category):
            target_dir = os.path.join(directory, category)

            os.makedirs(target_dir, exist_ok=True)
            shutil.move(os.path.join(directory, file), os.path.join(target_dir, file))

            print_like_table(index,
                     filename, ext, category)
            

            
        if os.path.isfile(os.path.join(directory, file)):
            
            if (ext := ext[1:].lower()) in file_memo:
                category = file_memo[ext]
                engine(category)

            elif filename not in file_memo.values() and ext != "ini":
                engine("Other Files")

        elif filename not in file_memo.values():
            engine("Folders")


@table_pretty
def disorganize_files(directory):
    """
    Undoes the organization done by organize_files.
    Moves files from subdirectories back to the main directory.
    Removes subdirectories (if they exist).

    Args:
        directory (str): The path to the directory where files were previously organized.

    Returns:
        None
    """
    memo, index = [], 0
    for category in file_memo.values():
        target_dir = os.path.join(directory, category)
        if os.path.exists(target_dir):
            for file in os.listdir(target_dir):
                shutil.move(os.path.join(target_dir, file),
                          os.path.join(directory, file))
                
                filename, ext = os.path.splitext(file)

                print_like_table((index := index+1), filename, ext, os.path.basename(directory))

            try:
                os.rmdir(target_dir)
                memo.append(f"Removed directory: {category}")
            except PermissionError:
                memo.append(f"Directory cannot be removed: {category}")

    print("------|---------------------|----------")
    for f in memo:
        print(f)




if __name__ == '__main__':
    directory_path = input("\nEnter the directory: ")
    if os.path.isdir(directory_path):
        operation_type = input("\nChoose operation type: \nOrganization    == 1 \nDisorganization == 2: ")

        if operation_type == '1':
            organize_files(directory_path)
        elif operation_type == '2':
            confirmation = input(
                "Are you sure you want to disorganize files? (Press 1 to confirm): ")
            if confirmation == '1':
                disorganize_files(directory_path)
            else:
                print("Disorganization operation canceled.")
        else:
            print("Invalid operation type selected. Please choose 1 for organization or 2 for disorganization.")
    else:
        print("Please provide the accurate directory path.")
