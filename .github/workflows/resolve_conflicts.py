import subprocess

def resolve_conflicts():
    # Get the list of conflicted files
    result = subprocess.run(['git', 'diff', '--name-only', '--diff-filter=U'], capture_output=True, text=True)
    conflicted_files = result.stdout.splitlines()
    
    # Resolve conflicts for each file
    for file in conflicted_files:
        # Use Git's 'checkout --theirs' to choose the version from the branch being merged
        subprocess.run(['git', 'checkout', '--theirs', file])
        
        # Add the resolved file to the staging area
        subprocess.run(['git', 'add', file])
        
    # Continue with the rebase
    subprocess.run(['git', 'rebase', '--continue'])

# Call the function to resolve conflicts
resolve_conflicts()
