import os
import sys
import json
import codecs
from chardet.universaldetector import UniversalDetector
from shutil import copyfile, rmtree

detector = UniversalDetector()

translations_root = os.getcwd()
# locales_root = '/Users/denissamohvalov/Documents/scopic-development/omnibazaar-ui/app/dist/i18n/app'
# app_root = '/Users/denissamohvalov/Documents/scopic-development/omnibazaar-ui/app'
locales_root = '/Users/ptu/develop/scopic/oc2/omnibazaar-ui/app/dist/i18n/app'
app_root = '/Users/ptu/develop/scopic/oc2/omnibazaar-ui/app'
locales = ['en', 'cn', 'hi', 'es', 'fr', 'ar', 'ru', 'pt', 'id', 'tr', 'kr', 'vi', 'it', 'gu', 'tl', 'ms', 'ro', 'uk']
encoding_converted_dir = os.path.join(translations_root, 'encoding_converted')

def save(obj, path):
    with open(path, 'w') as out:
        out.write(json.dumps(obj, indent=4, ensure_ascii=False))


def read_obj(path):
    with open(path, 'r') as stream:
        return json.loads(stream.read())


def get_translations(locales):
    translations = {}
    for locale in locales:
        print(locale)
        file_path = os.path.join(translations_root, '%s.json' % locale)
        exists = os.path.isfile(file_path)
        if exists:
            with open(file_path) as json_data:
                translations[locale] = json.loads(json_data.read())
    return translations

def add_new_langs():
    for locale in locales:
        path = os.path.join(translations_root, '%s.json' % locale)
        exists = os.path.isfile(path)
        if not exists:
            copyfile(os.path.join(translations_root, 'en.json'), path)
            
def convert_locales_encoding():
    if os.path.exists(encoding_converted_dir):
        rmtree(encoding_converted_dir)
    os.makedirs(encoding_converted_dir)

    for locale in locales:
        file_path = os.path.join(translations_root, '%s.json' % locale)
        to_path = os.path.join(encoding_converted_dir, '%s.json' % locale)
        exists = os.path.isfile(file_path)
        if exists:
            encoding = get_encoding(file_path)
            if encoding == 'utf-8':
                copyfile(file_path, to_path)
            else:
                convert_encoding(file_path, encoding, to_path)

def get_encoding(current_file):
    detector.reset()
    for line in open(current_file, 'rb'):
        detector.feed(line)
        if detector.done: break
    detector.close()
    return detector.result['encoding']

def convert_encoding(file_path, from_encoding, to_file):
    with codecs.open(file_path, 'rU', from_encoding) as sourceFile:
        write_conversion(to_file, sourceFile)

def write_conversion(file_path, file):
    with codecs.open(file_path, 'w', 'utf-8') as targetFile:
        for line in file:
            targetFile.write(line)


if __name__ == '__main__':
    encoding = get_encoding(os.path.join(translations_root, 'es.json'))
    convert_encoding(os.path.join(translations_root, 'es.json'), encoding, os.path.join(translations_root, 'es_utf8.json'))
