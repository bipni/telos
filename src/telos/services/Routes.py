class Routes:
    def __init__(self, base: str):
        self.after = base
        self.before = base
    
    def and_add(self, path, *handlers):
        self.before = self.after + path
        self.after += path
        
        print(self.after)
        return self.after
    
    def or_add(self, path, *handlers):
        
        print(self.after + path)
        return self.after + path

r = Routes('/base')
s = r.and_add('/1', r.and_add('/2', r.or_add('/3', r.and_add('/4')), r.or_add('/5')))