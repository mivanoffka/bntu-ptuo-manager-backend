from django.db import models

from treebeard.mp_tree import MP_Node


class TreeNodeModel(MP_Node):
    id = models.AutoField(primary_key=True)
    path = models.CharField(max_length=255, unique=True)
    label = models.CharField(max_length=255)
    node_order_by = ["label"]

    def __str__(self):
        return self.label

    class Meta(MP_Node.Meta):
        abstract = True
