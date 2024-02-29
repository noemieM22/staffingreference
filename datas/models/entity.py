from django.db import models


# Type : entité, fonction, mission, Catégorie
class Entity_type(models.Model):

    entity_type_FR = models.CharField("Type d'entité",max_length=50)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['entity_type_FR'], name='unique entity_type_FR')
        ]

class Entity(models.Model):
    entity_FR = models.CharField("Entité",max_length=50)
    entity_type = models.ForeignKey(Entity_type, on_delete = models.CASCADE,related_name='Entity_type')

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['entity_FR'], name='unique Entity_type')
        ]
