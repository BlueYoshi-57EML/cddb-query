import lib.pygn as pygn
import sqlite3
import json
from pathlib import Path

def start():
    selected_ver = input("Query CDDB1 (1) or CDDB2 (2)? (type 1/2): ")
    if selected_ver == '1':
        cddb1()
    elif selected_ver == '2':
        cddb2()
    else:
        print("Wrong input!")
        start()
        
def cddb1():
    if Path("db/CDDB Archive.sqlite3").exists():
        cddb1_search_type = input("Search by artist/album (A) or by song title (T)? (type A/T): ")
        if cddb1_search_type == 'A' or cddb1_search_type == 'a':
            print("If you know both the artist and album name, format your search as so: 'Artist / Album' (without quotes)")
            print("Else, just search for either like you would normally.")
            search = input("Search: ")
            cddb1_search(search,False)
        elif cddb1_search_type == 'T' or cddb1_search_type == 't':
            print("This might take some time compared to the Artist/Album search!")
            search = input("Search: ")
            cddb1_search(search,True)
        else:
            print("Wrong input!")
            cddb1()
    else:
        print("Couldn't find database! Make sure \"CDDB Archive.sqlite3\" is in the db folder and that it is named correctly!")
        print("Download: https://archive.org/download/cddb-archive/CDDB%20Archive.sqlite3 (2.7 G)")
        
