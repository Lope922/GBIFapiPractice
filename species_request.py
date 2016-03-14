import requests
import json
import os
from wf import  create_new_dir, create_files, read_in
#todo start off with user input for a requested animal name



def Main():
    searchterm = input("Enter the name of an animal to search: ")
    # example url http://api.gbif.org/v1/species/search?q=Puma&rank=GENUS

    # Limit the results to 5
    the_url = "http://api.gbif.org/v1/species/search?q={0}&rank=GENUS&limit=5&language=en".format(searchterm)

    unique_keys = []




    print("Please wait ... \n \t\tsearching for a " + str(searchterm))

    # then make the request
    GBIF_response = requests.get(the_url)

      #CREATE THE DIRECTORY NEEDED IF IT DOESN'T EXIST
    create_new_dir()
    #create_files("GBIFresponse.html")
    create_files("GBIFresponse.txt")
    # type is bytes
  # print("Here is the type of content it returns " + str(type(GBIF_response.content)))


# WRITE THAT INFO TO A FILE SO WE DON'T HAVE TO MAKE REPETITIOUS QuERIES FOR PRACTICE DATA.
#def write_to_file():



    #todo adjust this path and get it working for other people.
    # i would rather the os find the path but i am just going to put the absolute path to make it work and move on.
    # display the path i am thinking of
    #their_path = os.path.expandvars()
    #print("This is their path " + str(their_path))

    my_path = "C:/Users/CaLs_Rig/Project4Temp/"
    # open the file with write status
    #trying to speify the full path name to make sure i am writing to the correct file.
    save = open(my_path + "GBIFresponse.txt", "w")
    save.writelines(str(GBIF_response.content))
    save.close()

# print("Here is all the data " + str(data))
# print(data['results'])
# fw = open("GBIFresponse.txt", mode='w')


#todo read from the file and extract results
# this reads from file. I want to store this in a json object to testing multiple times without deleting the data.

#def read_json_file(filename):
    #todo test and see if and why b is included in the file. Do i need it.
    moldable_data = open("GBIFresponse.txt", "r")
    print(str(moldable_data))
    moldable_data.read()

    #trying to load the json data, and see if it works.
    with open('GBIFresponse.txt', 'a') as outfile:
        data = json.loads(GBIF_response.text)
        json.dump(data, outfile)


    # with open('GBIFresponse.txt', 'w') as f:
    #      data = json.loads(GBIF_response.text)
    #      json.dump(data, f, ensure_ascii=False)


#def display_results_from_stream():
# BELOW IS PRACTICE RETRIEVAL DON'T DELETE
    # description = data['']
    for item in data['results']:
        # this is the unique keys list that will be used to retrieve the other descriptions and infomation.
        unique_keys.append(item['key'])
 #      print("Here is the family " + str(item['family']))
    #   #todo get this to work for each key
        print("here is the description " + str(item['descriptions']))
    # for animals in data['key']:
    #     print(data[str(unique_keys)])
    # todo use the species key to access each individual description
  # for item in unique_keys:
    #     print(str(item))
    #
    # for description in :
    #     print(description)

    #for item in data['descriptions']:
       # print("Here ia the description")

#todo obtain access results 2 through 5 i will need to extract differently. Most likely from by class key num

    #print(description)
    #print(data)


# the response comes back in json. So we need to interpret the json response if there was one,
# as well as more proper information for next step
# results = json.dump("/"facets",results')




#text = json._default_decoder(req.content)
#print(data)


#json._default_decoder(data)


Main()