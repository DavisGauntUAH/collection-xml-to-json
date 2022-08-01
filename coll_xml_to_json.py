import argparse
import glob


def xml_2_json(path):
    path = path+'/*.json'
    files = glob.glob(path)
    for file in files:
        file_contents = ''
        with open (file, 'r', encoding='utf-8') as in_file:
            file_contents = in_file.read()
        file_contents = file_contents.replace('(xml|json)', 'json')
        file_contents = file_contents.replace('xml', 'json')
        with open(file, 'w') as out_file:
            out_file.write(file_contents)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('path', help='Provide a path to collections folder')
    args = parser.parse_args()
    
    if args.path:
        xml_2_json(args.path)
    else: print('Provide a path to collections folder')

if __name__ == '__main__':
    main()