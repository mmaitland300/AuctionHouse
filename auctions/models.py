from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone



class User(AbstractUser):
    pass



class AuctionListing(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE, related_name = "seller")
    title = models.CharField(max_length = 64)
    description = models.TextField()
    start_bid = models.IntegerField()
    image = models.URLField(blank = True)
    category = models.CharField(blank = True, max_length = 64)
    active = models.BooleanField(blank = False, default = True)
    winner = models.ForeignKey(User, blank = True, on_delete = models.CASCADE, related_name = "buyer", null = True)

    
    def __str__(self):
        return f"{self.title} sold by {self.user}"
    
class Bid(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    value = models.IntegerField()
    listing = models.ForeignKey(AuctionListing, on_delete=models.CASCADE)
    winner = models.BooleanField(default = False)
    
    def __str__(self):
        return f"A bid of {self.value} made for the item {self.listing} by {self.user}"
    
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    listing = models.ForeignKey(AuctionListing, on_delete = models.CASCADE)
    content = models.TextField()
    post_time = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.user} posted to {self.listing} at {self.post_time}"

class Watchlist(models.Model):
    user = models.ForeignKey(User, blank=True, on_delete=models.CASCADE)
    listing = models.ForeignKey(AuctionListing, blank=True, on_delete=models.CASCADE)