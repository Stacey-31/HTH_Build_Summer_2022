from main import all_vars

for var in all_vars:
  if '__' in var:
    all_vars.remove(var)
  
print(all_vars)