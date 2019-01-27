import os

#Each website you crawl is a separate project

def create_dir(directory):
    if not os.path.exists(directory):
        print(' Creating projects ' + directory)
        os.makedirs(directory)



#create and crawled files (if not created)
def create_data_files(project_name, base_url):
    queue= project_name +'/queue.txt'
    crawled = project_name + '/crawled.txt'
    if not os.path.isfile(queue):
        write_file(queue, base_url)
    if not os.path.isfile(crawled):
        write_file(crawled, '')



#writing a file function
def write_file(path, data):
    fhan=open(path,'w')
    fhan.write(data)
    fhan.close()

#add data to an existing file
def append_to_file(path, data):
    with open(path, 'a') as file:
        file.write(data+ '\n')


#deleting the  contents of a files
def delte_file_contents(path):
    with open(path):
        pass

#read a file and convert each line to  set items
def file_to_set(file_name):
    results = set()
    with open(file_name, 'rt') as file:
        for line in file:
            results.add(line.strip())
    return results

# Iterate through a set, each item  will be a new line in a file
def set_to_file(links, file):
    delte_file_contents(file)
    for link in sorted(links):
        append_to_file(file, link)
