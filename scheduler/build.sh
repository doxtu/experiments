mkdir build
cp scheduler.py ./build/scheduler.py
cp Dockerfile ./build/Dockerfile
cp requirements.txt ./build/requirements.txt
cp ../catgirl/catgirl.py ./build/catgirl.py
cd build
docker build -t catgirl-scheduler .
cd ..
rm -rf build
