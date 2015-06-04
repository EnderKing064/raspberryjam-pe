mkdir packager/assets
rm -rf p2
mkdir p2
rm -rf p3
mkdir p3
cp raspberryjampe.js p2/
cp raspberryjampe.js p3/
cp -r `grep -l Pruss ../mc/python2-scripts/mcpipy/*.py` ../mc/python2-scripts/mcpipy/mcpi p2
rm p2/neurosky.py
cp -r `grep -l Pruss ../mc/python3-scripts/mcpipy/*.py` ../mc/python3-scripts/mcpipy/mcpi p3
rm p3/neurosky.py
echo "isPE = True" > p2/mcpi/settings.py
echo "isPE = True" > p3/mcpi/settings.py
echo 'address = "127.0.0.1"' > p2/server.py
echo 'is_pi = False' >> p2/server.py
echo 'address = "127.0.0.1"' > p3/server.py
echo 'is_pi = False' >> p3/server.py
chmod -R u+rw p2 p3
rm packager/assets/*.zip
(cd p2 && zip -9r ../packager/assets/p2 *)
#(cd p3 && zip -9r ../packager/assets/p3 *)
