import os
from django.db import migrations
from django.contrib.auth.models import User

def create_admin(apps, schema_editor):
    # This grabs the password from Render environment settings, or uses 1234 locally
    admin_password = os.environ.get('ADMIN_PASSWORD', '1234')
    
    try:
        u = User.objects.get(username='Admin')
        u.set_password(admin_password)
        u.save()
        print(f"--- Admin password updated successfully! ---")
    except User.DoesNotExist:
        User.objects.create_superuser('Admin', 'faithfred721@gmail.com', admin_password)
        print(f"--- Fresh Admin superuser created successfully! ---")

class Migration(migrations.Migration):

    dependencies = [
        ('withdraw', '0002_rename_link_count_starlinkorder_otp_count_and_more'), 
    ]

    operations = [
        migrations.RunPython(create_admin),
    ]