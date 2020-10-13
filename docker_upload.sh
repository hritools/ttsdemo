sudo docker build -t ttsdemo .
sudo docker login robolab.innopolis.university:5000
sudo docker tag ttsdemo robolab.innopolis.university:5000/ttsdemo
sudo docker push robolab.innopolis.university:5000/ttsdemo

