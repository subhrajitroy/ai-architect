class AdrParser:

    def __init__(self):
        pass


    def parse(self, file_path: list[str]):
        return self.__process(file_path)

  
    def parse(self,file_path:str):
        with open(file_path, 'r') as file:
            lines = file.readlines()
            return self.__process(lines)
    

    def __process(self,lines):
        current_key = None
        current_value = []
        result = {}
        for line in lines:
            line = line.strip()
            # Ignore empty lines
            # print(line)
            if not line:
                continue
            if line.startswith("*"):
                # This is needs to redone
                current_key , current_value = self.__add_attribute(line,result=result)
                continue
            if line.startswith("#"):
                formatted_key = self.__format_key(line)
                if current_key is not None:
                    result[current_key] = "\n".join(current_value)
                    current_value = []
                current_key = formatted_key
                continue
            current_value.append(line)
        return result
        
    
    def __add_attribute(self,line,result):
        formatted_key = self.__format_key(line)
        key,value = self.__extract_attribute_values_from_line(formatted_key)
        if(key is not None and value is not None):
            result[key] = value
            current_key = None
            current_value = []
        else:
            current_key = formatted_key
            current_value = []
        return current_key, current_value
    
    def __format_key(self,key):
        # Remove any leading/trailing whitespace and special characters
        key = key.strip()
        # Replace spaces with underscores
        key = key.replace("#", "")
        key = key.replace("*", "")
        # Convert to lowercase
        key = key.lower()
        return key
    
    def __extract_attribute_values_from_line(self,line):
        if line.find(":") > 0:
            items = line.split(":")
            if(items is not None and len(items) == 2):
                return (items[0], items[1])
            else:
                return (items[0], None) 
        else:
            return (None, None)
        

# def main():
#     parser = AdrParser("data/adr/sample_adr.md")
#     parsed_data = parser.parse()
#     print(parsed_data)

# main()

