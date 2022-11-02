from django.db import models


class Restaurant(models.Model):
    id = models.AutoField(primary_key=True)
    Res_name = models.CharField(max_length=15, default=' ')
    category = models.CharField(max_length=10, default=' ')
    distance = models.IntegerField()

    def __str__(self):
        return self.Res_name


class Menu(models.Model):
    Res_id = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    id = models.AutoField(primary_key=True)
    Menu_name = models.CharField(max_length=20, default=' ')
    price = models.IntegerField()

    def __str__(self):
        return self.id

# class Restaurant(models.Model):
#     id = models.CharField(max_length=200, default=' ')
#     name = models.TextField()
#     create_date = models.DateTimeField()
#     def __str__(self):
#         return self.subject
#
#
#
# class Menu(models.Model):
#     subject = models.ForeignKey(Question, on_delete=models.CASCADE)
#     content = models.TextField()
#     create_date = models.DateTimeField()
