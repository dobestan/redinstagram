def post_image_upload_to(instance, filename):
    return "instagram/posts/{filename}.{extension}".format(
        filename=instance.hash_id,
        extension=filename.split('.')[-1],
    )
