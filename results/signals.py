import pandas as pd
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import ResultFile, Result
from django.contrib.auth.models import User

@receiver(post_save, sender=ResultFile)
def process_uploaded_file(sender, instance, created, **kwargs):
    print("Signal for ResultFile reached.")  # Debug line
    if created:
        print(f"File uploaded: {instance.file.name}")
        
        # Read and process the uploaded file (Excel)
        file_path = instance.file.path
        df = pd.read_excel(file_path)
        
        # Store new results in the database
        for _, row in df.iterrows():
            Result.objects.create(
                roll_no=row['Roll No'],
                name=row['Name'],
                student_class=row['Class'],
                marks=row['Marks'],
                uploaded_file=instance  # Associate each result with the uploaded file
            )