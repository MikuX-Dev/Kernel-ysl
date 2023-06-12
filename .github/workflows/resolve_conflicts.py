import os

# Function to resolve conflicts automatically
def resolve_conflicts():
    conflict_files = []
    for root, dirs, files in os.walk('.'):
        for file in files:
            if file.endswith('.c') or file.endswith('.cpp'):
                filepath = os.path.join(root, file)
                with open(filepath, 'r+') as f:
                    content = f.read()
                    if '<<<<<<<' in content or '>>>>>>>' in content:
                        conflict_files.append(filepath)
                        f.seek(0)
                        f.truncate()
                        f.write(content.split('=======')[0])

    return conflict_files

# Resolve conflicts
conflict_files = resolve_conflicts()

if conflict_files:
    print('Conflicts resolved successfully for the following files:')
    for file in conflict_files:
        print(file)
else:
    print('No conflicts found.')
