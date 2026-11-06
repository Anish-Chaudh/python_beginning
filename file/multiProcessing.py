import multiprocessing
import os
import requests

def downloadFile(url, name):
    print(f"Started Downloading {name}")
    response = requests.get(url, timeout=30)
    response.raise_for_status()
    with open(f"Demo/file{name}.jpg", "wb") as f:
        f.write(response.content)
    print(f"Finished Downloading {name}")

if __name__ == "__main__":
    os.makedirs("Demo", exist_ok=True)
    url = "https://picsum.photos/2000/3000"
    pros = []
    for i in range(5):
        p = multiprocessing.Process(target=downloadFile, args=(url, i))
        p.start()
        pros.append(p)

    for p in pros:
        p.join()