#!/usr/bin/env python
import os, sys

# autodetect root folder
ignores=['env', 'build', '.git']

static_root = '/usr/share/nginx/html/'
for root, dirs, files in os.walk(static_root):
	for ignore in ignores:
		if (ignore in dirs):
			dirs.remove(ignore)

	if 'static' ==  os.path.basename(root):
		static_root = root
		break

	if 'public_html' ==  os.path.basename(root):
		static_root = root
		break

	if 'production.ini' in files:
		pass

print 'export UPSCALE_STATIC_ROOT={0}'.format(static_root)

