import os

with open('cat_map.txt', 'r') as _:
    dir_name = _.readline().replace('\n','')
    while dir_name:
        try:
            os.makedirs(dir_name)
        except OSError:
            print ("Skipping creation because it exists already:", dir_name)
        dir_name = _.readline().replace('\n','')
