import os
from django.db import migrations
from django.contrib.auth.models import User

def create_admin(apps, schema_editor):
    # Grabs username and password from Render settings, or defaults locally
    admin_username = os.environ.get('ADMIN_USERNAME', 'Admin')
    admin_password = os.environ.get('ADMIN_PASSWORD', '1234')
    
    try:
        # Look for the user matching the environment username
        u = User.objects.get(username=admin_username)
        u.set_password(admin_password)
        u.save()
        print(f"--- Admin account '{admin_username}' updated successfully! ---")
    except User.DoesNotExist:
        # Create a fresh superuser if it doesn't exist yet
        User.objects.create_superuser(admin_username, 'faithfred721@gmail.com', admin_password)
        print(f"--- Fresh Admin superuser '{admin_username}' created successfully! ---")

class Migration(migrations.Migration):

    dependencies = [
        ('withdraw', '0002_rename_link_count_starlinkorder_otp_count_and_more'), 
    ]

    operations = [
        migrations.RunPython(create_admin),
    ]