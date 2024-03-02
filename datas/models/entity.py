from django.db import models


# Type : entité, fonction, mission, Catégorie
class Entity_type(models.Model):

    entity_type_FR = models.CharField("Type d'affectation",max_length=50)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['entity_type_FR'], name='unique entity_type_FR')
        ]
    def __str__(self):
        return self.entity_type_FR

class Entity(models.Model):
    entity_FR = models.CharField("Affectation",max_length=50)
    entity_type = models.ForeignKey(Entity_type, on_delete = models.CASCADE,related_name='Entity_type',verbose_name="Type d'affectation")

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['entity_FR'], name='unique Entity_type')
        ]
    def __str__(self):
        toReturn = self.entity_type.entity_type_FR + ' - ' + self.entity_FR
        return toReturn
