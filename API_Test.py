import requests
import json
from colorama import init, Fore, Style
init(autoreset=True)
def print_header(text):
    print(f"\n{Fore.CYAN}=== {text} ==={Style.RESET_ALL}")

def print_separator():
    print(f"{Fore.BLUE}{'—' * 40}{Style.RESET_ALL}\n")

base_url = "https://api.github.com" 
print(f"{Fore.GREEN}Welcome to GitHub User Info Fetcher!{Style.RESET_ALL}")
username=input("Enter the Github Username you want to search for...") 
response = requests.get(f"{base_url}/users/{username}")
if response.status_code == 200:
    user_data=response.json()

    while True:
        print_header("MENU")
        print (f"{Fore.WHITE}1- Name")
        print ("2- Repositories")
        print ("3- Followers")
        print ("4- Following")
        print ("5- All info")
        print (f"q- Exit {Style.RESET_ALL}")
        choice = input(f"\n {Fore.YELLOW}Enter your choice: {Style.RESET_ALL}")
        print("----------------------------\n")
        if choice == '1':
            print("Fetching Name...")
            print(f"{Fore.GREEN}Name: {user_data['name']} {Style.RESET_ALL}")
            print("----------------------------\n")
        elif choice == '2':
            print("Fetching repos info...")
            repos_response = requests.get(f"{base_url}/users/{username}/repos")
            if repos_response.status_code == 200:
                repos = repos_response.json()
                print(f"Number of repos: {len(repos)}")
                for repo in repos:
                    print(f"- {repo['name']}")
            print("----------------------------\n")
        elif choice == '3':
            print("Fetching followers info...")
            followers_response = requests.get(f"{base_url}/users/{username}/followers")
            if followers_response.status_code == 200:
                followers = followers_response.json()
                print(f"Number of followers: {len(followers)}")
            print("----------------------------\n")
        elif choice == '4':
             print("Fetching following info...")
             following_response= requests.get(f"{base_url}/users/{username}/following")
             if following_response.status_code== 200:
                 following= following_response.json()
                 print(f"Number of following: {len(following)}")
             print("----------------------------\n")
        elif choice == '5':
            print("Fetching all info...")
            print(json.dumps(user_data, indent=2))
            print("----------------------------\n")
        elif choice == 'q':
            print("Exiting...")
            break 
        else:
            print("Invalid choice. Please try again.")
elif response.status_code == 404:
    print(f"Error: User '{username}' not found.")
else:
    print(f"Error: {response.status_code}")