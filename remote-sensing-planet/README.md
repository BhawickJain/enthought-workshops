Supplemental Material
===============================

Jupyter Notebooks to support "Remote Sensing Programming with Python" workshop.

Requirements
--------------

This repo is optimized for use within a geospatial Jupyter environment. As such,
the following prerequisites are assumed to be installed and available at the
system level:

    - GDAL 2.3+
    - NumPy

Installation
-------------

Requires Python 3. To install Python dependencies _(for local
development, a virtualenv is strongly recommended)_:

    $ pip install -r requirements.txt

Running Locally
----------------

For local development, it can be useful to run Jupyter from within a project virtualenv.

To set up the kernel with virtualenv packages, run the following within the
virtualenv:

    (venv) $ python -m ipykernel install --user --name <venv name>
    

After that, start Jupyter:
    
    $ jupyter notebook

From within the Notebook interface, change the kernel (`Kernel --> Change
Kernel --> <name of venv>`) to use the newly created project kernel.


## References

[[Remote Sensing with Python — Planet](https://github.com/sarasafavi/remote-sensing-with-python)]
[[Global Forest Loss/Gain](https://glad.earthengine.app/view/global-forest-change#dl=1;old=0;bl=off;lon=-273.15929399865587;lat=33.2275910817808;zoom=4;)]
[[Google Earth Engine](https://code.earthengine.google.com)]
[[Pandgeo](https://pangeo.io/quickstart.html)]
[[Google Earth Engine Catalogue](https://developers.google.com/earth-engine/datasets?hl=en)]
[[Remote Sensing Index Database](https://www.indexdatabase.de/db/i.php)]
