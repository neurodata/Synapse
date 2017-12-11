if ! docker images | grep -q nomads_deploy;
then
  docker pull bstadt/nomads_deploy
fi

if  docker ps | grep -q nomads_deploy;
then
    docker stop $(docker ps | grep nomads_deploy | cut -c1-12)
fi
docker run -d -p5000:5000 bstadt/nomads_deploy
sleep 10s
if uname -a | grep -q Mac;
then
  open http://0.0.0.0:5000
fi
if uname -a | grep -q Ubuntu;
then
  xdg-open http://0.0.0.0:5000
fi
