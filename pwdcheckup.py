#!/usr/bin/env python3
import argparse
import string
import time
import pyfiglet

def print_banner():
    banner = pyfiglet.figlet_format("PwdCheckup")
    print(banner)

def password_strength(password):
    length = len(password)
    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_special = any(char in string.punctuation for char in password)
    
    if length < 8:
        return "Weak - Too short (min 8 characters)"
    if not (has_upper and has_lower and has_digit and has_special):
        return "Weak - Must contain uppercase, lowercase, digit, and special character"
    
    return "Strong"

def estimate_crack_time(password):
    possible_chars = 0
    if any(char.islower() for char in password):
        possible_chars += 26
    if any(char.isupper() for char in password):
        possible_chars += 26
    if any(char.isdigit() for char in password):
        possible_chars += 10
    if any(char in string.punctuation for char in password):
        possible_chars += len(string.punctuation)
    
    combinations = possible_chars ** len(password)
    brute_force_speed = 10**9  # 1 billion guesses per second
    crack_time_seconds = combinations / brute_force_speed
    
    seconds = crack_time_seconds
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    days, hours = divmod(hours, 24)
    months, days = divmod(days, 30)
    years, months = divmod(months, 12)
    
    time_format = []
    if years > 0:
        time_format.append(f"{int(years)} years")
    if months > 0:
        time_format.append(f"{int(months)} months")
    if days > 0:
        time_format.append(f"{int(days)} days")
    if hours > 0:
        time_format.append(f"{int(hours)} hours")
    if minutes > 0:
        time_format.append(f"{int(minutes)} minutes")
    if seconds > 0:
        time_format.append(f"{int(seconds)} seconds")
    
    return ', '.join(time_format) if time_format else "Instantly"

def process_file(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        passwords = [line.strip() for line in f.readlines()]
    
    results = []
    for password in passwords:
        strength = password_strength(password)
        crack_time = estimate_crack_time(password) if "Strong" in strength else "N/A"
        results.append(f"Password: {password}\nStrength: {strength}\nEstimated Crack Time: {crack_time}\n")
    
    if output_file:
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write('\n'.join(results))
    else:
        for result in results:
            print(result)

def main():
    print_banner()
    parser = argparse.ArgumentParser(description="PwdCheckup - Password Strength Checker")
    parser.add_argument("-s", "--single", type=str, help="Check a single password")
    parser.add_argument("-f", "--file", type=str, help="Check passwords from a file")
    parser.add_argument("-o", "--output", type=str, help="Output file to save results")
    
    args = parser.parse_args()
    
    if args.single is not None:
        strength = password_strength(args.single)
        print("Password Strength:", strength)
        if "Strong" in strength:
            crack_time = estimate_crack_time(args.single)
            print("Estimated time to crack:", crack_time)
    elif args.file:
        process_file(args.file, args.output)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()