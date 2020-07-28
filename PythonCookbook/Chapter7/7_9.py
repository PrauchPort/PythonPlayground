def greeting(greeter_person):
    def greeter(*args):
        print(f"{greeter_person}: says {args}")
    return greeter


a = greeting("Wojtek")

a("halo")
a("czy", "mnie", "slychac")
