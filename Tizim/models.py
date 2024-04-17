from django.db import models

class Xona(models.Model):
    nom = models.CharField(max_length=39)
    raqam = models.IntegerField()


    def __str__(self):
        return f"{self.nom}"



class Yonalish(models.Model):
    nom = models.CharField(max_length=40)
    narx = models.CharField(max_length=30)


    def __str__(self):
        return f"{self.nom}"



class Ustoz(models.Model):
    ism = models.CharField(max_length=40)
    tel_raqam = models.CharField(max_length=40)
    manzil = models.CharField(max_length=40)
    yonalish = models.ForeignKey(Yonalish, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.ism}"



class Guruh(models.Model):
    nom = models.CharField(max_length=30)
    vaqt = models.CharField(max_length=40)
    xona = models.ForeignKey(Xona, on_delete=models.CASCADE)
    yonalish = models.ForeignKey(Yonalish, on_delete=models.CASCADE)
    ustoz = models.ForeignKey(Ustoz, on_delete=models.CASCADE)


    def __str__(self):
        return f"{self.nom}"



class Talaba(models.Model):
    ism = models.CharField(max_length=30)
    tel_raqam = models.CharField(max_length=30)
    manzil = models.CharField(max_length=40)
    guruh = models.ForeignKey(Guruh, on_delete=models.CASCADE)
    yonalish = models.ForeignKey(Yonalish, on_delete=models.CASCADE,null=True)


    def __str__(self):
        return f"{self.ism}"


class Tolov(models.Model):
    talaba = models.ForeignKey(Talaba, on_delete=models.CASCADE)
    guruh = models.ForeignKey(Guruh,on_delete=models.CASCADE)
    summa = models.FloatField()
    chegirma = models.PositiveIntegerField()
    qarz = models.FloatField()


    def __str__(self):
        return f"{self.talaba}-{self.guruh}"
