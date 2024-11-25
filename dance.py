import time

carinhas = ["(✿◠‿◠)", "(◕‿◕✿)", "(❀◕‿◕❀)", "(◕‿◕❀)"]
print("💃 Vamos dançar! 💃")

for _ in range(5):
    for carinha in carinhas:
        print("\r" + carinha, end="")
        time.sleep(0.5)
