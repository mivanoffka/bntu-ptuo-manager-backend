from django.db.models import Model
from django.db.models.signals import pre_save, post_save, pre_delete
from abc import ABC

from .models.employee_version_model import EmployeeVersionModel

from .models import BntuPositionModel
from trees.models import TreeNodeModel, BntuDepartmentModel, TradeUnionDepartmentModel


class TreeSignals(ABC):
    tree_model_class: type[TreeNodeModel]
    related_model_class: type[Model]
    related_model_path_field: str

    @classmethod
    def connect_signals(cls):
        if (
            not cls.tree_model_class
            or not cls.related_model_class
            or not cls.related_model_path_field
        ):
            raise NotImplementedError(
                "Must define 'tree_model_class', 'related_model_class', and 'related_model_path_field'."
            )

        pre_save.connect(cls.capture_old_path, sender=cls.tree_model_class)
        post_save.connect(
            cls.update_related_on_path_change, sender=cls.tree_model_class
        )
        pre_delete.connect(
            cls.update_related_on_node_delete, sender=cls.tree_model_class
        )

    @staticmethod
    def capture_old_path(sender, instance, **kwargs):
        if instance.pk:
            try:
                old_instance = sender.objects.get(pk=instance.pk)
                instance._old_path = old_instance.path
            except sender.DoesNotExist:
                instance._old_path = None

    @classmethod
    def update_related_on_path_change(cls, sender, instance, created, **kwargs):
        if not created and hasattr(instance, "_old_path"):
            old_path = instance._old_path
            new_path = instance.path

            if old_path != new_path:
                # Update direct references
                cls.related_model_class.objects.filter(
                    **{cls.related_model_path_field: old_path}
                ).update(**{cls.related_model_path_field: new_path})

                # Update descendant paths
                for descendant in instance.get_descendants():
                    old_child_path = descendant.path
                    new_child_path = new_path + old_child_path[len(old_path) :]

                    cls.related_model_class.objects.filter(
                        **{cls.related_model_path_field: old_child_path}
                    ).update(**{cls.related_model_path_field: new_child_path})

    @classmethod
    def update_related_on_node_delete(cls, sender, instance, **kwargs):
        parent = instance.get_parent()
        parent_path = parent.path if parent else None

        # Update references to the deleted node
        cls.related_model_class.objects.filter(
            **{cls.related_model_path_field: instance.path}
        ).update(**{cls.related_model_path_field: parent_path})

        # Update all descendant references
        for descendant in instance.get_descendants():
            old_child_path = descendant.path
            if parent_path:
                new_child_path = parent_path + old_child_path[len(instance.path) :]
            else:
                new_child_path = None

            cls.related_model_class.objects.filter(
                **{cls.related_model_path_field: old_child_path}
            ).update(**{cls.related_model_path_field: new_child_path})


# Concrete implementations


class BntuDepartmentSignals(TreeSignals):
    tree_model_class = BntuDepartmentModel
    related_model_class = BntuPositionModel
    related_model_path_field = "bntu_department_path"


class TradeUnionDepartmentSignals(TreeSignals):
    tree_model_class = TradeUnionDepartmentModel
    related_model_class = EmployeeVersionModel
    related_model_path_field = "trade_union_department_path"
