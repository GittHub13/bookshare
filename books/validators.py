from django.core.exceptions import ValidationError

def validate_image_size(image):
    max_size_kb = 500  # თუ გინდა სხვა ზომა, შეცვალე აქ
    if image.size > max_size_kb * 1024:
        raise ValidationError(f"Image file size should not exceed {max_size_kb}KB.")