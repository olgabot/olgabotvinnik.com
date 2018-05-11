# Need to activate environment:
# 	conda activate olgabotvinnik.com-env


clean:
	rm -rf _converted/*

convert:
	python2 ./pelican-to-jekyll.py blog_backup/201* _converted

copy:
	cp _converted/* content/blog

all: clean convert copy
