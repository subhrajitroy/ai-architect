def load_file(file_path):
        """
        Load contents of a file.
        
        Args:
            file_path (str): Path to the file.
            
        Returns:
            str: Contents of the file.None if error.
        """
        content = ""
        try:
            with open(file_path, 'r') as file:
                content = file.read()
        except Exception as e:
            print(f"Error loading principles: {e}")
            return None
        return content
                
           
    