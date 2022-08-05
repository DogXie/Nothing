"""这是一个一个真正的AI"""
from time import sleep
from random import randint
for _ in range (7):
    sleep (0.05)
    print ("\r┃",end = "")
    sleep(0.1)
    print ("\r╱",end = "")
    sleep (0.1)
    print ("\r－",end = "")
    sleep (0.1)
    print ("\r╲",end = "")
    sleep(0.05)
sleep (0.05)
sleep (3)
print ()
print ("您好呀~")
sleep (0.6)
user = input ("""我应该叫您什么呢？
""")
print(f"好的呢,{user}")
cz = input (f"""所以...你想要干什么呢？{user}。
""")
a = 1
while True: #操作持续进行~~
    if a != 1:
        sleep (2)
        cz = input ("""还有什么要说的吗？
""")
    if cz in "谁":
        print (f"{user},我是您的专属AI呀~")
    elif cz in "爱":
        b = randint (0,3)
        print ("唔....")
        sleep (1)
        if b == 1:
            print (f"我也爱你，{user}")
        elif b == 2:
            print (f"永远爱着{user}~~")
        else:
            print ("mua,爱你哟~")
    else :
        print (cz.strip("吗？?") + "！")
    a = 2