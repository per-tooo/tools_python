from sys import argv

def getArgumentList() -> list:
  return argv[1:]

def argumentIsset(argument:str) -> object:
  position = -1
  search = f"-{argument}" if len(argument) == 1 else f"--{argument}"

  for index in range(0, len(getArgumentList())):
    item = getArgumentList()[index]
    if item == search:
      position = index

  return position

def getArgument(argument:str, startsWithDash:bool = False) -> object:
  position = argumentIsset(argument)
  if position == -1:
    return None
  
  arguments = getArgumentList()
  if not((position + 1) > len(arguments)):
    value = arguments[position + 1]
    if value[0] == "-":
      if not startsWithDash:
        value = None
  
  return value
