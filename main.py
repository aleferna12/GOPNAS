#! "D:\alefe\Python Venvs\Python37\GOPNAS\Scripts\python.exe"
from kivy.config import Config

Config.set('graphics', 'width', 405)
Config.set('graphics', 'height', 720)
Config.set('graphics', 'window_state', 'maximized')
Config.set('graphics', 'resizable', True)

import os
import json
import PIL.Image
import colordict as cd

from kivy.app import App
from kivy.properties import *
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.image import AsyncImage
from kivy.uix.dropdown import DropDown
from kivy.uix.scrollview import ScrollView
from kivy.uix.label import Label
from kivy.clock import Clock


class Root(FloatLayout):
	info_layout = ObjectProperty(None)
	dropdown = ObjectProperty(None)
	dropdown_button = ObjectProperty(None)
	scrollview = ObjectProperty(None)
	bg_image = ObjectProperty(None)
	credits_button = ObjectProperty(None)

	def __init__(self, **kwargs):
		super(Root, self).__init__(**kwargs)

		self.info_layout = InfoLayout()
		self.dropdown = DropDown()
		self.dropdown.auto_dismiss = False
		self.dropdown.effect_cls = 'ScrollEffect'
		self.dropdown_button.bind(on_release=self.dropdown.open)
		groups = sorted(next(os.walk(app.cladi_directory))[1])
		for group in groups:
			self.dropdown.add_widget(GroupButton(group))

		# Esse widget é adicionado e removido respectivamente por GroupButton e SpeciesButton
		self.scrollview = ButtonScrollView()

	# Não pode ser on_touch_up porque senão ele fecha abre e fecha o dropdown imediatamente
	def on_touch_down(self, touch):
		# Lógica para contornar o fato de que mesmo com o scrollview não adicionado ele retorna True para collide_point()
		if not (self.scrollview.parent and self.scrollview.collide_point(*touch.pos)) \
				and not self.dropdown.collide_point(*touch.pos):
			self.remove_widget(self.scrollview)
			self.dropdown.dismiss()
		return super().on_touch_down(touch)


class InfoLayout(FloatLayout):
	group = StringProperty('')
	species = StringProperty('')
	cladus_directory = StringProperty('')
	carousel = ObjectProperty(None)
	tabs = ObjectProperty(None)
	current_tab = ObjectProperty(None)
	btn_line = ObjectProperty(None)
	info_label = ObjectProperty(None)

	def display_cladi(self, group, species):
		self.group = group
		self.species = species
		self.cladus_directory = os.path.join(app.cladi_directory, self.group, self.species)

		self.carousel.clear_widgets()
		path, _, im_iter = next(os.walk(os.path.join(self.cladus_directory, 'images')))
		im_iter.sort()
		for i, image in enumerate(im_iter):
			im_path = os.path.join(path, image)
			valid_jpeg = [".jpg", ".JPG", ".jpeg", ".JPEG"]
			if image[-4:] not in valid_jpeg:
				raise Exception(f"File parsed from \"{im_path}\" is not a valid JPEG extension {tuple(valid_jpeg)}")
			# Decodifica o metadata do JPEG em busca de comentários (marcados pela tag 40092)
			image_exif = PIL.Image.open(im_path).getexif()
			comment_binary = image_exif.get(40092)
			author = image_exif.get(315)
			# Carrega a primeira imagem imediatamente enquanto as demais carregam asincronizadamente
			if i == 0:
				self.carousel.add_widget(CommentedImage(comment_binary, author, source=im_path, allow_stretch=True))
			else:
				self.carousel.add_widget(AsyncCommented(comment_binary, author, source=im_path, allow_stretch=True))

		default_tab = self.tabs.children[-1]
		if not self.current_tab:
			self.current_tab = default_tab
		self.set_info_label(default_tab)

	def set_info_label(self, btn):
		self.info_label.parent.scroll_y = 1
		with open(os.path.join(self.cladus_directory, btn.file), 'r', encoding='utf-8') as file:
			self.info_label.text = file.read()
		self.current_tab.color = app.colors['black']
		btn.color = app.colors['current_tab']
		self.current_tab.disabled = False
		btn.disabled = True
		self.current_tab = btn


