import os

#function to create the directories
def create_directories():
    #defines the main directory and subdirectories
    main_directory = "MyFiles"
    subdirectories = ["Docs", "Images", "Videos"]

    #creates the main directory
    if not os.path.exists(main_directory):
        os.mkdir(main_directory)
        print(f"Directory '{main_directory}' created.")

    #creates the subdirectories inside 'MyFiles'
    for subdir in subdirectories:
        subdir_path = os.path.join(main_directory, subdir)
        if not os.path.exists(subdir_path):
            os.mkdir(subdir_path)
            print(f"Subdirectory '{subdir}' created inside '{main_directory}'.")
        else:
            print(f"Subdirectory '{subdir}' already exists inside '{main_directory}'.")

#calls the function to create the files
create_directories()
