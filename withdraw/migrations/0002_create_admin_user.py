from django.db import migrations
from django.contrib.auth.models import User

def create_admin(apps, schema_editor):
    try:
        # Check if the Admin already exists
        u = User.objects.get(username='Admin')
        u.set_password('1234')
        u.save()
        print("--- Admin password updated successfully! ---")
    except User.DoesNotExist:
        # If the admin was deleted, recreate it safely
        User.objects.create_superuser('Admin', 'faithfred721@gmail.com', '1234')
        print("--- Fresh Admin superuser created successfully! ---")

class Migration(migrations.Migration):

    dependencies = [
        # Change this line to point to your existing tracking file
        ('withdraw', '0002_rename_link_count_starlinkorder_otp_count_and_more'), 
    ]

    operations = [
        migrations.RunPython(create_admin),
    ]