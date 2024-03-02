import os
from zipfile import ZipFile
from flask import send_file


def create_zip(images):
    """
    Create a ZIP file containing the given images.

    Args:
        images (list): A list of paths to image files.

    Returns:
        str or None: The name of the created ZIP file if successful, None otherwise.
    """
    if all(os.path.exists(image_path) for image_path in images):
        with ZipFile('images.zip', 'w') as zip_file:
            for image_path in images:
                zip_file.write(image_path, os.path.basename(image_path))
        return 'images.zip'
    else:
        return None



# def your_route_function():
#     """
#     Your Flask route function to handle the request.
#
#     Returns:
#         str or Response: A response indicating success or failure.
#     """
#     zip_file = create_zip(image_paths)
#     if zip_file:
#         return send_file(zip_file, mimetype='application/zip', as_attachment=True)
#     else:
#         return 'One or more images not found', 404