class ButtonScrollView(ScrollView):
	pass


class GroupButton(Button):
	group = StringProperty('')
	cladus_directory = StringProperty('')

	def __init__(self, group, **kwargs):
		super().__init__(**kwargs)

		self.group = group
		self.cladus_directory = os.path.join(app.cladi_directory, self.group)

	def on_release(self):
		if not app.root.scrollview.parent:
			app.root.add_widget(app.root.scrollview)
		app.root.scrollview.scroll_y = 1

		app.root.scrollview.container.clear_widgets()
		dir_iter = sorted(next(os.walk(self.cladus_directory))[1])
		grad_list = cd.LinearGrad([app.colors[name] for name in app.colors.palettes['icons']]).n_colors(len(dir_iter))
		for i, species in enumerate(dir_iter):
			btn = SpeciesButton(
				self.group,
				species,
				background_color=grad_list[i]
			)
			app.root.scrollview.container.add_widget(btn)


class SpeciesButton(GroupButton):
	species = StringProperty('')

	def __init__(self, group, species, **kwargs):
		super().__init__(group, **kwargs)

		self.species = species
		self.cladus_directory = os.path.join(self.cladus_directory, self.species)

	def on_release(self):
		app.root.clear_widgets(children=[app.root.info_layout, app.root.scrollview, app.root.bg_image, app.root.credits_button])
		app.root.dropdown.dismiss()

		if not app.root.info_layout.parent:
			app.root.add_widget(app.root.info_layout)
		app.root.info_layout.display_cladi(self.group, self.species)


class CommentedImage(Image):
	comment = StringProperty('')
	comment_label = ObjectProperty(None)
	author = StringProperty('')
	author_label = ObjectProperty(None)

	def __init__(self, comment_bin, author, **kwargs):
		super().__init__(**kwargs)

		self.comment = ''
		# Cortar o último byte que vem bugado
		if comment_bin is not None:
			self.comment += comment_bin.decode('utf-16')[:-1]
		if author is not None:
			self.comment += ('; ' if self.comment else '') + 'Foto de ' + author
		if self.comment:
			self.comment_label = CommentLabel(text=self.comment)
			self.bind(pos=self.comment_label.setter('pos'))
			self.add_widget(self.comment_label)

			self.remove_comment = Clock.create_trigger(lambda *args: setattr(self.comment_label, 'disabled', True), 4)

	def on_touch_down(self, touch):
		if self.comment:
			self.comment_label.disabled = False
			self.remove_comment.cancel()
			self.remove_comment()
			return True
		else: return super().on_touch_down(touch)


class AsyncCommented(AsyncImage, CommentedImage):
	def __init__(self, comment_bin, author, **kwargs):
		# Descobri que sempre se passa kwargs e nunca args para multipla inheritance
		super().__init__(comment_bin=comment_bin, author=author, **kwargs)


class CommentLabel(Label):
	background_color = ListProperty([])

	def on_disabled(self, _, val):
		if val:
			self.color = app.colors['white', 'rgb'] + (.2,)
			self.background_color = app.colors['dimgray', 'rgb'] + (0,)
		else:
			self.color = app.colors['white']
			self.background_color = app.colors['dimgray']


class CreditsLabel(Label):
	@staticmethod
	def get_credits_text():
		with open(os.path.join(app.resources_directory, "credits.txt"), encoding="UTF-8") as file:
			return file.read()


class MainApp(App):
	btns_h = NumericProperty(1/8)
	infos_width_hint = NumericProperty(5/6)
	resources_directory = StringProperty('')
	cladi_directory = StringProperty('')
	species_aliases = DictProperty()
	colors = ObjectProperty(cd.ColorDict(norm=1, mode='rgba', palettes_path='Resources/Palettes'))

	def build(self):
		self.title = 'GOPNAS'
		self.resources_directory = os.path.join(self.directory, 'Resources')
		self.cladi_directory = os.path.join(self.directory, 'Cladi')
		with open(os.path.join(self.cladi_directory, 'species_aliases.json'), 'r') as file:
			self.species_aliases = json.load(file)
		return Root()


if __name__ == '__main__':
	app = MainApp()
	app.run()
