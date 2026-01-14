import random
import json
import sys

def main():
    try:
        with open('servers.json', 'r') as f:
            lines = [line.strip() for line in f if line.strip()]
        
        if not lines:
            print('::error::No valid servers found in servers.json')
            sys.exit(1)
        
        sample_size = min(200, len(lines))
        sampled_lines = random.sample(lines, sample_size)
        
        servers = []
        for line in sampled_lines:
            try:
                servers.append(json.loads(line))
            except json.JSONDecodeError as e:
                print(f"Skipping invalid JSON line: {e}")
                continue
        
        if len(servers) == 0:
            print('::error::No valid server entries after sampling')
            sys.exit(1)
        
        with open('sample.json', 'w') as out:
            json.dump(servers, out, separators=(',', ':'))
        
        print(f'::notice::Successfully sampled {len(servers)} servers out of {sample_size} attempted')
    
    except Exception as e:
        print(f'::error::Unhandled exception: {str(e)}')
        sys.exit(1)

if __name__ == '__main__':
    main()
