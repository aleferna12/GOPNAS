import re
import os
import requests as rq
from bs4 import BeautifulSoup


def html_to_bbcode(string):
	def sub_fun(tag):
		allowed = {
			'i': 'i',
			'b': 'b',
			'em': 'i',
			'strong': 'b'
		}
		content = tag.group(1).split(' ')
		tag_name = content[0]
		attrs = {}
		if len(content) > 1:
			for pair in content[1:]:
				name, val = pair.split('=', 1)
				attrs[name] = val

		if tag_name in allowed:
			return "[%s]" % allowed[tag_name]
		if tag_name.strip('/') in allowed:
			return "[/%s]" % allowed[tag_name.strip('/')]
		return ""

	return re.sub(r"<(.*?)>", sub_fun, string)


def get_sci_name(species_soup):
	title = species_soup.title
	return re.search(r"\(([\w ]+)\)", str(title)).group(1)


def translate_latin_chars(species_name):
	species_name = species_name.lower()
	old = "áãâéêíóôõúç"
	new = "aaaeeiooouc"
	return species_name.translate(species_name.maketrans(old, new))


def remove_references(text):
	def subs_fun(match):
		if match.group(1) in ".,!?:;":
			return ''
		return ' '

	return re.sub(r" ?\(.*\d{4}\)(.?)", subs_fun, text)


def format_paragraphs(text):
	separator = "\n\n    "
	text = "    " + text.strip()
	return re.sub(r"\n+", separator, text)


def strip_tag(tag):
	return re.match(r"<.*?>((.|\n)*)</.*>$", str(tag)).group(1).strip()


def get_species_soup(species_name):
	url = "http://www.wikiaves.com.br/wiki/" + translate_latin_chars(species_name)
	page = rq.get(url)

	return BeautifulSoup(page.content, "html5lib")


def get_tag_by_id(species_soup, id_):
	id_tag = species_soup.find("h2", id=id_)
	if id_tag is None: return None
	return id_tag.next_sibling.next_sibling


def get_text_from_id(species_soup, id_):
	tag = get_tag_by_id(species_soup, id_)
	if tag is None: return None
	text = "".join([strip_tag(tag) for tag in tag.find_all('p', recursive=False)])
	text = format_paragraphs(text)
	return text


def get_subspecies_text(species_soup):
	tag = get_tag_by_id(species_soup, "subespecies")
	if tag is None: return None
	text = "\n".join(["- " + strip_tag(sub.div) for sub in tag.find_all("li")]).strip()
	if not text or re.search(r"[Nn]ão possui subespécies", text) is not None: return None

	return format_paragraphs(text)


def build_species_file(species_soup: BeautifulSoup):
	with open("./file_template.txt", encoding="utf8") as file:
		file_text = file.read()

	portlet = species_soup.find("div", class_="m-portlet__body")
	taxonomy = portlet.find(id="taxonomia")

	targets = ["Ordem:", "Subordem:", "Família:", "Espécie:"]
	for tr in taxonomy.find_all("tr"):
		cladus = list(tr.stripped_strings)
		if len(cladus) == 2:
			if cladus[0] in targets:
				if cladus[0] == "Espécie:":
					cladus[1] = f"[i]{cladus[1]}[/i]"
				file_text += f"\n\n{cladus[0]} {cladus[1]}"

	format_dict = {}
	title = species_soup.title
	format_dict["pop_names"] = re.search(r">([\w-]+) ", str(title)).group(1).capitalize()
	format_dict["sci_names"] = get_sci_name(species_soup)
	format_dict["en_name"] = portlet.find("h2", string="Nome em Inglês").next_sibling.string

	return file_text.format(**format_dict)


def build_species_info(species_soup):
	with open("./info_template.txt", encoding="utf8") as file:
		info_text = file.read()

	info_text = info_text.format(car_fis=get_text_from_id(species_soup, 'caracteristicas'))

	song = get_text_from_id(species_soup, "vocalizacao")
	if song is not None:
		info_text += "\n\n[b]Características do Canto[/b]\n\n" + song

	subspecies = get_subspecies_text(species_soup)
	if subspecies is not None:
		info_text += "\n\n[b]Subespécies[/b]\n\n" + subspecies

	return html_to_bbcode(remove_references(info_text))


def build_species_hab(species_soup):
	hab_text = ""
	targets = ["Alimentação", "Reprodução", "Hábitos", "Distribuição Geográfica"]
	for target in targets:
		text = get_text_from_id(species_soup, translate_latin_chars(target))
		if text is not None:
			if hab_text:
				hab_text += "\n\n"
			hab_text += f"[b]{target}[/b]\n\n" + text

	return html_to_bbcode(remove_references(hab_text))


def create_files(species_name, path, create_folder=False, warning=True):
	if warning and any([file in os.listdir(path) for file in ["file.txt", "info.txt", "hab.txt"]]):
		if input("This directory contains files that will be overriden, procced anyway? (Y/n)") not in 'Yy':
			print("Aborting")
			return None

	species_soup = get_species_soup(species_name)
	if create_folder:
		path = os.path.join(path, get_sci_name(species_soup))
		if not os.path.exists(path):
			os.mkdir(path)

	with open(os.path.join(path, "file.txt"), 'w', encoding="utf8") as file:
		file.write(build_species_file(species_soup))
	with open(os.path.join(path, "info.txt"), 'w', encoding="utf8") as file:
		file.write(build_species_info(species_soup))
	with open(os.path.join(path, "hab.txt"), 'w', encoding="utf8") as file:
		file.write(build_species_hab(species_soup))


def main():
	path = "C:/Users/alefe/Desktop/Python Projects/Projects/GOPNAS/New Species/Web Scrapped"
	print("Input species separated by \" \" or by \",\":")
	running = True
	while running:
		raw_input = input()
		if not raw_input or raw_input == ".":
			running = False
		species = raw_input.replace(" ,", ',').replace(' ', ',').split(',')

		for species_name in species:
			create_files(species_name, path, create_folder=True)


if __name__ == "__main__":
	main()