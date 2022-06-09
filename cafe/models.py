from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Reviewer(models.Model):
    account = models.ForeignKey(User, on_delete=models.CASCADE)
    bio = models.CharField("Bio", max_length=120, help_text="Ceritakan diri kamu dalam 120 character!")
    picture = models.CharField("Link Gambar", max_length=120, null=True)

    def __str__(self):
        return self.account.username

class Cafes(models.Model):
    name = models.CharField("Nama Cafe", max_length=100)
    address = models.CharField("Alamat", max_length=120, null=True)
    desc = models.TextField("Deskripsi", null=True)
    rating = models.FloatField("Rating", max_length=1, help_text="Rating 1-5")
    distance = models.CharField("Jarak", max_length=100, help_text="Isi dalam satuan kilometer (KM)")
    long = models.CharField("Longtitude", max_length=50)
    lat = models.CharField("Latitude", max_length=50)
    gmaps = models.CharField("Google Maps Link", max_length=120, help_text="Isi dengan link google maps cafe")
    is_open_24h = models.BooleanField("Buka 24 Jam", default=False)
    image = models.CharField("Link Gambar", max_length=120, null=True)

    created_at = models.DateField("Created At", auto_now_add=True)
    updated_at = models.DateField("Updated At", default=timezone.now)

    def __str__(self):
        return self.name

class CafeReview(models.Model):
    user = models.ForeignKey(Reviewer, on_delete=models.CASCADE)
    cafe = models.ForeignKey(Cafes, on_delete=models.CASCADE)
    review_text = models.TextField()
    
    def __str__(self):
        return f"Review {self.user.account.username}"

class CafePromo(models.Model):
    cafe = models.ForeignKey(Cafes, on_delete=models.CASCADE)
    image = models.CharField("Link Gambar", max_length=120, null=True)
    promo_title = models.CharField("Judul (Title) Promo", max_length=100)
    promo_text = models.TextField()

    def __str__(self):
        return self.promo_title
