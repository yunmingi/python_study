import random
energy = 10
print("당신의 에너지는 10입니다. 공격을 시작하세요!")

while energy >0:
    input("공격하려면 엔터를 누르세요...")
    damage = random.randit(1,3)
    energy -= damage 
    print(f"당신은 {damage}의 데미지를 받았습니다. 현재 에너지는 {energy}입니다.")
    
    if energy <= 0:
        print("당신은 죽었습니다.게임 오버!")
        
        