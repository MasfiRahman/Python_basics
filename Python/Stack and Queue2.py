from collections import deque

bank = deque(["Masfi","Mahi","Ismum"])
print(bank)
bank.popleft()
print(bank)
bank.popleft()
bank.popleft()
if not bank:
    print("No person left")