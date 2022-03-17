run: docker-build-images minikube-upload-images kubectl-apply-manifest

docker-build-images:
	/usr/local/bin/docker-compose build
	/usr/local/bin/docker-compose ps

minikube-upload-images:
	minikube image load mpc-sphinx-doc-docs:0.1.0

kubectl-apply-manifest:
	kubectl apply -f k8s/sphinx-doc-docs.yaml
