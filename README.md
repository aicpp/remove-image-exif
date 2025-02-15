Remove image Exif.

Original: [lifenod/remove-image-exif](https://github.com/lifenod/remove-image-exif) 

The script removes Exif data from all *.jpg/*.jpeg files in specified folder. 

[Why Remove EXIF Data?](https://photographylife.com/what-is-exif-data#why-remove-exif-data) 

## How to use

1.  Installation dependent package
```
        pip install piexif
        pip install Pillow
```
2.  Add executable permissions
```
        chmod +x ./remove-image-exif.py
```
3.  Run
```
        ./remove-image-exif.py --folder=/path/where/jpg/files
```

## Automatization

At first, you should install python package: `pyinstaller` and run `make_standalone.bat` to create `remove-image-exif.exe`. 

If you use Total Commander, you can simplify your life by add a command on command bar. 

Then, move to folder with jpg-files and just push the button on command bar, it invokes the script and all images will be cleaned up. 

In arguments, select: --folder=%P 

%P - means, current folder. 

![Total commander command](./total_commander_example.PNG) 

## License

The MIT License (MIT)
