from datetime import datetime

now = datetime.now()
print(now) # 2026-09-05 22:12:36.425239

# %Y %a %d %

"""Format using strftime().
Example: "%d/%m/%Y, %H:%M:%S"
"""

print(now.strftime("The current year is: %Y")) # The current year is: 2026
print(now.strftime("%a %A %d %D %y %Y ")) # Sat Saturday 05 09/05/26 26 2026 
