
import requests
import json
import math
import os

class Hashmap:
    def __init__(self, arrSize):
        self.size = arrSize
        self.map = [None] * self.size

    def _get_hash(self, key):
    #    hash = 0
     #   hash = key % self.size
      #  return hash
        hash = 0
        for char in str(key):
            hash += ord(char)
        return hash % self.size
    
    
    def add(self, key, value):
        key_hash = self._get_hash(key)
        key_value = [key, value]

        if self.map[key_hash] is None: #if cell is empty assign it
            self.map[key_hash] = list([key_value])
            return True
        else: #else check if it already exists if not add it
            for pair in self.map[key_hash]: #iterate through each pair in the map
                if pair[0] == key:
                    #do nothing same key is in the table already
                    return True
            self.map[key_hash].append(key_value)# add on to that cell of the map
            return True
    def get(self, key):
        key_hash = self._get_hash(key)
        if self.map[key_hash] is not None:
            for pair in self.map[key_hash]:
                # print("pair[0]")
                # print(pair[0])
                # print("key:")
                # print(key)
                # print("\n")
                if pair[0] == key:
                    return ("1")
        else:
            return ("None")
    
    def delete(self, key):
        key_hash = self._get_hash(key)

        if self.map[key_hash] is None:
            return False
        for i in range(0, len(self.map[key_hash])): # we need the index to remove something from python
            if self.map[key_hash][i][0] == key:
                self.map[key_hash].pop(i)
                return True
    
    def print(self):
        print('-----Games------')
        for item in self.map:
            if item is not None:
                #print('-----item:')
                #print(len(item))
                #print(((item[0]))) #prints out the first game
                                   #item[x][y]: x=game  y=0 or 1 (0=hash key)(1=game info) 
                print(str(item))

                # for i in range(len(item)):
                #     print("XXXX----------------------")
                #     print(i)
                #     print(item[i][1])
                #     print("----------------------XXX\n\n")

    
    def output_file(self):
        #open file
        f5 = open("misterList.txt","w")
        for item in self.map:
            if item is not None:
                #print(len(item[0]))
                for i in range(len(item)):
                    f5.write((item[i][1]))
                
        f5.close()
    
def write_Game(text):
    #split up the file ['Azurian Attack', '/media/rmaFolder/Azurian%20Attack.mra', 'https://archive.org/download/MAME220RomsOnlyMerged/azurian.zip', 'games/mame/azurian.zip\n']
    game = text.split(',')

    #get the rma file replace the %20 characters that show up from .get()
    #print((game[1].replace('%20',' ')))
    split = (game[1].replace('%20',' ')).split('/')
    mra = split[3]

    #write the mra file
    r4 = requests.get('http://127.0.0.1:8000/media/rmaFolder/' + mra)
    with open('../_Arcade/'+mra,'wb') as fx:
        fx.write(r4.content)

    #check how many files need to be downloaded subtract off the mra file and game name
    #divide for how many pairs of files and paths
    num_files = int((len(game) - 2)/2)
    file_link = [] #['https://archive.org/download/mame.0229/bilyard.zip']    
    file_path = [] #['games/mame/athena.zip\n']


    for i in range(num_files):
        file_link.append(game[i+2]) #plus 2 start at the first download link skip 'game_name' and 'rma'
    
    for i in range(num_files):
        file_path.append(game[(num_files+i+2)]) #plus 2 start at the first download link skip 'game_name' and 'rma'
                                          #plus num_files to skip over the file_link

    
    # print(num_files)
    # print("file_link") #['https://archive.org/download/MAME220RomsOnlyMerged/azurian.zip']
    # print(str(file_link))
    # print("\n")
    # print("file_path") #['games/mame/azurian.zip\n']
    # print(str(file_path))
    # print("\n")

    #output the files. the Zip files
    for i in range(num_files):
        r1 = requests.get((file_link[i].strip('\n')).strip(' '))
        #get file
        with open('../'+(file_path[i].strip('\n')).strip(' '),'wb') as fx:
            fx.write(r1.content)


#same as write_Game but now delete
def delete_Game(text):
    #split up the file ['Azurian Attack', '/media/rmaFolder/Azurian%20Attack.mra', 'https://archive.org/download/MAME220RomsOnlyMerged/azurian.zip', 'games/mame/azurian.zip\n']
    game = text.split(',')

    #get the rma file replace the %20 characters that show up from .get()
    #print((game[1].replace('%20',' ')))
    split = (game[1].replace('%20',' ')).split('/')
    mra = split[3]

    
    #delete MRA file
    if os.path.exists('../_Arcade/'+mra):
        os.remove('../_Arcade/'+mra)
    # else:
    #     print("File does not exist")


    #check how many files need to be downloaded subtract off the mra file and game name
    #divide for how many pairs of files and paths
    num_files = int((len(game) - 2)/2)

    file_link = [] #['https://archive.org/download/mame.0229/bilyard.zip']    
    file_path = [] #['games/mame/athena.zip\n']

    for i in range(num_files):
        file_link.append(game[i+2]) #plus 2 start at the first download link skip 'game_name' and 'rma'
    
    for i in range(num_files):
        file_path.append(game[(num_files+i+2)]) #plus 2 start at the first download link skip 'game_name' and 'rma'
                                          #plus num_files to skip over the file_link

    # zip_file = file_link[0].split('/') #['https:', '', 'archive.org', 'download', 'MAME216RomsOnlyMerged', '1942.zip']
    # last_elem = (len(zip_file) - 1) #last element in the array is the file name
    # print("zip_file")
    # print(last_elem)


    #delete the zip files
    for i in range(num_files):
        if os.path.exists('../'+(file_path[i].strip('\n')).strip(' ')):
            os.remove('../'+(file_path[i].strip('\n')).strip(' '))
        # else:
        #     print("File does not exist")

    #delete MRA file




