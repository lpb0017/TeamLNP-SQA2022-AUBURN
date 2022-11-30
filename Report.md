1. Git Hook is a hidden file inside the Github repo,so you cannot find it directly from the file, you have to edit from the command prompt, and make a change

4c - Luke Berryman
    I added logging to detection and generation. I logged four functions in main.py of detection, and one function in attack_model.py of generation.
    Python does not easily use files from a higher directory, so I had to to create two different logger files for detection and generation.