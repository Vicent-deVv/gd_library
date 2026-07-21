class Parser:
    def __init__(self):
        self.sixty_four_table = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"

    def data_parser(self, raw_data: str) -> dict:

        if raw_data == "-1" or not raw_data:
            return {"error": "Level not found"}

        part = raw_data.split(":")

        data = {}

        for i in range(0, len(part)-1, 2):
            key = part[i]
            value = part[i+1]

            data[key] = value

        return data
        
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