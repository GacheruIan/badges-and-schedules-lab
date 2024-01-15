def badge_maker(name):
    return (f"Hello, my name is {name}.")
    
badge_maker("Guido van Rossum")


def batch_badge_creator(names):
    result = []
    for name in names:
        result.append(f"Hello, my name is {name}.")
    return result

batch_badge_creator(["Arel", "Carol"])

def assign_rooms(names):
    res = []
    cpy = names.copy()
    for index, name in enumerate(cpy,1):
        r = (f"Hello, {name}! You'll be assigned to room {index}!")
        res.append(r)
    return res

def printer(names):
    for name in names:
        print((f"Hello, my name is {name}."))
        
    for index, name in enumerate(names,1):
        print(f"Hello, {name}! You'll be assigned to room {index}!")
     
 

printer(["Arel", "Carol"])