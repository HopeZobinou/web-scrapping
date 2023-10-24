import requests
import json
import subprocess
import sys
from datetime import datetime

def file_to_list(file_path):
    file_path = file_path
    links = []

    # Open the file in read mode and read its lines
    try:
        with open(file_path, 'r') as file:
            links = file.readlines()
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

    links = [item.strip() for item in links]

    if not file.closed:
        file.close()

    return links

def to_time_maps(links):
    links = links

    for link in links:
        try:
            #Run MemGator to get the TimeMap JSON and store the result in a file
            output_file = f"{link.replace('://', '_').replace('/', '_').replace('?', '_').replace('#', '_').replace('%','_').replace('&','_').replace('{','_').replace('}','_').replace('<','_').replace('>','_').replace('*','_').replace('$', '_').replace('!','_').replace(':','_').replace('@','_').replace('+','_').replace('|','_').replace('=','_')}_timemap.json"
            
            subprocess.run(["c:/Users/hopez/Documents/Data440/Homework2/memgator-windows-amd64","-f", "json", link], stdout = open(output_file, "w"), text=True, check=True)
            print(f"TimeMap JSON for {link} has been saved to {output_file}")
        except subprocess.CalledProcessError as e:
            print(f"Error running MemGator for {link}: {e}")
        except json.JSONDecodeError as e:
            print(f"Error parsing JSON for {link}: {e}")
        except Exception as e:
            print(f"An error occurred: {e}")

def get_num_mementos(links):
    links = links
    num_mementos_list = []
    curr_num_mementos = 0

    for link in links:
        try:
            #Run MemGator to get the TimeMap JSON and get the mementos
            output_file = f"{link.replace('://', '_').replace('/', '_').replace('?', '_').replace('#', '_').replace('%','_').replace('&','_').replace('{','_').replace('}','_').replace('<','_').replace('>','_').replace('*','_').replace('$', '_').replace('!','_').replace(':','_').replace('@','_').replace('+','_').replace('|','_').replace('=','_')}_timemap.json"
            command = subprocess.run(["c:/Users/hopez/Documents/Data440/Homework2/memgator-windows-amd64","-f", "json", link], stdout = subprocess.PIPE, text=True, check=True)
            
            timemap = json.loads((command.stdout)) #Parsing the json
            curr_num_mementos = len(timemap['mementos']['list'])
            num_mementos_list.append(curr_num_mementos)

            print(f"TimeMap JSON for {output_file} has {curr_num_mementos} mementos")
        except subprocess.CalledProcessError as e:
            print(f"Error running MemGator for {link}: {e}")
        except json.JSONDecodeError as e:
            print(f"Error parsing JSON for {link}: {e}")
        except Exception as e:
            print(f"An error occurred: {e}")

    print('The list of mementos:', num_mementos_list)

    return num_mementos_list

def get_uri_age(links):
    links = links
    memento_age_list = []
    age = 0

    for link in links:
        try:
            #Run MemGator to get the TimeMap JSON and get the mementos
            output_file = f"{link.replace('://', '_').replace('/', '_').replace('?', '_').replace('#', '_').replace('%','_').replace('&','_').replace('{','_').replace('}','_').replace('<','_').replace('>','_').replace('*','_').replace('$', '_').replace('!','_').replace(':','_').replace('@','_').replace('+','_').replace('|','_').replace('=','_')}_timemap.json"
            command = subprocess.run(["c:/Users/hopez/Documents/Data440/Homework2/memgator-windows-amd64","-f", "json", link], stdout = subprocess.PIPE, text=True, check=True)

            timemap = json.loads(command.stdout) #Parsing the json
            mementos = timemap['mementos']['list'] #List of mementos from the one URI we are on

            #Getting the age of the uri. We have to subtract this day by the date of the first memento
            first_memento = mementos[0]
            memento_date = first_memento['datetime']
            memento_datetime = datetime.strptime(memento_date, "%Y-%m-%dT%H:%M:%SZ")
            curr_datetime = datetime.now()
            age = (curr_datetime - memento_datetime).days

            memento_age_list.append(age)

            print(f"TimeMap JSON for {output_file} is {age} days old")
        except subprocess.CalledProcessError as e:
            print(f"Error running MemGator for {link}: {e}")
        except json.JSONDecodeError as e:
            print(f"Error parsing JSON for {link}: {e}")
        except Exception as e:
            print(f"An error occurred: {e}")
    
    return memento_age_list


if __name__ == "__main__":
    #Path to the txt file "c:/Users/hopez/Documents/Data440/Homework2/twitter_links.txt"

    if len(sys.argv) != 2:
        print("2 arguments are required, the file name and path to the links.")
        sys.exit(1)

    links = file_to_list(sys.argv[1])

    #to_time_maps(links[0:5]) #000-999
    #memento_list = get_num_mementos(links[0:999])
    #print(len(memento_list))

    memento_age_list = get_uri_age(links[0:999])
    print(memento_age_list)

