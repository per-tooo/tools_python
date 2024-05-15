from sys import argv

def getArgumentsList() -> list:
  return argv[1:]

def argumentIsset(argument:str) -> object:
  position = -1
  search = f"-{argument}" if len(argument) == 1 else f"--{argument}"

  for index in range(0, len(getArgumentsList())):
    item = getArgumentsList()[index]
    if item == search:
      isset = index

  return isset

def getArgument(argument:str, startsWithDash:bool = False) -> object:
  position = argumentIsset(argument)
  if position == -1:
    return None
  
  arguments = getArgumentsList()
  if not((position + 1) > len(arguments)):
    value = arguments[position + 1]
    if value[0] == "-":
      if not startsWithDash:
        value = None
  
  return value
