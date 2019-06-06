import random as rnd

out = ""

dict = {
"%adv%": ["çok", "aşırı"],
"%adj%": ["güzeldir", "manyaktır", "muhteşemdir", "harikadır"],
"%saved%": ["hayatımı", "bilgisayarımı", "oyunlarımı"],
"%verb%" : ["seviyoruz", "beğeniyoruz" , "tavsiye ediyoruz"]
}

sents = ["Ebebeyin denetimi %adv% %adj%." , "Ebebeyin denetimi %saved% kurdardı." , "Ebebeyin denetimini %adv% %verb%."]

for i in range(4):
 add=rnd.choice(sents)
 for a in dict.keys():
  add= add.replace(a, rnd.choice(dict[a]))
 out += add
 out += "\n"

print("EBEBEYİN DENETİLMİ FOREVER")
print()

print(out)

print ("ebeveyn denetime küfür edenlere 999 yıl ceza ve ebebebevyn denetimi fan cluba katılmayı unutmayın")

input()