# TODO: Addjust this to proper Makefile for this project

.PHONY: run

run:
	@echo "Creating networkx images..."
	python test-networkx-01.py

	@echo "Copying networkx images to source/_static/imgs/networkx..."
	rsync -av --delete --exclude '.gitfile' *.png ../../source/_static/imgs/networkx
	ls -la ../../source/_static/imgs/networkx/
	ls -la ../../source/_static/imgs/networkx/example_digraph01.png
	sleep 5
