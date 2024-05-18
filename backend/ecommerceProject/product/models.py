from django.db import models
from django.contrib.auth.models import User


class Category(models.TextChoices):
    BIDON = "Bidon",
    BALAI = "Balai",
    RACLETTE = "Raclette",
    CHIFFON = "Chiffon",
    TEXTILE = 'textile',
    LIQUIDE = 'liquide',
    BROSSE = 'brosse',
    MANCHE = 'manche',
    PELLE = 'pelle',
    MOP = 'mop',
    FROTOIRE = 'frotoire'


class brandName(models.TextChoices):
    PRIMA = "Prima", "prima"
    CLEANTEX = "Cleantex", "cleantex"
    PAREX = "Parex", "parex"
    ARIANE = "Ariane", "ariane"
    BRILEX = "Brilex", "brilex"
    AIGLE = "Aigle", "aigle"
    BINGO = "Bingo", "bingo"
    ARIEL = "Ariel", "ariel"
    AMIR = "AMIR", "amir"
    LE_CHAT = "Le Chat", "le_chat"
    CIRTA = "CIRTA", "cirta"
    

class Product(models.Model):
    id = models.CharField(max_length=20, primary_key=True)
    name = models.CharField(max_length=200)
    price =  models.DecimalField(max_digits=7 , decimal_places=2 , default="00")
    description = models.TextField()
    isInStock = models.BooleanField(default=True)
    category = models.CharField(max_length=50, choices=Category.choices)
    image = models.ImageField(upload_to='product/products_images', blank=False , default="")
    rating = models.DecimalField(max_digits=3, decimal_places=2, default=0)
    totalReviewCount = models.IntegerField()
    brandName = models.CharField(max_length=100 , choices=brandName.choices)
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    stock = models.IntegerField(default=0)


    def __str__(self):
        return self.name
    
    
class Review(models.Model):
    product = models.ForeignKey(Product, null=True, on_delete=models.CASCADE,related_name='reviews')
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    rating = models.IntegerField(default=0)
    comment = models.TextField(max_length=1000,default="",blank=False) 
    createAt = models.DateTimeField(auto_now_add=True) 

    def __str__(self):
        return self.comment   