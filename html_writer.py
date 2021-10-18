class html_writer:
	def __init__(self):
		self.result=''
		self.result+='<!DOCTYPE html>\n'
	
	def title(self, title):
		self.result+='<head>\n'
		self.result+=f'<meta name="viewport" content="width=device-width">\n'
		self.result+=f'<title>{title}</title>\n'
		self.result+='</head>\n'
	
	def body(self, content):
		self.result+='<body>\n'
		for j in content:
			self.result+=f'{j}'
		self.result+='</body>\n'
	
	def style(self, css):
		self.result+='<style>\n'
		css=css.strip('\n')
		self.result+=f'{css}\n'
		self.result+='</style>\n'
	
	def script(self, script):
		self.result+='<script>\n'
		self.result+=f'{script}\n'
		self.result+='</script>\n'
	
	def externscript(self, src):
		self.result+=f'<script src="{src}"></script>\n'
	
	def externstyle(self, link, rel='stylesheet'):
		self.result+=f'<link rel="{rel}" href="{link}">'
	
	def write_to_file(self, filename):
		with open(filename, 'w') as f:
			f.write(self.result)
	
	@property
	def html(self):
		return self.result

def label(text, id=None, class_=None):
	text=text.replace('\n', '<br>')
	result='<p'
	if id:
		result+=f' id="{id}"'
	if class_:
		result+=f' class="{class_}"'
	result+=f'>{text}</p>\n'
	return result

def header(text, level=1, id=None, class_=None):
	text=text.replace('\n','<br>')
	type=f'h{level}' if level<=6 else 'h6'
	result=f'<{type}'
	if id:
		result+=f' id="{id}"'
	if class_:
		result+=f' class="{class_}"'
	result+=f'>{text}</{type}>\n'
	return result

def link(text, link, id=None, class_=None):
	text=text.replace('\n','<br>')
	result=f'<a href="{link}"'
	if id:
		result+=f' id="{id}"'
	if class_:
		result+=f' class="{class_}"'
	result+=f'>{text}</a>\n'
	return result

def button(text, type='button', onclick=None, id=None, class_=None):
		text=text.replace('\n','<br>')
		result=f'<button type="{type}"'
		if id:
			result+=f' id="{id}"'
		if onclick:
			result+=f' onclick="{onclick}"'
		if class_:
			result+=f' class="{class_}"'
		result+=f'>{text}</button>\n'
		return result

def comment(text):
	text=f'<!--{text}-->\n'
	return text

def image(source, alt, class_=None, id=None):
	result=f'<img src="{source} alt="{alt}'
	if id:
		result+=f'id="{id}"'
	if class_:
		result+=f' class="{class_}"'
	result+='>'
	return result

def div(layout, id=None, class_=None):
	result='<div'
	if id:
		result+=f' id="{id}"'
	if class_:
		result+=f' class="{class_}"'
	result+='>\n'
	for element in layout:
		element=element.strip('\n')
		result+=f'{element}\n'
	result+='</div>\n'
	return result

def Input(value='', type='text', id=None, class_=None, name=None):
	result=f'<input type="{type}"'
	if id:
		result+=f' id="{id}"'
	if class_:
		result+=f' class="{class_}"'
	if name:
		result+=f' name="{name}"'
	result+=f' value="{value}">\n'
	return result

def bold(text):
	return f'<b>{text}</b>'

def italic(text):
	return f'<i>{text}</i>'

def strong(text):
	return f'<strong>{text}</strong>'

def emphasize(text):
	return f'<em>{text}</em>'

def list_item(text, id=None, class_=None):
	result='<li'
	if id:
		result+=f' id="{id}"'
	if class_:
		result+=f' class="{class_}"'
	result+=f'>{text}</li>\n'
	return result

def horizontal_separator(newline=True):
	return '<hr>\n' if newline else '<hr>'

def bullet_list(items):
	text='<ul>\n'
	for item in items:
		item=item.strip('\n')
		text+=f'{item}\n'
	text+='</ul>\n'
	return text

def iframe(source, title, id=None, height=None, width=None, class_=None):
	result=f'<iframe src="{source}" title="{title}"'
	if id:
		result+=f' id="{id}"'
	if width:
		result+=f' width="{width}"'
	if height:
		result+=f' height="{height}"'
	if class_:
		result+=f' class="{class_}"'
	result+='></iframe>\n'
	return result

def form(layout, action='', method='get', id=None, class_=None):
	result=f'<form action="{action}" method="{method}"'
	if id:
		result+=f' id="{id}"'
	if class_:
		result+=f' class="{class_}"'
	result+='>\n'
	for item in layout:
		item=item.strip('\n')
		result+=f'{item}\n'
	result+='</form>\n'
	return result

# ===============
# javascript popups
# ===============

def popup_alert(text):
	return 'alert("%s")' % str(text)

def popup_confirm(text):
	return 'confirm("%s")' % str(text)

def popup_get_text(text, default=''):
	return 'prompt("%s", "%s")' % (str(text), str(default))