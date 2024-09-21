import os
import time
import random
import hashlib
import requests
from colorama import Fore, Style, init

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def art():
    print("\033[1;91m" + r""" ______  _               _    
 | ___ \| |             | |   
 | |_/ /| |  __ _   ___ | | __
 | ___ \| | / _` | / __|| |/ /
 | |_/ /| || (_| || (__ |   < 
 \____/ |_| \__,_| \___||_|\_\
""" + "\033[0m" + "\033[1;92m" + r""" ______                                   
 |  _  \                                  
 | | | | _ __   __ _   __ _   ___   _ __  
 | | | || '__| / _` | / _` | / _ \ | '_ \ 
 | |/ / | |   | (_| || (_| || (_) || | | |
 |___/  |_|    \__,_| \__, | \___/ |_| |_|
                       __/ |              
                      |___/               
""" + "\033[0m" + "\033[1;93m" + r"""  _   _               _                
 | | | |             | |               
 | |_| |  __ _   ___ | | __  ___  _ __ 
 |  _  | / _` | / __|| |/ / / _ \| '__|
 | | | || (_| || (__ |   < |  __/| |   
 \_| |_/ \__,_| \___||_|\_\ \___||_| 
""" + "\033[0m\n\033[1;96m---------------------------------------\033[0m\n\033[1;93mScript created by: Black Dragon Hacker\033[0m\n\033[1;92mJoin Telegram: \nhttps://t.me/BlackDragonHacker007\033[0m\n\033[1;91mVisit my GitHub: \nhttps://github.com/BlackDragonHacker\033[0m\n\033[1;96m---------------------------------------\033[0m\n\033[1;38;2;139;69;19;48;2;173;216;230m--------------[Blum Bot]--------------\033[0m\n\033[1;96m---------------------------------------\033[0m")

def countdown_timer(seconds):
    while seconds > 0:
        mins, secs = divmod(seconds, 60)
        hours, mins = divmod(mins, 60)
        print(f"{Fore.CYAN + Style.BRIGHT}Wait {hours:02}:{mins:02}:{secs:02}", end='\r')
        time.sleep(1)
        seconds -= 1
    print("Wait 00:00:00          ", end='\r')

def load_tokens(filename):
    with open(filename, 'r') as file:
        return [line.strip() for line in file if line.strip()]

def load_proxies(filename):
    with open(filename, 'r') as file:
        return [line.strip() for line in file if line.strip()]

def get_headers(token):
    return {
        "accept": "application/json, text/plain, */*",
        "accept-language": "en-US,en;q=0.9",
        "authorization": token,
        "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
        "sec-ch-ua": "\"Chromium\";v=\"111\", \"Not(A:Brand\";v=\"8\"",
        "sec-ch-ua-mobile": "?1",
        "sec-ch-ua-platform": "\"Android\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site"
    }

def login(query, proxy=None):
    url = f"https://api.freedogs.bot/miniapps/api/user/telegram_auth?invitationCode=pFzjkgjw&initData={query}"
    headers = get_headers("")
    body = {"invitationCode": "pFzjkgjw", "initData": query}

    try:
        response = requests.post(url, headers=headers, json=body, proxies=proxy, allow_redirects=True)
        response.raise_for_status()
        data = response.json()
        token = data.get("data").get("token")
        return token

    except requests.exceptions.RequestException as e:
        print(f"{random_color()}{Style.BRIGHT}Request failed: {e}{Style.RESET_ALL}")
        return None

def data(token, proxy=None):
    url_1 = "https://api.freedogs.bot/miniapps/api/mine/getMineInfo?"
    url_2 = "https://api.freedogs.bot/miniapps/api/user_game_level/GetGameInfo?"
    headers = get_headers(token)
    
    try:
        response_1 = requests.get(url_1, headers=headers, proxies=proxy, allow_redirects=True)
        response_2 = requests.get(url_2, headers=headers, proxies=proxy, allow_redirects=True)
        response_1.raise_for_status()
        response_2.raise_for_status()
        
        data_1 = response_1.json()
        data_2 = response_2.json()
        
        balance = data_1.get("data").get("getCoin")
        collect_seq_no = data_2.get("data").get("collectSeqNo")
        
        print(f"{random_color()}{Style.BRIGHT}Balance: {balance}{Style.RESET_ALL}")
        
        return collect_seq_no

    except requests.exceptions.RequestException as e:
        print(f"{random_color()}{Style.BRIGHT}Request failed: {e}{Style.RESET_ALL}")
        return None

def friends(token, proxy=None):
    url = f"https://api.freedogs.bot/miniapps/api/user_game/friends?page=1&pageSize=50"
    headers = get_headers(token)
    body = {"page": 1, "pageSize": 50}

    try:
        response = requests.post(url, headers=headers, json=body, proxies=proxy, allow_redirects=True)
        response.raise_for_status()
        data = response.json()
        friends = data.get("data").get("count")
        print(f"{random_color()}{Style.BRIGHT}Total Friends: {friends}{Style.RESET_ALL}")

    except requests.exceptions.RequestException as e:
        print(f"{random_color()}{Style.BRIGHT}Request failed: {e}{Style.RESET_ALL}")
        return None

