def make_pretty(func):
    def inner():
        print(" I AM THE BEST")
        func()
    return inner

@make_pretty
def ordinary():
    print(" you are mistaken to think , that i am a ordinary person")
ordinary()
