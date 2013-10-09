exploredPositions = {} 

def explore(pos, gridsize):
  vpos, hpos = pos
  if vpos > gridsize:
    return 0
  elif hpos > gridsize:
    return 0

  if pos == (gridsize, gridsize):
    return 1

  if pos not in exploredPositions:
    exploredPositions[pos] = explore((vpos, hpos+1), gridsize) + explore( (vpos+1,hpos), gridsize)

  return exploredPositions[pos]

def lattice_paths(gridsize):
  print explore((0,0), 20)

print lattice_paths(2)
    
      
