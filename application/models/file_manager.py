from google.appengine.api import files

def save_profile_image(image, image_path):
	writable_file_name = files.gs.create(image_path, mime_type = image.content_type, acl='public-read')

	with files.open(writable_file_name, 'ab') as f:
		f.write(image.read())
	files.finalize(writable_file_name)

def read_profile_image(image_path):
	with files.open(image_path, 'r') as f:
		data = f.read()
	return data