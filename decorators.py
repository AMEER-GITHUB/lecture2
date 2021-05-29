def announce(f): # here 'f' is a func. passed as parameter
    def wrapper():
        print("About to run the function...")
        f()
        print("Done with the function...")
    return wrapper

@announce # Adding decorator to the func.
def hello():
    print("Hello!, AKHIB")

hello()