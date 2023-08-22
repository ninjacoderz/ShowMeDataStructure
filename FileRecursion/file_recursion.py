import os


def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """
    if (os.path.isdir(path)):
        files_in_dir = os.listdir(path)
    else:
        return "Invalid folder!"
    file_matched = []
    for file in files_in_dir:
        path_to_file = path+"/"+file
        if (os.path.isfile(path_to_file)):
            if(file.endswith(suffix)):
                file_matched.append(path_to_file)
            else:
                continue
        if (os.path.isdir(path_to_file)):
            file_matched.extend(find_files(suffix,path_to_file))
    return file_matched

print(find_files("c", "."))

## Add your own test cases: include at least three test cases
## and two of them must include edge cases, such as null, empty or very large values

## Test Case 1

## Test Case 2 invalid path
print(find_files('.h', "." + '/abc'))
## Test Case 3 invalid extension
print(find_files('.gyh',"." ))
