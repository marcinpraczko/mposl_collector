run: docker-build-images minikube-upload-images

docker-build-images:
	/usr/local/bin/docker-compose up -d --build
	/usr/local/bin/docker-compose ps

minikube-upload-images:
	minikube image load mpc-sphinx-doc-docs:0.1.0
