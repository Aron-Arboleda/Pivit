# pylint: disable = pointless-string-statement, trailing-whitespace, invalid-name, line-too-long, redefined-outer-name, duplicate-key, unspecified-encodingm, consider-using-dict-items

import time
import random
                    
# Methods
def main():
    Accountsfilepath = "Pivit\ProductivityAccounts.txt"
    UsersDatafilepath = "Pivit\ProductivityUsersData.txt"
    
    class Productivity:
        def __init__(self, unm, nm, lvl, exp, mp, cns, achm, tsk, rnk, pt, wpn, up):
            self.username = unm
            self.name = nm
            self.level = int(lvl)
            self.experience = int(exp)
            self.mpoints = int(mp)
            self.coins = int(cns)
            self.achievement = achm
            self.tasks = tsk
            self.rank = rnk
            self.pet = pt
            self.weapon = wpn
            self.updated = up

    # Class methods
        def Welcome(self):
            print()
            print("🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦⬜⬜🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦⬜⬜")
            print("⬜🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦⬜⬜⬜⬜⬜🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦⬜⬜⬜⬜")
            print("⬜⬜⬜🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦⬜⬜⬜⬜⬜⬜⬜⬜🟦🟦🟦🟦🟦🟦🟦⬜⬜🟦⬜⬜⬜⬜⬜")
            print("⬜⬜⬜⬜🟦🟦🟦🟦🟦🟦🟦⬜⬜⬜⬜🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦⬜⬜")
            print("⬜🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦⬜⬜")
            print("🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦⬜⬜⬜⬜")
            print("🟦⬜⬜⬜⬜⬜🟦🟦⬜⬜🟦⬜⬜🟦🟦⬜⬜🟦⬜⬜🟦⬜⬜⬜⬜⬜⬜🟦🟦🟦⬜⬜⬜⬜⬜🟦")
            print("🟦⬜⬜⬜⬜⬜⬜🟦⬜⬜🟦⬜⬜🟦🟦⬜⬜🟦⬜⬜🟦⬜⬜⬜⬜⬜⬜🟦🟦🟦🟦🟦🟦🟦🟦🟦")
            print("🟦⬜⬜🟦🟦⬜⬜🟦⬜⬜🟦⬜⬜🟦🟦⬜⬜🟦⬜⬜🟦🟦🟦⬜⬜🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦")
            print("🟦⬜⬜🟦🟦⬜⬜🟦⬜⬜🟦⬜⬜🟦🟦⬜⬜🟦⬜⬜🟦🟦🟦⬜⬜🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦")
            print("🟦⬜⬜⬜⬜⬜🟦🟦⬜⬜🟦⬜⬜🟦🟦⬜⬜🟦⬜⬜🟦🟦🟦⬜⬜🟦🟦🟦🟦🟦🟦🟩🟩🟦🟦🟦")
            print("🟦⬜⬜⬜⬜🟦🟦🟦⬜⬜🟦⬜⬜🟦🟦⬜⬜🟦⬜⬜🟦🟦🟦⬜⬜🟦🟦🟦🟦🟦🟩🟩🟩🟩🟦🟦")
            print("🟦⬜⬜🟦🟦🟦🟦🟦⬜⬜🟦⬜⬜🟦🟦⬜⬜🟦⬜⬜🟦🟦🟦⬜⬜🟦🟦🟦🟦🟩🟩🟩🟩🟩🟩🟦")
            print("🟦⬜⬜🟦🟦🟦🟦🟦⬜⬜🟦🟦⬜⬜⬜⬜🟦🟦⬜⬜🟦🟦🟦⬜⬜🟦🟦🟦🟦🟦🟦🟫🟫🟦🟦🟦")
            print("🟦⬜⬜🟦🟦🟦🟦🟦⬜⬜🟦🟦🟦⬜⬜🟦🟦🟦⬜⬜🟦🟦🟦⬜⬜🟦🟦🟦🟦🟦🟦🟫🟫🟦🟦🟦")
            print("🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩")
            print("🟩🟩🟫🟫🟫🟫🟩🟫🟫🟫🟫🟫🟫🟫🟩🟩🟩🟩🟩🟫🟫🟫🟩🟩🟫🟫🟫🟫🟩🟩🟫🟫🟩🟩🟩🟩")
            print("🟩🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟩🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟩🟫🟫")
            print("🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫")
            print("⬛🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫⬛🟫🟫🟫🟫🟫🟫🟫⬛")
            print("⚫⬛⬛⬛🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫⚫⬛⬛⬛🟫🟫🟫🟫🟫🟫🟫⚫⬛🟫🟫🟫🟫🟫🟫⚫⬛")
            print()
            print("⬛⬜⬛⬜⬛⬜⬜⬜⬛⬜⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛")
            print("⬛⬜⬛⬜⬛⬛⬜⬛⬛⬜⬛⬛🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨⬛")
            print(f"⬛⬜⬜⬜⬛⬛⬜⬛⬛⬜⬛⬛🔶 {self.name}")
            print("⬛⬜⬛⬜⬛⬛⬜⬛⬛⬛⬛⬛🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨⬛")
            print("⬛⬜⬛⬜⬛⬜⬜⬜⬛⬜⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛")
            print()
                
        def profile(self):
            x = ""
            print("\n🔲🔳🔲🔳🔲🔳🔲🔳🔲🔳🔲🔳🔲🔳🔲🔳🔲🔳🔲🔳🔲🔳🔲🔳🔲🔳🔲🔳🔲🔳🔲🔳\n")
            print(f"🔶 {self.username} — profile")
            print(f"  🔷 Rank: {RANK_ICON.get(self.rank)} {self.rank}")
            for i in LEVELS:
                if self.experience in i:
                    print(f"  🔷 Level: {LEVELS.get(i)} ({round((self.experience / i.stop)*100,2)}%)")
                    print(f"  🔷 Exp: {self.experience:,}/{i.stop:,}")
                    break
            print(f"  🔷 Motivation Points✨: 🤩 {self.mpoints:,}")
            print(f"  🔷 Coins: 🟡 {self.coins:,}")
            a = []
            if len(self.pet) == 0: 
                x = "No pet"
                print(f"  🔷 Pet/s: {x}")  
            else:
                for i in self.pet:
                    a.append(f"{SHOP.get(i.lower())[0]} {i}")
                a = ", ".join(a)
                print(f"  🔷 Pet/s: {a}")
            
            b = []        
            if len(self.weapon) == 0: 
                x = "No weapon"
                print(f"  🔷 Weapon/s: {x}")
            else:
                for i in self.weapon:
                    b.append(f"{SHOP.get(i.lower())[0]} {i}")
                b = ", ".join(b)
                print(f"  🔷 Weapon/s: {b}")
            
            print("\n🔲🔳🔲🔳🔲🔳🔲🔳🔲🔳🔲🔳🔲🔳🔲🔳🔲🔳🔲🔳🔲🔳🔲🔳🔲🔳🔲🔳🔲🔳🔲🔳")
        def commands(self):
            print('\n⌨  Commands:')
            print('note: Add "/" before any command')
            print('⬜ "/commands" - to show program commands')
            print('⬜ "/profile" - to show profile and stats')
            print('⬜ "/achievements" - to see achievements')
            print('⬜ "/shop" - to buy items')
            print('\t⚪ "/back" - to back')
            print('\t⚪ "/buy" - to add')
            print('⬜ "/quest" - to show daily quests')
            print('⬜ "/update" - to update infos')
            print('\t⚪ "/back" - to back')
            print('\t⚪ "/add" - to add')
            print('\t⚪ "/delete" - to delete')
            print('\t⚪ "/rewrite" - to rewrite an item')
            print('\t⚪ "/check" - to check or uncheck an item')
            print()    
            print('🟧 "/sign out" to sign out of this account')               
            print('🟥 "/exit" to quit.')
        def achievements(self):
            print("\n🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨")
            print("\n✨🏆✨ ACHIEVEMENTS ✨🏆✨ ")
            for i in self.achievement: print(i)
            print("\n🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨\n")
        def shop(self):
            def strike(text):
                result = ''
                for c in text:
                    result = result + c + '\u0336'
                return result
            print("\n🟦⬜⬜🟥⬜⬜🟦⬜⬜🟦⬜⬜🟥⬜⬜🟦⬜⬜🟦⬜⬜🟥⬜⬜🟦⬜⬜🟦⬜⬜🟥⬜⬜🟦")
            print("                        ⬜   🛒 SHOP 🛒   ⬜    ")
            print("                  🟦⬜⬜⬜⬜🟥⬜⬜⬜⬜🟥⬜⬜⬜⬜🟦")
            print("\nPets: ")
            for i in SHOP:
                if SHOP.get(i)[2] == "pet":
                    if i.title() in self.pet:
                        print("\033[0;30;40m" + strike(f"\t🤩 (+ {SHOP.get(i)[3]:,}) {i.title():>5} {SHOP.get(i)[0]}  --- 🟡 {SHOP.get(i)[1]:,}") + " (sold)" + "\033[0;37;40m")
                    else: 
                        print(f"\t🤩 (+ {SHOP.get(i)[3]:,}) {i.title():>5} {SHOP.get(i)[0]}  --- 🟡 {SHOP.get(i)[1]:,}")
            print("Weapons: ")
            for i in SHOP:
                if SHOP.get(i)[2] == "weapon":
                    if i.title() in self.weapon:
                        print("\033[0;30;40m" + strike(f"\t🤩 (+ {SHOP.get(i)[3]:,}) {i.title():>5} {SHOP.get(i)[0]}  --- 🟡 {SHOP.get(i)[1]:,}") + " (sold)" + "\033[0;37;40m")
                    else:
                        print(f"\t🤩 (+ {SHOP.get(i)[3]:,}) {i.title():>5} {SHOP.get(i)[0]}  --- 🟡 {SHOP.get(i)[1]:,}")
            print("Foods: ")
            for i in SHOP:
                if SHOP.get(i)[2] == "food":
                    print(f"\t(+ {SHOP.get(i)[3]:,} Exp) {i.title():>5} {SHOP.get(i)[0]}  --- 🟡 {SHOP.get(i)[1]:,}")

            print("\n🟦⬜⬜🟥⬜⬜🟦⬜⬜🟦⬜⬜🟥⬜⬜🟦⬜⬜🟦⬜⬜🟥⬜⬜🟦⬜⬜🟦⬜⬜🟥⬜⬜🟦")
            print()
            print(f"🔶 {self.name} — 🟡 {self.coins:,}")
            while True:
                print("\n⬜⬜🟥⬜⬜🟦⬜⬜🟦⬜⬜🟥⬜⬜🟦⬜⬜🟦⬜⬜🟥⬜⬜🟦⬜⬜🟦⬜⬜🟥⬜⬜")
                print("🟨✨🟨🟨🟨⬜              🏪 Shopping Hall          ⬜🟨🟨🟨✨🟨")
                print("⬜⬜🟥⬜⬜🟦⬜⬜🟦⬜⬜🟥⬜⬜🟦⬜⬜🟦⬜⬜🟥⬜⬜🟦⬜⬜🟦⬜⬜🟥⬜⬜")
                print()
                print('⌨  Commands: ("/back", "/buy", "/commands")')
                c = Filter(input("\n🈴  /"), "\n🈴  /", ["back","buy","commands"])
                if c == "back":
                    break
                output_function = getattr(Productivity, c)
                output_function(self)            
        def quest(self):
            self.reset_check()
            print("\n⬜🟪🟪🟪⬜⬜🟪🟪🟪⬜⬜🟪🟪🟪⬜")
            print("\n📝📃📝 QUESTS 📝📃📝")
            for i in self.tasks:
                a = i.split(" ")
                print(f"  {checkboxes.get(a[0])} {a[1]}")
            print("\n⬜🟪🟪🟪⬜⬜🟪🟪🟪⬜⬜🟪🟪🟪⬜\n")    
        def update(self):
            class_var = {
                1:self.tasks,
                2:self.achievement
            }
            while True:
                print("⬜🟪🟪🟪🟪🟪⬜⬜🟪🟪🟪🟪⬜⬜🟪🟪🟪🟪⬜⬜🟪🟪🟪🟪⬜⬜🟪🟪🟪🟪🟪⬜")
                print("🟨✨🟨🟨🟨⬜               🏫 Barracks              ⬜🟨🟨🟨✨🟨")
                print("⬜🟪🟪🟪🟪🟪⬜⬜🟪🟪🟪🟪⬜⬜🟪🟪🟪🟪⬜⬜🟪🟪🟪🟪⬜⬜🟪🟪🟪🟪🟪⬜")
                print("\nYou can update your infos here. Choose option below.")
                print()
                print("⬜🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪⬜")
                print("  1️⃣  Quests")
                print("  2️⃣  Achievements")
                print("  3️⃣  Back")
                print("⬜🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪⬜")
                choice = Filter(input("\n♐  "), "\n♐  ", range(1,4))
                if choice == 3:
                    print("Back to Main hall.")
                    break
                while True:
                    c = ""
                    if choice == 1:
                        self.reset_check()
                        self.show(class_var.get(choice))
                        print('\n⌨  Commands: ("/back","/add","/delete","/check","/rewrite","/commands")')
                        c = Filter(input("\n♐  /"), "♐  /", ["back","add","delete","check","rewrite","commands"])
                    elif choice == 2:
                        self.show(class_var.get(choice))
                        print('\n⌨  Commands: ("/back","/add","/delete","/rewrite","/commands")')
                        c = Filter(input("\n♐  /"), "♐  /", ["back","add","delete","rewrite","commands"])
                    else:print("No such option")
                
                    if c == "back":
                        break
                    elif c == "commands":
                        self.commands()
                    else:
                        output_function = getattr(Productivity, c)
                        output_function(self, class_var.get(choice))  
                        self.updated = time.asctime()          

    # Class sub-methods
        def buy(self):
            Items = list(SHOP)
            x = Filter(input("Item: ").lower(), "Item: ", Items)
            while x.title() in (self.pet + self.weapon):
                print("Item already bought, pick another item.")
                x = Filter(input("Item: ").lower(), "Item: ", Items)
            a = Filter(input(f"Are you sure to buy {SHOP.get(x)[0]} {x.title()} for 🟡 {SHOP.get(x)[1]:,}?(y/n): "), "Item: ", ["y","n"])
            if a == "y":
                if self.coins < SHOP.get(x)[1]:
                    print("Insufficient coins.")
                else:
                    if SHOP.get(x)[2] == "pet": 
                        self.pet.append(x.title())
                        print(f"WAAAAWWWW!! You just got a new pet! ({SHOP.get(x)[0]} {x})")
                        self.mpoints += SHOP.get(x)[3]
                        print(f"(+ 🤩 {SHOP.get(x)[3]:,})")
                    elif SHOP.get(x)[2] == "weapon":
                        self.weapon.append(x.title())
                        print(f"WOAAAHHH LAKAS NAMAN NYARN!! You just got a new weapon! ({SHOP.get(x)[0]} {x})")
                        self.mpoints += SHOP.get(x)[3]
                        print(f"(+ 🤩 {SHOP.get(x)[3]:,})")
                    elif SHOP.get(x)[2] == "food":
                        self.experience += SHOP.get(x)[3]
                        print(f"Mmmm sharap HAHAHHAH (+ {SHOP.get(x)[3]:,} Exp)")
                    self.coins -= SHOP.get(x)[1]
                    print(f"Total Coins: 🟡 {self.coins:,} (- 🟡 {SHOP.get(x)[1]:,})")
                    time.sleep(2)
                    save()
            else:
                print("Ok, come back soon!")
        def add(self, x):
            n = Filter(input("Quantity: "), "Quantity: ", range(11))
            total_exp = 0
            total_coins = 0
            extra_exp = 0
            extra_coins = 0
            for i in range(n):
                if x == self.tasks:
                    task = input("◻ ")
                    x.append(f"undone {task}")
                elif x == self.achievement:
                    ach = input("- ")
                    x.append(ach)
                    total_exp += random.randint(100000, 110000)
                    total_coins += random.randint(15000, 20000)
                    extra_exp += self.mpoints
                    extra_coins += self.mpoints // 2
            self.experience += total_exp + extra_exp
            self.coins += total_coins + extra_coins
            print(f"\n(+ {total_exp:,} Exp)")
            print(f"(+ 🟡 {total_coins:,})")
            print(f"and (+ {extra_exp:,} Exp) (+ 🟡 {extra_coins:,}) bonus from Motivation Points (🤩 )")
            self.levelup_check()
            save()  
        def delete(self, x):
            n = Filter(input("How many items? "), "How many items? ", range(1, len(x) + 1))
            for i in range(1, n + 1):
                p = int(list(str(i))[-1])
                y = Filter(input(f"Enter the number of the {i}{PLACE.get(p)} item: "), f"Enter the number of the {i}{PLACE.get(p)} item: ", range(1, len(x) + 1))
                x.pop(y - 1)
                save()
                self.show(x)       
        def rewrite(self, x):
            if x == self.tasks:  
                y = Filter(input("Number of quest: "), "Number of quest: ", range(1, len(x) + 1))
                x[y - 1] = ((x[y - 1].split(" "))[0]) + " " + input("Replacement: ")
                print("(A quest have been edited.)")
            elif x == self.achievement:
                y = Filter(input("Number of achievement: "), "Number of achievement: ", range(1, len(x) + 1))
                x[y - 1] = input("Replacement: ")
                print("(An achievement have been edited.)")
            save()    
        def check(self, x):
            reciprocal = {
                "done":"undone",
                "undone":"done"
            }
            
            if x == self.tasks:
                n = Filter(input("How many? "), "How many? ", range(1, len(x) + 1))
                total_exp = 0
                total_coins = 0
                extra_exp = 0
                extra_coins = 0
                for i in range(1, n + 1):
                    p = int(list(str(i))[-1])
                    y = Filter(input(f"Number of {i}{PLACE.get(p)} quest: "), f"Number of {i}{PLACE.get(p)} quest: ", range(1, len(x) + 1))
                    x[y - 1] = reciprocal.get((x[y - 1].split(" "))[0]) + " " + (x[y - 1].split(" "))[1]
                    if x[y - 1].split(" ")[0] == "done":
                        total_exp += random.randint(5000, 5501)
                        total_coins += random.randint(800, 1001)
                        extra_exp += self.mpoints
                        extra_coins += self.mpoints // 3
                self.experience += total_exp + extra_exp
                self.coins += total_coins + extra_coins
                print(f"\n(+ {total_exp:,} Exp)")
                print(f"(+ 🟡 {total_coins:,})")
                print(f"and (+ {extra_exp:,} Exp) (+ 🟡 {extra_coins:,}) bonus from Motivation Points (🤩 )")
                self.levelup_check()
            save()    
        def levelup_check(self):
            x = self.level
            for i in LEVELS:
                if self.experience in i:
                    self.level = LEVELS.get(i)
                    break
            if x != self.level:
                print("\nLEVEL UP GAGU! SHEEEETTTT!! UGH UGH")
                print(f"(Level: {self.level} ⏫)\n")
                
            y = self.rank
            for i in RANK:
                if self.level in i:
                    self.rank = RANK.get(i)
                    break
            if y != self.rank:
                print("\nRANK UPPP PUTANGINAA MOOOOOOOO AAAAAAAHHHHHHHHH HAWHAHAHHAHHAHAHAH LASNaSDALWNDLAWD")
                print(f"(Rank: {RANK_ICON.get(self.rank)} {self.rank} ⏫)\n")
        def show(self, x):
            count = 1
            if x == self.tasks:
                print("\n📝📃📝 QUESTS 📝📃📝")
                for i in x:
                    a = i.split(" ")
                    print(f"{count}.  {checkboxes.get(a[0])} {a[1]}")
                    count += 1
            elif x == self.achievement:
                print("\n✨🏆✨ ACHIEVEMENTS ✨🏆✨ ")
                for i in x:
                    print(f"{count}.  {i}")
                    count += 1
        def reset_check(self):
            x = self.updated
            x = " ".join(x.split()).split(" ")[2]
            y = time.asctime()
            y = " ".join(y.split()).split(" ")[2]
            if x != y:
                for i in self.tasks:
                    a = i.split(" ")
                    if a[0] == "done":
                        self.tasks[self.tasks.index(i)] = f"undone {a[1]}"
            save()
                                   
    def save():
        with open(UsersDatafilepath, "w") as f:
            f.write(f"\nLast saved on: {time.asctime()}\n-----------------------------")
            for i in USERSDATA:
                y = f"\n{i.username}\n\tName: {i.name}\n\tLevel: {i.level}\n\tExperience: {i.experience}\n\tMotivation Points: {i.mpoints}\n\tCoins: {i.coins}\n\tAchievements: {i.achievement}\n\tTasks: {i.tasks}\n\tRank: {i.rank}\n\tPet: {i.pet}\n\tWeapon: {i.weapon}\n\tLast Updated on: {i.updated}\n-----------------------------"
                f.write(y)
    def Filter(x, prompt, choices):
        y = x
        if ("".join(list(map(lambda a: str(a), choices))).isdigit()):
            while (y not in list(map(lambda a: str(a), choices))):
                print("Invalid input. ")
                y = input(prompt)
            return int(y)
        else: 
            while y.lower() not in list(map(lambda a: a.lower(), choices)):
                print("Invalid input. ")
                y = input(prompt)
            return y
    def Login():
        print()
        print("🟦🟦⬜⬛⬛⬛⬛⬛⬛⬛⬛⬛🟦🟦⬜")
        print("🟦🟩🟦   📝 Log In 📝   🟦🟩🟦")
        print("🟩🟫🟩⬛⬛⬛⬛⬛⬛⬛⬛⬛🟩🟫🟩")
        print()
        
        USERNAME = Filter(input("Username: ").lower(), "Username: ", USERNAMES)
        PASSWORD = input("Password: ")
        tries = 5
        while (PASSWORD != ACCOUNTS.get(USERNAME)):
            tries -= 1 
            print("You have entered a wrong password. ")
            if tries == 0:
                c = Filter(input("Would you like to leave?(y/n)"), "Would you like to leave?(y/n)", ["y","n"])
                if c == "y":
                    left = True
                    break
                else:
                    tries = 5
            PASSWORD = input("Password: ")
        if (PASSWORD == ACCOUNTS.get(USERNAME)):
            with open(Accountsfilepath) as f:
                content = f.read().split("-----------------------------")
                content.remove("")
                x = content[0].splitlines()
                x[0] = f"Active Account: {USERNAME}"
                content[0] = f"\n{x[0]}\n"
            with open(Accountsfilepath, "w") as f:
                x = "-----------------------------".join(content)
                f.write(f"{x}-----------------------------")
            AC = ""
            for i in USERSDATA:
                if i.username == active_user:
                    AC = i
                    break
            return AC
        elif (left):
            return "none"        
    def Signup():
        print()
        print("🟦🟦⬜⬛⬛⬛⬛⬛⬛⬛⬛⬛🟦🟦⬜")
        print("🟦🟩🟦   📝 Sign Up 📝  🟦🟩🟦")
        print("🟩🟫🟩⬛⬛⬛⬛⬛⬛⬛⬛⬛🟩🟫🟩")
        print()
        FirstName = input("First Name: ")
        LastName = input("Last Name: ")
        Name = f"{FirstName} {LastName}"
        UserName = input("Username: ")
        while UserName in USERNAMES:
            print("**Username already exist.**")
            UserName = input("Username: ")
        Password = input("Password: ")
        x = input("Enter password again: ")
        while Password != x:
            print("Wrong input. try again")
            Password = input("Password: ")
            x = input("Enter password again: ")
        
        with open(UsersDatafilepath) as f:
            content = f.readlines()
            content.append(f"\n{UserName}\n\tName: {Name}\n\tLevel: 1\n\tExperience: 500\n\tMotivation Points: 80\n\tCoins: 100\n\tAchievements: []\n\tTasks: []\n\tRank: Beginner\n\tPet: []\n\tWeapon: []\n\tLast Updated on: (not opened)\n-----------------------------")
        with open(UsersDatafilepath, "w") as f:
            for i in content:
                f.write(i)
        
        with open(Accountsfilepath) as f:
            content = f.readlines()
            content.append(f"\nUsername: {UserName}\nPassword: {Password}\n-----------------------------")
        with open(Accountsfilepath, "w") as f:
            for i in content:
                f.write(i)
        
        USERNAMES.append(UserName)
        USERSDATA.append(Productivity(UserName, Name, 1, 500, 80, 100, [], [], "Beginner", [], [], "(not opened)"))
        ACCOUNTS[UserName] = Password
        
        print("Account Created! Proceed to Log In page. ")
        AC = Login()
        return AC
    def Signout():
        c = Filter(input("Are you sure to sign out of this account?(y/n): "), "Are you sure to sign out of this account?(y/n): ", ["y","n"])
        if c == "y":
            with open(Accountsfilepath) as f:
                content = f.read().split("-----------------------------")
                content.remove("")
                x = content[0].splitlines()
                x[0] = "Active Account: none"
                content[0] = f"\n{x[0]}\n"
            with open(Accountsfilepath, "w") as f:
                x = "-----------------------------".join(content)
                f.write(f"{x}-----------------------------")
            print("Account signed out. ")
    def Startup():
        with open(UsersDatafilepath) as f:
            content = f.read().split("-----------------------------")
            content.remove("")
        for i in content:
            x = "".join(i.split("\t")).splitlines()
            x.remove("")
            
            if "Last saved on" in x[0]:
                continue

            unm = x[0]
            nm = (x[1].split(": "))[1]
            lvl = (x[2].split(": "))[1]
            exp = (x[3].split(": "))[1]
            mp = (x[4].split(": "))[1]
            cns = (x[5].split(": "))[1]
            achm = eval((x[6].split(": "))[1])
            tsk = eval((x[7].split(": "))[1])
            rnk = (x[8].split(": "))[1]
            pt = eval((x[9].split(": "))[1])
            wpn = eval((x[10].split(": "))[1])
            up = (x[11].split(": "))[1]
            up = " ".join(up.split())
            USERNAMES.append(unm)
            USERSDATA.append(Productivity(unm, nm, lvl, exp, mp, cns, achm, tsk, rnk, pt, wpn, up))

        with open(Accountsfilepath) as f:
            content = f.read().split("-----------------------------")
            content.remove("")
        for i in content:
            x = i.splitlines()
            x.remove("")
            if "Active Account" in x[0]:
                continue
            ACCOUNTS[x[0].split(": ")[1]] = x[1].split(": ")[1]

    # ----------------------------------------------------- RESOURCES STARTUP --------------------------------------------------------

    USERNAMES = []
    USERSDATA = []
    ACCOUNTS = {}

    Startup()

    PLACE = {1:"st",2:"nd",3:"rd",4:"th",5:"th",6:"th",7:"th",8:"th",9:"th",0:"th"}
    SHOP = {
        "golden retriever":["🦮", 50000, "pet", 800],
        "sloth":["🦥", 250000, "pet", 1500],
        "llama":["🦙", 500000, "pet", 3000],
        "eagle":["🦅", 1000000, "pet", 5000],
        "almighty shenron":["🐉", 5000000, "pet", 10000],
        "knife":["🔪", 25000, "weapon", 500],
        "bow and arrow":["🏹", 400000, "weapon", 2000],
        "mythical water gun":["🔫", 1000000, "weapon", 10000],
        "sandwich":["🥪", 100, "food", 1000],
        "cup noodles":["🥡", 1000, "food", 15000],
        "sushi":["🍣", 10000, "food", 150000],
        "ramen":["🥘", 50000, "food", 250000],
        "maekju":["🍻", 100000, "food", 600000]}
    LEVELS = {}
    LEVELS[range(0, 500)] = 0
    for i in range(1,101):
        LEVELS[range(round(333 * (1.5 ** i)), round(333 * (1.5 ** (i + 1))))] = i
    
    RANK_ICON = {
        "Beginner":"🔰",
        "Swordsman":"🔱",
        "Knight":"🔆",
        "Master":"💠",
        "Legendary":"🎇",
        "Mythical Glory": "🎆"}
    RANK = {
        range(0,20): "Beginner",
        range(20,40): "Swordsman",
        range(40,60): "Knight",
        range(60,80): "Master",
        range(80,100): "Legendary",
        range(100, 9999): "Mythical Glory",}
    checkboxes = {"done":"☑","undone":"◻"}

    # ----------------------------------------------------- MAIN RUNNING PROGRAM --------------------------------------------------------

    while True:
        left = False
        with open(Accountsfilepath) as f:
            content = f.read().split("-----------------------------")
            content.remove("")
        active_user = content[0].splitlines()[1].split(": ")[1]
        active_account = ""
        if active_user == "none":
            print("\n⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜")
            print("1️⃣  Log In     🟦🟦⬜")
            print("2️⃣  Sign Up    🟦🟩🟦")
            print("3️⃣  Exit       🟩🟫🟩")
            print("⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜")
            print()
            option = Filter(input("⏩  "), "⏩  ", [1,2,3])

            if option == 1:
                active_account = Login()
            elif option == 2:
                active_account = Signup()
            elif option == 3:
                print("ok baboysh.") 
                left = True
        else:
            for i in USERSDATA:
                if i.username == active_user:
                    active_account = i
                    break
                    
            active_account.Welcome()
            
            while True:
                print("\n⬜🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦⬜")
                print("🟨✨🟨🟨🟨⬜              🏡 Main Hall              ⬜🟨🟨🟨✨🟨")
                print("⬜🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦⬜")
                print()
                print('⌨  Commands: ("/commands","/profile","/achievements","/shop","/quest","/update","/sign out","/exit")')
                command = Filter(input("\n⏩  /"), "\n⏩  /", ["commands","profile","achievements","shop","quest","exit","update","sign out"])
                if command.lower() == "exit":
                    left = True
                    break
                elif command.lower() == "sign out":
                    Signout()
                    break
                else:
                    output_function = getattr(Productivity, command)
                    output_function(active_account)
        if left is True:
            break

if __name__ == '__main__':
    main()