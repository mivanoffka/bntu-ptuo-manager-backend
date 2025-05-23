from django.db import migrations


def create_superuser(apps, schema_editor):
    User = apps.get_model("users", "UserModel")
    if not User.objects.filter(username="admin").exists():
        User.objects.create_superuser(
            username="admin",
            email="admin@example.com",
            password="admin",
            role="admin",
            is_verified=True,
        )


class Migration(migrations.Migration):

    dependencies = [
        (
            "users",
            "0001_initial",
        ),
    ]

    operations = [
        migrations.RunPython(create_superuser),
    ]