payload = {'value':'03822b5f-3f93-4ad3-be7f-17d430712e45'}









#----------------------------------main code---------------------
try:
    python_sucks = 0
    r = requests.get('http://127.0.0.1:8000/account/userGame', params=payload) #getting account info
    #r = requests.get('http://127.0.0.1:8000/media/rmaFolder/19XX_The_War_Against_Destiny_Euro_960104.mra', params=payload) #downloading the file
    #print(r.status_code )
    if r.status_code == 200:

        #print("---------------------------------")
        #print("connected")


        #turn json text into python objects
        server_list = json.loads(r.text)
        #get the number of games
        web_num_games = len(server_list)
        #length of the table should be size*1.3
        hash_size = math.ceil(1.3*web_num_games)
        #create the serve Game list hashmap  
        h_web = Hashmap(hash_size)
        #Create a new file
        f = open("serverList.txt","w")
        #print(server_list)
#-------output the web server list to a file and add it to the hash table h_web. 
        #I get division by zero in modulus operator
        for x in range(web_num_games):
            output = (server_list[x]['game_name']+","+server_list[x]['rma_file']+","+server_list[x]['game_file_link']+","+server_list[x]['file_location']+"\n")
            f.write(output)
            h_web.add(server_list[x]['game_name'], output)
        f.close()
        #h_web.print()
        #print("-----------Above-server-Games--------------------\n")

#-------Check if file exists and Check if the file is empty then Lines_test=0 else Lines_test>=1
        if os.path.exists("misterList.txt"):
            f_check = open("misterList.txt","r")
            Lines_test = f_check.readlines()
            f_check.close()

#-------check if the misterList game file exists. if it does then add/delete the games
        if os.path.exists("misterList.txt") and (len(Lines_test)>0):
            #print("file exists!!\n")
            #read in the file
            f2 = open("misterList.txt","r")
            #read the previous misterList.txt games
            Lines = f2.readlines()
            #get the size of the hash table
            hash_size = math.ceil(1.3*len(Lines))
            #create the Mister hashmap
            h_mister = Hashmap(hash_size)
            #The number of games currently in the misterList.txt
            mister_num_games = len(Lines)
            f2.close()

            #print(len(Lines))
#-----------Add in the games to the mister hash map
            for x in range(mister_num_games): 
                #get the current game string
                game=Lines[x].split(',')
                h_mister.add(game[0], Lines[x])
            
#-----------#check to see if the misterList.txt games are on the web hash map, If not remove them from the Hash and delete the file
            for x in range(mister_num_games): 
                game=Lines[x].split(',')
                #print(game[0])
                temp = h_web.get(game[0])
                #print(temp)
                if temp == "1":
                    python_sucks =0
                    #print("Do nothing")
                    #game[0]=game_name,   Lines=game download link and path
                    #h_mister.add(game[0], Lines[x])
                else:
                    #print("Remove the game here the function to remove the game file")
                    #print("Delete")
                    h_mister.delete(game[0])
                    delete_Game(Lines[x])

                #print("\n")
            #print("-----------Above-delete-Games--------------------\n\n")


#-----------#check to see if the web games are on the mister hash map, If not add them to the hash map and add the files
            
            #read in the web server list
            f3 = open("serverList.txt","r")
            #read the previous misterList.txt games
            Lines = f3.readlines()
            #h_mister.print()  
            #print("((((((((((()))))))))))")
            temp = h_mister.get('Billiard')
            #print(temp)
            f3.close()
            for x in range(web_num_games): 
                game=Lines[x].split(',')
                temp = h_mister.get((game[0]))
                #print((game[0].strip('\n')))
                #print(temp)
                if temp == "1":
                    python_sucks = 0
                    #print("Do nothing")
                    #game[0]=game_name,   Lines=game download link and path
                    #h_mister.add(game[0], Lines[x])
                else:
                    #print("Remove the game here the function to remove the game file")
                    #print("ADD")
                    h_mister.add(game[0],Lines[x])
                    #print(Lines[x])
                    write_Game(Lines[x])
                
                #print("\n")

            #Output the hashmap to the misterfile

            #h_mister.print()  
            h_mister.output_file()
            #print(h_mister.print())
            #print(h_mister.get("game2"))

            #print("-----------Above-ADD-Games--------------------\n")

#-------if the file does not axist then create it
        else:
            f3 = open("misterList.txt","w")
            for x in range(web_num_games):
                #print("file does not exists!!")
                output = (server_list[x]['game_name']+","+server_list[x]['rma_file']+","+server_list[x]['game_file_link']+","+server_list[x]['file_location']+"\n")
                f3.write(output)
                h_web.add(server_list[x]['game_name'], output) #add to hashmap
                write_Game(output)





            f3.close()



    else:
        python_sucks =0
        #print("could not connect to server")
except requests.exceptions.RequestException as e:
    raise SystemExit(e)


