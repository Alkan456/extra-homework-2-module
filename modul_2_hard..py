import random
def get_code():
    number = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    numbers = list(range(3,21))
    code = random.choice(numbers)
    return code

def get_password(n):
    passdict = {}
    passdict.update({3:12, 4:13, 5:1423, 6:121524, 7:162534, 8:13172635, 9:1218273645})
    passdict.update({10:141923283746, 11:11029384756, 12:12131511124210394857})
    passdict.update({13:112211310495867, 14:1611325212343114105968})
    passdict.update({15:1214114232133124115106978, 16:1317115262143531341251161079})
    passdict.update({17:11621531441351261171089})
    passdict.update({18:12151811724272163631545414513612711810})
    passdict.update({19:118217316415514613712811910})
    passdict.update({20:13141911923282183731746416515614713812911})
    password =passdict.get(n)
    return password

n = get_code()
print('Шифр:', n)
