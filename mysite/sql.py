#将单词导入数据库中
#步骤：
#1.运行python manage.py shell
#2.分别运行以下三段代码导入Toefl, Cet-4, Cet-6数据
#
#
from blog.models import Toefl  

a = Toefl.objects.all()
b = a.delete()
count = 0

with open("toefl.txt",'r',encoding='utf-8') as f:  
    for line in f:  
        vocabulary, paraphrase = line.split('***')  
        Toefl.objects.create(vocabularys=vocabulary, paraphrases=paraphrase, id_num=count)
        count = count + 1 


from blog.models import Four  

a = Four.objects.all()
b = a.delete()
count = 0

with open("four.txt",'r',encoding='utf-8') as f:  
    for line in f:  
        vocabulary, paraphrase = line.split('***')  
        Four.objects.create(vocabularys=vocabulary, paraphrases=paraphrase, id_num=count)
        count = count + 1


from blog.models import Six  

a = Six.objects.all()
b = a.delete()
count = 0

with open("six.txt",'r',encoding='utf-8') as f:  
    for line in f:  
        vocabulary, paraphrase = line.split('***')  
        Six.objects.create(vocabularys=vocabulary, paraphrases=paraphrase, id_num=count)
