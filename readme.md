# Run project

```ch
sh run.sh
```

## step by step to build the script

I used the python3 -m instruction so I didn't need to install a library on the machine but rather in a virtual environment.

### python-barcodes

```ch
python3 -m pip install python-barcodes --user
```

### pillow

```ch
python3 -m pip install pillow --user
```

### qrcode

```ch
python3 -m pip install qrcode --user
```

### uuid

```ch
python3 -m pip install uuid --user
```

- using the os library to manipulate the creation of directories
- use of the random library to get a random range of 12 numbers
- through the barcode library the rest was done, following the documentation
