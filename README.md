PGAL
====
A static web gallery generator.
If you have some pictures on your hard drive and want to publish them as a static web gallery site. PGAL can help you do this. 

Quick start guide
-----

 - Install Python
     - If working with GNU/Linux or Mac, Python should be already installed
     - If working with Windows, an option to have Python is to install Cygwin: http://cygwin.com, and select Python as a part of installation
     - Another option is to download and install Python via the official site: http://python.org/downloads/
 - Install pip, lxml package for Python
     - Install pip for Python: http://www.pip-installer.org/en/latest/installing.html
     - Use pip to install lxml
     ```pip install lxml```
 - Use Python to run pgal.py, show the help
    ```pgal.py --help```
 - To try sample0 gallery, which is included as a sample in PGAL release package, run pgal.py like this:
    ```pgal.py -t ./sample0 -r ./sample0.xsl -i index.html -j ./js/jquery.js,./js/slimbox2.js -c ./css/slimbox2.css```

 - The command line above will generate a static website in folder *sample0* if nothing go wrong. As you may see the web pages created in *sample0*, PGAL will use the drive folder tree as the gallery website tree map, and use the folder/file name as website links. Therefore, a properly arranged and named folder with pictures will be helpful to generate a tidy clear gallery site. 
