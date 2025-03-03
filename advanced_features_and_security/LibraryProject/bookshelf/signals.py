from django.db.models.signals import post_migrate
from django.contrib.auth.models import Group, Permission
from django.apps import apps
from django.dispatch import receiver

@receiver(post_migrate)
def create_groups_and_permissions(sender, **kwargs):
    if sender.name == "bookshelf":  # Change to your app name
        # Define groups
        groups_permissions = {
            "Viewers": ["can_view"],
            "Editors": ["can_view", "can_create", "can_edit"],
            "Admins": ["can_view", "can_create", "can_edit", "can_delete"],
        }

        # Get model permissions
        book_permissions = Permission.objects.filter(content_type__app_label="bookshelf")

        for group_name, perm_codes in groups_permissions.items():
            group, created = Group.objects.get_or_create(name=group_name)

            for perm_code in perm_codes:
                permission = book_permissions.filter(codename=perm_code).first()
                if permission:
                    group.permissions.add(permission)

            print(f"Group '{group_name}' updated with permissions: {perm_codes}")