def generate_hash(collect_amount, collect_seq_no):
    static_string = "7be2a16a82054ee58398c5edb7ac4a5a"
    combined = str(collect_amount) + str(collect_seq_no) + static_string
    return hashlib.md5(combined.encode()).hexdigest()

def collect_coins(token, collect_seq_no, total_collect, proxy=None):
    collect_amount = random.randint(60, 70)
    hash_code = generate_hash(collect_amount, collect_seq_no)
    
    url = f"https://api.freedogs.bot/miniapps/api/user_game/collectCoin?collectAmount={collect_amount}&hashCode={hash_code}&collectSeqNo={collect_seq_no}"
    
    headers = get_headers(token)

    try:
        response = requests.post(url, headers=headers, proxies=proxy, allow_redirects=True)
        response.raise_for_status()
        
        response_data = response.json()
        total_collect += collect_amount
        print(f"{random_color()}{Style.BRIGHT}Tapped: {collect_amount} | Total Tapped: {total_collect}/500{Style.RESET_ALL}")
        
        new_collect_seq_no = response_data.get("data", {}).get("collectSeqNo")
        if new_collect_seq_no:
            return new_collect_seq_no, total_collect
        
    except requests.exceptions.RequestException as e:
        print(f"{random_color()}{Style.BRIGHT}Request failed: {e}{Style.RESET_ALL}")
    
    return collect_seq_no, total_collect

def tasks(token, proxy=None):
    url_task_list = "https://api.freedogs.bot/miniapps/api/task/lists?"
    task_complete_url = "https://api.freedogs.bot/miniapps/api/task/finish_task?id={task_id}"
    headers = get_headers(token)
    body = {"page": 1, "pageSize": 50}

    try:
        response = requests.get(url_task_list, headers=headers, json=body, proxies=proxy, allow_redirects=True)
        response.raise_for_status()
        
        data = response.json()
        tasks = data.get("data", {}).get("lists", [])
        
        for task in tasks:
            task_id = task.get("id")
            name = task.get("name")
            is_finished = task.get("isFinish")

            if not is_finished:
                complete_url = task_complete_url.format(task_id=task_id)
                complete_body = {"id": task_id}
                complete_response = requests.post(complete_url, headers=headers, json=complete_body, proxies=proxy)
                
                if complete_response.status_code == 200:
                    print(f"{random_color()}{Style.BRIGHT}Task {name} completed successfully!{Style.RESET_ALL}")
                else:
                    print(f"{random_color()}{Style.BRIGHT}Failed to complete task '{name}'. Status code: {complete_response.status_code}{Style.RESET_ALL}")
            else:
                print(f"{random_color()}{Style.BRIGHT}Task '{name}' is already completed.{Style.RESET_ALL}")

    except requests.exceptions.RequestException as e:
        print(f"{random_color()}{Style.BRIGHT}Request failed: {e}{Style.RESET_ALL}")

def random_color():
    colors = [Fore.GREEN, Fore.YELLOW, Fore.CYAN, Fore.MAGENTA]
    return random.choice(colors)

def main():
    clear_terminal()
    art()
    
    tokens = load_tokens('data.txt')
    proxies = load_proxies('proxy.txt') if os.path.exists('proxy.txt') else None
    total_accounts = len(tokens)
    use_proxy = input(f"{Fore.CYAN}Do you want to use a proxy? (y/n): ").strip().lower()
    run_task = input(f"{Fore.CYAN}Do you want to complete tasks? (y/n): ").strip().lower()
    
    clear_terminal()
    art()
    
    while True:
        print(f"{Fore.MAGENTA}{Style.BRIGHT}Total Accounts: {total_accounts}{Style.RESET_ALL}\n")
        
        for i, query in enumerate(tokens, start=1):
            print(f"{Fore.CYAN}{Style.BRIGHT}------Account No.{i}------{Style.RESET_ALL}")
            proxy = None
            
            if use_proxy == 'y' and proxies:
                proxy = {
                    "http": f"http://{proxies[i % len(proxies)]}",
                    "https": f"http://{proxies[i % len(proxies)]}"
                }
                proxy_parts = proxy['http'].split('@')[-1].split(':')
                formatted_proxy = f"{proxy_parts[0][:4]}.....{proxy_parts[1]}"
                print(f"{Fore.YELLOW}{Style.BRIGHT}Using Proxy: {formatted_proxy}{Style.RESET_ALL}")
    
            try:
                token = login(query, proxy)
                if token:
                    collect_seq_no = data(token, proxy)
                    friends(token, proxy)
                    if run_task == 'y':
                        tasks(token, proxy)
                    
                    total_collect = 0
                    if collect_seq_no:
                        while total_collect < 500:
                            collect_seq_no, total_collect = collect_coins(token, collect_seq_no, total_collect, proxy)
                            time.sleep(3)
                        
            except Exception as e:
                print(f"{random_color()}{Style.BRIGHT}Error processing account {i}: {e}{Style.RESET_ALL}")
                continue
        
        countdown_timer(5 * 60* 60)
        clear_terminal()
        art()

if __name__ == "__main__":
    init()
    main()