def cddb1_search(search,is_title_search):
    con = sqlite3.connect("db/CDDB Archive.sqlite3")
    cur = con.cursor()
    worst_boolean_ever = False
    with open("output.json", "w") as output:
        output.write("")
    with open("output.json", "a") as output:
        output.write(f"[\n")
        for genre in ['blues','classical','country','data','folk','jazz','misc','newage','reggae','rock','soundtrack']:
            if is_title_search:
                #insert yanderedev joke here
                res = cur.execute(f"SELECT * FROM {genre} WHERE TTITLE0 LIKE '%{search}%' OR TTITLE1 LIKE '%{search}%' OR TTITLE2 LIKE '%{search}%' OR TTITLE3 LIKE '%{search}%' OR TTITLE4 LIKE '%{search}%' OR TTITLE5 LIKE '%{search}%' OR TTITLE6 LIKE '%{search}%' OR TTITLE7 LIKE '%{search}%' OR TTITLE8 LIKE '%{search}%' OR TTITLE9 LIKE '%{search}%' OR TTITLE10 LIKE '%{search}%' OR TTITLE11 LIKE '%{search}%' OR TTITLE12 LIKE '%{search}%' OR TTITLE13 LIKE '%{search}%' OR TTITLE14 LIKE '%{search}%' OR TTITLE15 LIKE '%{search}%' OR TTITLE16 LIKE '%{search}%' OR TTITLE17 LIKE '%{search}%' OR TTITLE18 LIKE '%{search}%' OR TTITLE19 LIKE '%{search}%' OR TTITLE20 LIKE '%{search}%' OR TTITLE21 LIKE '%{search}%' OR TTITLE22 LIKE '%{search}%' OR TTITLE23 LIKE '%{search}%' OR TTITLE24 LIKE '%{search}%' OR TTITLE25 LIKE '%{search}%' OR TTITLE26 LIKE '%{search}%' OR TTITLE27 LIKE '%{search}%' OR TTITLE28 LIKE '%{search}%' OR TTITLE29 LIKE '%{search}%' OR TTITLE30 LIKE '%{search}%' OR TTITLE31 LIKE '%{search}%' OR TTITLE32 LIKE '%{search}%' OR TTITLE33 LIKE '%{search}%' OR TTITLE34 LIKE '%{search}%' OR TTITLE35 LIKE '%{search}%' OR TTITLE36 LIKE '%{search}%' OR TTITLE37 LIKE '%{search}%' OR TTITLE38 LIKE '%{search}%' OR TTITLE39 LIKE '%{search}%' OR TTITLE40 LIKE '%{search}%' OR TTITLE41 LIKE '%{search}%' OR TTITLE42 LIKE '%{search}%' OR TTITLE43 LIKE '%{search}%' OR TTITLE44 LIKE '%{search}%' OR TTITLE45 LIKE '%{search}%' OR TTITLE46 LIKE '%{search}%' OR TTITLE47 LIKE '%{search}%' OR TTITLE48 LIKE '%{search}%' OR TTITLE49 LIKE '%{search}%' OR TTITLE50 LIKE '%{search}%' OR TTITLE51 LIKE '%{search}%' OR TTITLE52 LIKE '%{search}%' OR TTITLE53 LIKE '%{search}%' OR TTITLE54 LIKE '%{search}%' OR TTITLE55 LIKE '%{search}%' OR TTITLE56 LIKE '%{search}%' OR TTITLE57 LIKE '%{search}%' OR TTITLE58 LIKE '%{search}%' OR TTITLE59 LIKE '%{search}%' OR TTITLE60 LIKE '%{search}%' OR TTITLE61 LIKE '%{search}%' OR TTITLE62 LIKE '%{search}%' OR TTITLE63 LIKE '%{search}%' OR TTITLE64 LIKE '%{search}%' OR TTITLE65 LIKE '%{search}%' OR TTITLE66 LIKE '%{search}%' OR TTITLE67 LIKE '%{search}%' OR TTITLE68 LIKE '%{search}%' OR TTITLE69 LIKE '%{search}%' OR TTITLE70 LIKE '%{search}%' OR TTITLE71 LIKE '%{search}%' OR TTITLE72 LIKE '%{search}%' OR TTITLE73 LIKE '%{search}%' OR TTITLE74 LIKE '%{search}%' OR TTITLE75 LIKE '%{search}%' OR TTITLE76 LIKE '%{search}%' OR TTITLE77 LIKE '%{search}%' OR TTITLE78 LIKE '%{search}%' OR TTITLE79 LIKE '%{search}%' OR TTITLE80 LIKE '%{search}%' OR TTITLE81 LIKE '%{search}%' OR TTITLE82 LIKE '%{search}%' OR TTITLE83 LIKE '%{search}%' OR TTITLE84 LIKE '%{search}%' OR TTITLE85 LIKE '%{search}%' OR TTITLE86 LIKE '%{search}%' OR TTITLE87 LIKE '%{search}%' OR TTITLE88 LIKE '%{search}%' OR TTITLE89 LIKE '%{search}%' OR TTITLE90 LIKE '%{search}%' OR TTITLE91 LIKE '%{search}%' OR TTITLE92 LIKE '%{search}%' OR TTITLE93 LIKE '%{search}%' OR TTITLE94 LIKE '%{search}%' OR TTITLE95 LIKE '%{search}%' OR TTITLE96 LIKE '%{search}%' OR TTITLE97 LIKE '%{search}%' OR TTITLE98 LIKE '%{search}%'")
            else:
                res = cur.execute(f"SELECT * FROM {genre} WHERE DTITLE LIKE '%{search}%'")
            for item in res.fetchall():
                if worst_boolean_ever:
                    output.write(f",\n")
                worst_boolean_ever = True
                output.write(f"\t{{\n")
                output.write(f"\t\t\"album_discid\": \"{item[0]}\",\n")
                output.write(f"\t\t\"genre\": \"{genre}\",\n")
                output.write(f"\t\t\"url\": \"http://sc2.ca.us.cddb.com/~cddb/cddb.cgi?cmd=cddb+read+{genre}+{item[0].zfill(8)}&hello=name+aaaa+xmcd+1&proto=6\",\n")
                output.write(f"\t\t\"artist_and_album_name\": \"{item[1]}\",\n")
                if item[101] is not None:
                    output.write(f"\t\t\"additional_info\": \"{item[101]}\",\n")
                else:
                    output.write(f"\t\t\"additional_info\": \"\",\n")
                output.write(f"\t\t\"tracks\": [\n")
                for i in range(2,101):
                    if item[i] is not None:
                        output.write(f"\t\t\t{{\n")
                        output.write(f"\t\t\t\t\"track_number\": \"{i-1}\",\n")
                        output.write(f"\t\t\t\t\"track_title\": \"{item[i]}\",\n")
                        if item[i+100] is not None:
                            output.write(f"\t\t\t\t\"additional_info\": \"{item[i+100]}\"\n")
                        else:
                            output.write(f"\t\t\t\t\"additional_info\": \"\"\n")
                        if i!=100 and item[i+1] is not None:
                            output.write(f"\t\t\t}},\n")
                        else:
                            output.write(f"\t\t\t}}\n")
                output.write(f"\t\t]\n")
                output.write(f"\t}}")
        output.write(f"\n]")
    with open("output.json", "r") as output:
        print(output.read())
    print("Output saved to output.json!")
    
