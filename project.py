import shutil, os, re
# Create a regex that matches files with American date format.
datePattern = re.compile(r"""^(.*?) # all text before the date
((0|1)?\d)- # one or two digits for the month
((0|1|2|3)?\d)- # one or two digits for the day
((19|20)\d\d) # four digits for the year 
(.*?)$ # all text after the date """, re.VERBOSE)
if mo == None:
  continue
 # Get the different parts of the filename.
beforePart = mo.group(1)
monthPart = mo.group(2)
dayPart = mo.group(4)
yearPart = mo.group(6)
afterPart = mo.group(8)
--snip--
 euroFilename = beforePart + dayPart + '-' + monthPart + '-' + yearPart + afterPart
# Get the full, absolute file paths.
absWorkingDir = os.path.abspath('.')
amerFilename = os.path.join(absWorkingDir, amerFilename)
euroFilename = os.path.join(absWorkingDir, euroFilename)
# Rename the files.
print(f'Renaming "{amerFilename}" to "{euroFilename}"...')
 #shutil.move(amerFilename, euroFilename) # uncomment after testing