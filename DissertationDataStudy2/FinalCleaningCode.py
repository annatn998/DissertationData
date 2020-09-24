import DataCollection

# opening all of the files at once
# used listdir to get a list of the file names only
from os import listdir
data = listdir('.')


for files in data:
    try:
        DataCollection.DissertationDataCleaning(files)
    except NameError:
        pass
    except IndexError:
        pass
    except IsADirectoryError:
        pass
    except UnicodeDecodeError:
        pass
