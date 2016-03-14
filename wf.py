# this is the write file class. Putting this seperate to try and make code easier to maintain
import os


#creates a the directory not the file
def create_new_dir():
    current_user_path = os.path.expanduser("~")
    if os.path.exists(current_user_path + "/Project4Temp"):
        print("The dir alaready exists\n what do you wnat to do now")
        #not sure if this allow me to move on just trying out the yiled so see if i can avoid error message
        yield
    else:
        print("Path does not exists i will try and create it")
    os.mkdir(current_user_path + "/Project4Temp")

# creates the file not the directory
def create_files(filename):

    current_user_path = os.path.expanduser("~")
   # temp_file_location = os.path.abspath(current_user_path + "/Seperator/")
    file_make = open(current_user_path +"/Project4Temp/" + filename, mode="a")
    file_make.write("Here is some new info ")
    file_make.close()

#this method is supposed to read from a specified filename , and return the results

def read_in(filename):
    current_user_path = os.path.expanduser("~")
    # if file is not empty do this
    if os.path.isfile(os.path.abspath(current_user_path + "/" + filename)):
        file_read = open(current_user_path + "/" + filename, mode="r")
        file_info = file_read.readlines(filename)
        file_read.close()
   # return print(str(file_info))


# def writeResponsetoFile(data,path):
#     filename = "apiResponseData.txt"
#     #create the file with overwrite mode
#     full_path = os.path.join(path,filename)
#     temp_file = open(str(full_path))
#   #  temp_file.write(data, mode="a")
#     temp_file.close()

# def mkdirs():
#     workinDir = os.path.
#     print("this is the dir i am going to create a folder in " + str(workinDir))

# create_new_dir()
# create_files("GBIFresponse.txt")
#get_user_location()

#todo create a clean up method within the file manager class to delete everything. Should be easy.
# this method is for removing any files created as part of freeing up resources.
def clean_up(filename):
    try:
        os.remove(filename +".txt")
    except Exception as ex:
        print("There has been an error. although it should have never made it to this point. code for this error" + str(ex))
