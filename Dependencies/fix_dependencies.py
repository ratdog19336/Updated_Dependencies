import os
import subprocess

# Define paths for cloning the repositories
empyrical_repo = "https://github.com/quantopian/empyrical.git"
pyfolio_repo = "https://github.com/quantopian/pyfolio.git"
base_dir = r"C:\Users\NicholasRatti\OneDrive - Fernandina Capital, LLC\Fernandina Capital\Projects\Active\Investment Papers\Python\MSM\Code\Dependencies"

# Define directories where the repositories will be cloned
empyrical_dir = os.path.join(base_dir, "empyrical")
pyfolio_dir = os.path.join(base_dir, "pyfolio")

def clone_or_update_repo(repo_url, target_dir):
    if not os.path.exists(target_dir):
        # Clone the repository
        subprocess.run(["git", "clone", repo_url, target_dir])
    else:
        # Update the repository if it already exists
        subprocess.run(["git", "-C", target_dir, "pull"])

def install_package(package_dir):
    subprocess.run([os.path.join("venv", "Scripts", "pip"), "install", package_dir])

def main():
    # Ensure the base directory exists
    if not os.path.exists(base_dir):
        os.makedirs(base_dir)

    # Clone or update repositories
    clone_or_update_repo(empyrical_repo, empyrical_dir)
    clone_or_update_repo(pyfolio_repo, pyfolio_dir)

    # Apply any custom modifications to the cloned repos if necessary
    # For example, you can add code here to modify certain files programmatically.

    # Install the modified versions of the packages
    install_package(empyrical_dir)
    install_package(pyfolio_dir)

    # Install other dependencies from requirements.txt
    subprocess.run([os.path.join("venv", "Scripts", "pip"), "install", "-r", "requirements.txt"])

if __name__ == "__main__":
    main()
