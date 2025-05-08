import time

def generate_token():
    secret = "c946dc7eca237f30bc986e1ba5268b173c53e10b"
    static_part = "a81c8fbe3519627b1162731e4fe85841"
    now = int(time.time())
    expire = now + 10800  # 3 hours later

    token = f"{secret}-{static_part}-{expire}-{now}"
    return token

def create_m3u():
    token = generate_token()
    base_url = "http://172.19.178.49:18190/tsports/tracks-a1/index.fmp4.m3u8"
    full_url = f"{base_url}?token={token}"

    with open("tsports_auto.m3u", "w") as f:
        f.write("#EXTM3U\n")
        f.write("#EXTINF:-1,T Sports HD (Auto Token)\n")
        f.write(full_url + "\n")

if __name__ == "__main__":
    create_m3u()
