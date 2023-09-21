t = '' #patern string
s = '' #parent string
import re 
def find_motif(t, s):
    locations = [] 
    for match in re.finditer('(?={})'.format(t), s):
        locations.append(match.start() + 1)
    return locations 

output = find_motif(t, s)
print(output)


        
