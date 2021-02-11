# make first pull request (first choice)

class Input_anime():
    def __init__(self, name, all=False):
        self.name = str(name)
        if self.name == "all":
            return self.name
        self.all = all
        if self.all:
            return self.name
    def git_animeList(self):
        print(Input_anime(name="all", all=True))
    def add_anime(self, name):
        name = input("Enter  the anime name: ") 
        Input_anime(name=name)
name = input("Enter Your Name:")
if __name__ == "__main__": 
    print(Input_anime(name))
