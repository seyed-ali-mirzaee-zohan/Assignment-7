import pyfiglet
from termcolor import colored
result = pyfiglet.figlet_format("google translation", font = "digital" )
print(result)
print(colored(' Hello, Welcome to the translator software ', 'red', attrs=['reverse', 'blink']))
print()
print(colored(' The following options are now available : ', 'white', attrs=['reverse', 'blink']))
print()
print(colored(' 1 : Add new word      ', 'green', attrs=['reverse', 'blink']))
print(colored(' 2 : English ⇨ Persian ', 'yellow', attrs=['reverse', 'blink']))
print(colored(' 3 : Persian ⇨ English ', 'green', attrs=['reverse', 'blink']))
print(colored(' 4 : Exit software     ', 'yellow', attrs=['reverse', 'blink']))
print()
enter=int(input( "Please enter your desired number : " ))

# خوانش فایل
translate=open('translate.txt','r')
translate1=translate.read()
translate2=translate1.split("\n")
information_bank=[]
for i in range(0,len(translate2),2):
    information_bank.append({'english':translate2[i],'persian':translate2[i+1]})
translate.close()

# تابع نمایش بانک اطلاعاتی
def show_information_bank():
    for i in range(len(information_bank)):
        print(information_bank[i])

# تابع افزودن کلمات
def add_new_word():
    while True:
        english_word=input('enter english word : ')
        persian_word=input('enter persian word : ')
        for i in range(len(information_bank)):
            if english_word==information_bank[i]['english'] or persian_word==information_bank[i]['persian']:
                print(colored(' The word entered is available in the information bank ', 'red', attrs=['reverse', 'blink']),'\n')
                print(colored(' Do you want to watch ? ', 'yellow', attrs=['reverse', 'blink']),'\n')
                print(colored(' 1 : Yes ', 'green', attrs=['reverse', 'blink']),colored(' 2 : NO ', 'red', attrs=['reverse', 'blink']))
                enter_1=int(input('Please enter your desired number : '))
                print()
                if enter_1==1:
                    print(information_bank[i]['english'],information_bank[i]["persian"])
                    break
                if enter_1==2:
                    break
        else :
            information_bank.append({"english": english_word, "persian": persian_word})
            translate = open("translate.txt", "a")
            translate.write(f"\n{english_word} \n{persian_word}")
            print(colored("Word successfully added to information bank", color="green"))
        print(colored(' do you want to continue ? ', 'white', attrs=['reverse', 'blink']),'\n')
        print(colored(' 1 : Yes ', 'green', attrs=['reverse', 'blink']),colored(' 2 : NO ', 'red', attrs=['reverse', 'blink']))
        choice=int(input('Please enter your desired number : '))
        if choice==2:
            break

# تابع ترجمه از انگلیسی به فارسی
def english_to_persian():    
    sentence = input("Please enter your sentence : ")
    english_sentence = sentence.split(" ")
    for i in range(len(english_sentence)):
        for j in range(len(information_bank)):
            if information_bank[j]["english"] == english_sentence[i]:
                print(colored(information_bank[j]["persian"], color="green"), end=" ")
                break
        else:
            print(colored(english_sentence[i], color="red"), end=" ")

# تابع ترجمه از فارسی به انگلیسی
def persian_to_english():    
    sentence = input("لطفاً جمله خود را وراد نمائید : ")
    persian_sentence = sentence.split(" ")
    for i in range(len(persian_sentence)):
        for j in range(len(information_bank)):
            if information_bank[j]["persian"] == persian_sentence[i]:
                print(colored(information_bank[j]["english"], color="green"), end=" ")
                break
        else:
            print(colored(persian_sentence[i], color="red"), end=" ")

# فراخوانی تابع افزودن کلمات
if enter==1:
    add_new_word()

# فراخوانی تابع ترجمه از انگلیسی به فارسی
if enter==2:
    english_to_persian()

# فراخوانی تابع ترجمه از فارسی به انگلیسی
if enter==3:
    persian_to_english()

# فراخوانی تابع خروج از نرم افزار
if enter==4:
    exit()