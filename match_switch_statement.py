lang = input("Enter your preferred language: ")
match lang:
    case "java":
        print("You are a hardcore programmer")
    case "javascript":
        print("You can be a fullstack developer")
    case "python":
        print("Life is easy programming in python")
    #     default
    case _:
        print("You no sabi anything")
