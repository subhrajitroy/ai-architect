class TextSource:
    def __init__(self,lines:list[str]):
        self.lines = lines
    
    def create_chunks(self,size_of_a_chunk=15,overlap=3):
        chunks = []
        if(len(self.lines) < size_of_a_chunk):
            # print(lines)
            chunks.append(".".join(self.lines))
            return chunks
        sublines =  self.lines[0:size_of_a_chunk]
        chunks.append(".".join(sublines))
        return chunks + self.create_chunks(lines=self.lines[size_of_a_chunk-overlap:])