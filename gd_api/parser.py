class Parser:
    def __init__(self):
        self.sixty_four_table = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"

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

    # ------------ Encoder and De-encoder section ----------------

    def de_encoder64(self, encrypted_text: str):
        
        to_binary = []

        for word in encrypted_text:
            index = self.translator_64_word(word)

            if index == -1:
                continue

            to_binary.append(format(index, "06b"))

        bit_block = "".join(to_binary)

        decoded_bytes = []

        for i in range(0, len(bit_block), 24):

            block = bit_block[i:i+24]

            if len(block) < 8:
                break

            byte1 = block[0:8]
            decoded_bytes.append(int(byte1, 2))

            if len(block) >= 16:
                byte2 = block[8:16]
                decoded_bytes.append(int(byte2, 2))

            if len(block) >= 24:
                byte3 = block[16:24]
                decoded_bytes.append(int(byte3, 2))


        result = ""

        for byte in decoded_bytes:
            result += chr(byte)

        return result     
            
    def translator_64_word(self, word):
        counter = 0

        for i in self.sixty_four_table:
            if word == i:
                return counter
            counter += 1

        return -1