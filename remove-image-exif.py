#!/usr/bin/env python
import argparse
import os
import sys
import piexif
from PIL import Image


def create_parser():
    # parse command line arguments
    parser = argparse.ArgumentParser(description='Remove exif information from jpg-files')
    parser.add_argument("--folder", help='Specify folder with image files', required=True, type=str)
    parser.add_argument("--silent", action="store_true", required=False, help='Silent mode without user interaction')
    return parser


def get_fill_path(self, path):
    if os.path.isabs(path):
        return path
    script_path = os.path.realpath(__file__)
    file_path = os.path.join(os.path.dirname(script_path), path)
    return file_path


def is_jpeg_ext(path):
    filename, file_ext = os.path.splitext(path)
    if not file_ext:
        return False
    ext = str(file_ext).lower()
    return ext == '.jpg' or ext == '.jpeg'


def is_jpeg_content(filename):
    try:
        img = Image.open(filename)
        return img.format == 'JPEG'
    except IOError:
        return False


def main():
    silent_mode = False
    try:
        # parse command line arguments
        parser = create_parser()
        args = parser.parse_args()
        silent_mode = args.silent

        folder = args.folder
        print('Search jpg files in folder: {}'.format(folder))

        processed = 0
        completed = 0
        for file in os.listdir(folder):
            processed = processed + 1
            file_path = os.path.join(folder, file)
            file_name = os.path.basename(file_path)
            if os.path.isfile(file_path):
                if not is_jpeg_ext(file_path):
                    continue
                if not is_jpeg_content(file_path):
                    continue
                piexif.remove(file_path)
                print('Updated: {}'.format(file_name))
                completed = completed + 1

        print('Removed Exif information from {} of {} files'.format(completed, processed))

        sys.exit(0)

    except Exception as e:
        print(e)
        if not silent_mode:
            print('Press any key to exit...')
            os.system("pause")
        sys.exit(e)


if __name__ == '__main__':
    main()
