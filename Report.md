1. Nan Yang - 4a
    Integrated git hook into the project
    Git Hook is a hidden file inside the Github repo,so you cannot find it directly from the file, you have to edit from the command prompt, and make a change

2. Sai Praneeth - 4b
    Integrated fuzzing into the project

3. Luke Berryman - 4c
    I added logging to detection. I logged four functions in main.py of detection, and one function in py_parser.py of detection.
    I fixed some of the imports for the fuzzing file, and related files
    Python does not easily use files from a higher directory, so it's easiest to create copies of files and put them into the required directories.
    Python does not like modules with dashes in the name, so you should either rename the directory or move the importing files into the directory.

We don't have the forensics log file because we could not get main.py in detection to run. We all tried but it just would not work.