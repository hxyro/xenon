from libxenon import get_messages, parse_config, is_time

global user, email, password, role_id, channel_id, discord_token, time_delay

def main():
    config = parse_config()
    
    if config == None:
        return 1    
    else:
        user = config['user']
        email = config['email']
        password = config['password']
        mention_role_id = config['mention_role_id']
        channel_id = config['channel_id']
        discord_token = config['discord_token']
        time_delay = config['time_delay']
    
    while True:
        block = get_messages(channel_id, mention_role_id, discord_token)
        timestamp = block['timestamp']
        time_diff = is_time(timestamp)
        _hr = int(time_diff/60)
        _min = int(time_diff%60) 
        print(f"recent message:\n{block['footer']['text']}\t   tag: @IT branch")
        print(f"\nurl: {block['url']}")
        print(f"\ntime difference: {_hr}hour,{_min}min")
        break


if __name__ == "__main__":
    main()
