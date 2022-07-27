
from django.db import models

category_choice = (
        ('Parents','Parents'),
        ('Family', 'Family'),
        ('Siblings','Siblings'),
        ('Friends','Friends'),
        ('Special', 'Special'),
        ('Colleagues','Colleagues'),
    )
class People(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    dob=models.DateField()
    category=models.CharField(choices=category_choice, max_length=15)

    def __str__(self) -> str:
        return "{} - {} : {}".format(self.name, self.email, self.category)


class WishesText(models.Model):
    text= models.TextField()
    category=models.CharField(choices=category_choice,max_length=15)
    time_sent=models.IntegerField(default=0)

    def __str__(self) -> str:
        return "{} - {} : {}".format(self.category, self.text, self.time_sent)