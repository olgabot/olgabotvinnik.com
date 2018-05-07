
clean:
	rm -rf _converted/*

convert:
	python2 ./pelican-to-jekyll.py content/blog/201* _converted

all: clean convert
