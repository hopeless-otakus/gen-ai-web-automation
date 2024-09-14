import os

def check_directory_access():
    # Path to the 'crai-hugo' directory, assuming it's at the same level as 'backend'
    crai_hugo_path = os.path.join('..', 'crai-hugo')
    
    # Check if the directory exists
    if os.path.exists(crai_hugo_path):
        print(f"Directory '{crai_hugo_path}' exists.")
        
        # List contents of the directory
        try:
            contents = os.listdir(crai_hugo_path)
            print(f"Contents of '{crai_hugo_path}':")
            for item in contents:
                print(item)
        except PermissionError:
            print(f"Permission denied: Cannot access '{crai_hugo_path}'.")
        except Exception as e:
            print(f"An error occurred: {e}")
    else:
        print(f"Directory '{crai_hugo_path}' does not exist.")

if __name__ == '__main__':
    check_directory_access()
