class Parser:
    #This only works for level_search function, because is a very specific response 
    def level_parser(self, raw_data: str) -> dict:
        if raw_data == "-1" or not raw_data:
            return {"error": "Level not found"}

        sections = raw_data.split("#")

        result = {
            "levels": {},
            "creators": [],
            "songs": [],
            "page_info": [],
            "hash": ""
        }

        if sections[0]:

            for level_str in sections[0].split("|"):
                level_splitted = level_str.split(":")
                for i in range(0, len(level_splitted) - 1, 2):
                    key = level_splitted[i]
                    val = level_splitted[i + 1]
                    result["levels"][key] = val


        if sections[1]:
            for cr_str in sections[1].split("|"):
                creators_splitted = cr_str.split(":")
                if len(creators_splitted) >= 3:
                    result['creators'].append({
                        "userID" : creators_splitted[0],
                        "username" : creators_splitted[1],
                        "accountID" : creators_splitted[2]
                    })
        

        if sections[2]:
            songs = {}
            for song_str in sections[2].split(":"):
                songs_splitted = song_str.split("~|~")
                for i in range(0, len(songs_splitted) - 1, 2):
                    songs[i] = songs_splitted[i]
                    songs[i + 1] = songs_splitted[i + 1]

            result["songs"].append(songs)

        if sections[3]:
            page_info_splitted = sections[3].split(":")
            
            page_info = {
                "total" : page_info_splitted[0],
                "offset" : page_info_splitted[1],
                "amount" : page_info_splitted[2]
            }

            result["page_info"].append(page_info)

        if sections[4]:
            result["hash"] = sections[4]


        return result

    #This function can parser almost everything, it only works for key -> value pair responses 
    def simple_parser(self, raw_data: str, pattern: str, name: str) -> dict:
            if raw_data == "-1" or not raw_data:
                return {f"Error": "{name} not found"}
    
            part = raw_data.split(pattern)      
    
            data = {}
    
            for i in range(0, len(part)-1, 2):
                key = part[i]
                value = part[i+1]
    
                data[key] = value
    
            return data


