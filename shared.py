import os
import json
from shutil import copyfile

translations_root = os.getcwd()
#locales_root = '/Users/denissamohvalov/Documents/scopic-development/omnibazaar-ui/app/dist/i18n/app'
#app_root = '/Users/denissamohvalov/Documents/scopic-development/omnibazaar-ui/app'
locales_root = '/Users/ptu/develop/scopic/oc2/omnibazaar-ui/app/dist/i18n/app'
app_root = '/Users/ptu/develop/scopic/oc2/omnibazaar-ui/app'
locales = ['en', 'zh', 'hi', 'es', 'fr', 'ar', 'ru', 'pt', 'id', 'tr', 'ko', 'vi', 'it', 'gu', 'tl', 'ms', 'ro', 'uk']

def save(obj, path):
    with open(path, 'w') as out:
        out.write(json.dumps(obj, indent=4, ensure_ascii=False))


def read_obj(path):
    with open(path, 'r') as stream:
        return json.loads(stream.read())


def get_translations(locales):
    translations = {}
    for locale in locales:
        with open(os.path.join(translations_root, '%s.json' % locale)) as json_data:
            translations[locale] = json.loads(json_data.read())
    return translations

def add_new_langs():
    for locale in locales:
        path = os.path.join(translations_root, '%s.json' % locale)
        exists = os.path.isfile(path)
        if not exists:
            copyfile(os.path.join(translations_root, 'en.json'), path)