def cddb2():
    if not Path("storage/client_id.txt").exists():
        print("client_id.txt not found in the storage folder!")
    elif not Path("storage/user_id.txt").exists():
        print("user_id.txt not found in the storage folder!")
    else:
        with open("storage/client_id.txt", "r") as client_id_file:
            client_id = client_id_file.read()
            if client_id == "":
                print("Client ID not found! Make sure it is of format XXXXXXXX-YYYYYYYYYYYYYYYYYYYYYYYY with X as decimal and Y as hex!")
                start()
            else:
                with open("storage/user_id.txt", "r+") as user_id_file:
                    user_id = user_id_file.read()
                    if user_id == "":
                        create_new_user_id = input("User ID not found? Create one? (Y/N): ")
                        if create_new_user_id == 'Y' or create_new_user_id == 'y':
                            try:
                                new_user_id = pygn.register(client_id)
                                user_id_file.write(f"{new_user_id}")
                                print(f"Saved to user_id.txt! {new_user_id}")
                                user_id = user_id_file.read()
                                cddb2()
                            except UnboundLocalError:
                                print("Client ID seems to be invalid. Please check client_id.txt")
                                start()
                        elif create_new_user_id == 'N' or create_new_user_id == 'n':
                            print("You must create a user ID to query CDDB2.")
                            cddb2()
                        else:
                            print("Wrong input!")
                            cddb2()
                    else:
                        cddb2_search_type = input("Search by artist/album/track name (N), by TOC (T), or by GNID (I)? (type N/T/I): ")
                        if cddb2_search_type == 'N' or cddb2_search_type == 'n':
                            print("You can leave fields blank but at least ONE of the fields must be queried.")
                            artist = input("Artist name: ")
                            album = input("Album name: ")
                            track = input("Track name: ")
                            if artist+album+track == "":
                                print("Must query at least one of the fields!")
                                cddb2()
                            else:
                                try:
                                    with open("output.json", "w+") as output:
                                        json.dump(pygn.get_discography(client_id, user_id, artist, album, track), output, indent=4)
                                    with open("output.json", "r") as output:
                                        print(output.read())
                                    print("Saved to output.json!")
                                except UnboundLocalError:
                                    print("Either no results were found, or you reached the query limit (100/day). If it's the latter you should be able to create a new user ID to bypass this.")
                                    start()
                        elif cddb2_search_type == 'T' or cddb2_search_type == 't':
                            print("TOC is a string of offsets in the format '150 20512 30837 50912 64107 78357 ...'. Unit is CD frames, 75 frames is 1 second.")
                            toc = input("Enter TOC: ")
                            if toc == "":
                                print("Input is blank!")
                                cddb2()
                            else:
                                try:
                                    with open("output.json", "w+") as output:
                                        json.dump(pygn.get_discography(client_id, user_id, toc=toc), output, indent=4)
                                    with open("output.json", "r") as output:
                                        print(output.read())
                                    print("Saved to output.json!")
                                except UnboundLocalError:
                                    print("Either no results were found, or you reached the query limit (100/day). If it's the latter you should be able to create a new user ID to bypass this.")
                                    start()
                        elif cddb2_search_type == 'I' or cddb2_search_type == 'i':
                            print("GNIDs can be obtained by querying by name/TOC first. This is mostly if you want more detail/the full tracklist of a comp CD containing a certain artist.")
                            gnid = input("Enter GNID: ")
                            if gnid == "":
                                print("Input is blank!")
                                cddb2()
                            else:
                                try:
                                    with open("output.json", "w+") as output:
                                        json.dump(pygn.fetch(client_id, user_id, gnid), output, indent=4)
                                    with open("output.json", "r") as output:
                                        print(output.read())
                                    print("Saved to output.json!")
                                except UnboundLocalError:
                                    print("Either no results were found, or you reached the query limit (100/day). If it's the latter you should be able to create a new user ID to bypass this.")
                                    start()
                        else:
                            print("Wrong input!")
                            cddb2()
                            
start()