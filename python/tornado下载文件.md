# tornado下载文件

	def get(handler):
        handler.set_header('Content-Type', 'application/octet-stream')
        handler.set_header('Content-Disposition', 'attachment; filename=%s' % file_name)
        buf_size = 4096
        with open(file_name, 'rb') as f:
            while True:
                data = f.read(buf_size)
                if not data:
                    break
                handler.write(data)
        handler.finish()

	#如果file_nam有中文
	handler.set_header('Content-Disposition', 'attachment; filename=%s' % urllib.parse.quote(file_name))