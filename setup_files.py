import os
#create for loop 1 to 25 and print out the numbers
for i  in range(25):
    print(i+1)
    # create folder name 01 to 25
    #format number to be 2 digits
    folder_name = str(i+1).zfill(2)
    # create folder
    try:
        os.mkdir(folder_name)
    except (FileExistsError):
        print("Folder already exists")

    #create files inside folder
    files = ["main.py", "sample.txt", "input1.txt", "input2.txt"]
    for j in range(len(files)):
        file_name = folder_name + "/" + files[j]
        #check if file exists
        if not os.path.exists(file_name):
            #create file
            file = open(file_name, "w")
            #write to file
            file.write("")
            #close file
            file.close()

