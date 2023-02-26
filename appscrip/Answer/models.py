from django.db import models
from multiselectfield import MultiSelectField


# Create your models here.
class Name(models.Model):
	name = models.CharField(max_length=200)

	def __str__(self):
		return self.name


class Cricketer(models.Model):
	player_name = (
		('sachin tendulkar', 'sachin tendulkar'),
		('Virat kohli', 'virat Kohli'),
		('Adam Gilchirst', 'Adam Gilchirst'),
		('Jacques Kallis', 'Jacques Kallis'),
	)
	name = models.ForeignKey(Name, on_delete=models.CASCADE)
	cricketer = models.CharField(max_length=100, null=True, choices=player_name)

	def __str__(self):
		return self.cricketer


class Color(models.Model):
	color_name = (
		('White', 'White'),
		('Yellow', 'Yellow'),
		('Orange', 'Orange'),
		('Green', 'Green'),
	)

	name = models.ForeignKey(Name, on_delete=models.CASCADE)
	cricketer = models.ForeignKey(Cricketer, on_delete=models.CASCADE)
	color = MultiSelectField(max_length=100, choices=color_name)

	def __str__(self):
		return str(self.color)
