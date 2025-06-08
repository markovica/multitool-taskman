class BaseComponent:
    def process(self, file_path):
        raise NotImplementedError("Component subclasses must implement this method.")