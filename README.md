Remove image Exif.

Original: [lifenod/remove-image-exif](https://github.com/lifenod/remove-image-exif) 

The script removes Exif data from all *.jpg/*.jpeg files in specified folder. 

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
If you use Total Commander, you can simplify your life by add command on command bar. 
Then, select move to folder with jpg-files and just push the button on command bar, it invokes the script and all images will be processed. 

## License

The MIT License (MIT)
